from flask import request, jsonify
from . import api_bp
from database import db
from model.login import Login
from flask_jwt_extended import create_access_token

@api_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    existData = Login.query.all()

    data_list = [{
        "email": info.email, 
        "name": info.name, 
        "phone": info.phone,
        "password": info.password
    } for info in existData]

    user = next((item for item in data_list if item["email"] == email), None)

    if not user :
        return jsonify({
            "message": "該E-mail不存在!"
        }), 400

    if user["password"] != password :
        return jsonify({
            "message": "密碼錯誤!"
        }), 400
    
    # 產生 JWT token
    access_token = create_access_token(identity=email)

    return jsonify({
        "message": "登入成功!",
        "token": access_token
    }), 200

@api_bp.route("/signup", methods=["POST"])
def signup() :
    data = request.get_json()

    email = data.get("email")
    name = data.get("name")
    phone = data.get("phone")
    password = data.get("password")

    existing_user = Login.query.filter_by(email = email).first()
    if existing_user:
        return jsonify({
            "message": "該E-mail已存在!"
        }), 400

    login = Login(
        email = email,
        name = name,
        role = "user",
        phone = phone,
        password = password
    )

    db.session.add(login)
    db.session.commit()

    return jsonify({
        "message": "註冊成功!"
    }), 200

@api_bp.route("/get-user-info", methods=["GET"])
def getData():
    infos = Login.query.all()

    data_list = [{
        "id": info.login_id,
        "email": info.email, 
        "name": info.name, 
        "role": info.role,
        "phone": info.phone,
    } for info in infos]

    return jsonify({
        "data": data_list,
    }), 200

@api_bp.route("/delete-user", methods=["POST"])
def deleteUser() :
    data = request.get_json()

    id = data.get("id")

    login = Login.query.filter_by(login_id = id).first()

    db.session.delete(login)
    db.session.commit()

    return jsonify({
        "message": "刪除成功"
    }), 200

@api_bp.route("/modify-user", methods=["POST"])
def modifyUser() :
    data = request.get_json()

    id = data.get("id")

    login = Login.query.filter_by(login_id = id).first()

    login.role = data.get("role", login.role)

    db.session.commit()

    return jsonify({
        "message": "修改成功"
    }), 200

def init_admin() :
    exist_user = Login.query.filter_by(email = "clothReuseAdmin@gmail.com").first()

    if not exist_user :
        login = Login (
            email = "clothReuseAdmin@gmail.com",
            name = "初始管理者",
            role = "admin",
            password = "clothreuseadmin"
        )

        db.session.add(login)
        db.session.commit()