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

# 導向 Google 登入頁面
@api_bp.route("/auth-google", methods=["GET"])
def googleLogin():
    params = {
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": GOOGLE_CALLBACK_URL,
        "response_type": "code",
        "scope": "openid email profile", # 確保 Google 回傳使用者的基本資料和 email
        "access_type": "offline",
        "prompt": "consent"
    }

    url = "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode(params)
    return redirect(url)

@api_bp.route("/auth-callback", methods=["GET"])
def googleCallback():
    code = request.args.get("code")

    # 用 code 換 token
    token_res = requests.post(
        "https://oauth2.googleapis.com/token",
        data={
            "client_id": GOOGLE_CLIENT_ID,
            "client_secret": GOOGLE_CLIENT_SECRET,
            "code": code,
            "redirect_uri": GOOGLE_CALLBACK_URL,
            "grant_type": "authorization_code",
        }
    ).json()

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

    return redirect(f"http://localhost:8080/?token={access_token}")

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
