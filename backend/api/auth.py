from flask import request, jsonify, redirect
from . import api_bp
from database import db
from model.login import Login
import os
import requests
from dotenv import load_dotenv
import urllib.parse
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

# 載入 .env
load_dotenv()

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_CALLBACK_URL = os.getenv("GOOGLE_CALLBACK_URL")

def get_configured_callback_url():
    if not GOOGLE_CALLBACK_URL:
        return None

    callback_url = GOOGLE_CALLBACK_URL.rstrip("/")
    if "localhost" in callback_url or "127.0.0.1" in callback_url:
        return None

    return callback_url

def get_google_callback_url():
    configured_callback_url = get_configured_callback_url()
    if configured_callback_url:
        return configured_callback_url

    proto = request.headers.get("X-Forwarded-Proto", request.scheme)
    host = request.headers.get("X-Forwarded-Host", request.host)

    proto = proto.split(",")[0].strip()
    host = host.split(",")[0].strip()

    if host.endswith(".onrender.com"):
        proto = "https"

    request_callback_url = f"{proto}://{host}/api/auth-callback"

    if host.endswith(".onrender.com"):
        return request_callback_url

    return request_callback_url

def get_missing_google_config():
    missing = []

    if not GOOGLE_CLIENT_ID:
        missing.append("GOOGLE_CLIENT_ID")

    if not GOOGLE_CLIENT_SECRET:
        missing.append("GOOGLE_CLIENT_SECRET")

    return missing

# 導向 Google 登入頁面
@api_bp.route("/auth-google", methods=["GET"])
def googleLogin():
    missing_config = get_missing_google_config()
    if missing_config:
        return jsonify({
            "error": "Google OAuth config is missing",
            "missing": missing_config
        }), 500

    callback_url = get_google_callback_url()

    params = {
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": callback_url,
        "response_type": "code",
        "scope": "openid email profile", # 確保 Google 回傳使用者的基本資料和 email
        "access_type": "offline",
        "prompt": "consent"
    }

    url = "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode(params)
    return redirect(url)

@api_bp.route("/auth-callback", methods=["GET"])
def googleCallback():
    missing_config = get_missing_google_config()
    if missing_config:
        return jsonify({
            "error": "Google OAuth config is missing",
            "missing": missing_config
        }), 500

    if request.args.get("error"):
        return redirect("/login")

    code = request.args.get("code")
    if not code:
        return redirect("/login")

    callback_url = get_google_callback_url()

    # 用 code 換 token
    token_res = requests.post(
        "https://oauth2.googleapis.com/token",
        data={
            "client_id": GOOGLE_CLIENT_ID,
            "client_secret": GOOGLE_CLIENT_SECRET,
            "code": code,
            "redirect_uri": callback_url,
            "grant_type": "authorization_code",
        }
    ).json()

    if "access_token" not in token_res:
        return jsonify({
            "error": "Google token exchange failed",
            "details": token_res
        }), 400

    access_token = token_res["access_token"]

    user_res = requests.get(
        "https://www.googleapis.com/oauth2/v2/userinfo",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    ).json()

    email = user_res["email"]
    name = user_res["name"]

    if not email:
        return jsonify({
            "error": "Google 沒有回傳 email",
            "details": user_res
        }), 400

    existData = Login.query.all()

    data_list = [{
        "email": info.email, 
        "name": info.name, 
        "phone": info.phone,
        "password": info.password
    } for info in existData]

    user = next((item for item in data_list if item["email"] == email), None)

    if not user :
        login = Login(
            email = email,
            name = name,
            role = "user",
            phone = "",
            password = ""
        )

        db.session.add(login)
        db.session.commit()

    # 產生 JWT token
    access_token = create_access_token(identity=email)

    return redirect(f"/?token={access_token}")

    # return jsonify({
    #     "message": "登入成功!",
    #     "token": access_token
    # }), 200

@api_bp.route("/profile", methods=["GET"])
@jwt_required()  # 驗證 JWT
def profile():
    # 取得目前登入的使用者身份 (這裡是 email)
    current_user_email = get_jwt_identity()
    user = Login.query.filter_by(email=current_user_email).first()

    if not user:
        return jsonify({"message": "Not logged in"}), 401

    # 重新簽發一個新的 JWT (可選)
    token = create_access_token(identity=user.email)

    return jsonify({
        "user": {
            "id": user.login_id,
            "email": user.email,
            "name": user.name,
            "role": user.role
        },
        "token": token
    }), 200

@api_bp.route("/logout", methods=["POST"])
def logout():
    return jsonify({"message": "已登出"}), 200
