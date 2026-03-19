from flask import request, jsonify
from . import api_bp
from database import db
from model.contact import Contact

@api_bp.route("/send-contact", methods=["POST"])
def sendContact():
    data = request.get_json()

    email = data.get("email")
    name = data.get("name")
    content = data.get("content")
    time = data.get("time")

    review = Contact(
        email = email,
        name = name,
        content = content,
        time = time
    )

    db.session.add(review)
    db.session.commit()

    return jsonify({
        "message": "success"
    }), 200


@api_bp.route("/get-contact", methods=["GET"])
def getContact():
    infos = Contact.query.all()

    data_list = [{
        "email": info.email,
        "name": info.name,
        "content": info.content,
        "time": info.time
    } for info in infos]

    return jsonify({
        "data": data_list
    }), 200