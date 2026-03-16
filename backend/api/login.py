from flask import request, jsonify
from . import api_bp
from database import db
from model.login import Login

@api_bp.route("/login", methods=["GET"])
def login():
    data = Login.query.all()

    data_list = [{
        "email": info.email, 
        "name": info.name, 
        "phone": info.phone, 
        "password": info.password
    } for info in data]

    return jsonify({
        "data": data_list,
        "message": "登入成功!"
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
            "message": "該E-mail已存在!",
            "data": {
                "email": email,
                "name": name,
                "phone": phone
            }
        }), 400

    login = Login(
        email = email,
        name = name,
        phone = phone,
        password = password
    )

    db.session.add(login)
    db.session.commit()

    return jsonify({
        "message": "註冊成功!",
        "data": {
            "email": email,
            "name": name,
            "phone": phone
        }
    }), 200