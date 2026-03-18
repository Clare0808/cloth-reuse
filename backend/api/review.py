from flask import request, jsonify
from . import api_bp
from database import db
from model.review import Review

@api_bp.route("/send-review", methods=["POST"])
def sendReview():
    data = request.get_json()

    email = data.get("email")
    name = data.get("name")
    content = data.get("content")
    star = data.get("star")
    date = data.get("date")
    image = data.get("image")

    review = Review(
        email = email,
        name = name,
        content = content,
        star = star,
        date = date,
        image = image
    )

    db.session.add(review)
    db.session.commit()

    return jsonify({
        "message": "success"
    }), 200


@api_bp.route("/get-review", methods=["GET"])
def getReview():
    infos = Review.query.all()

    data_list = [{
        "email": info.email,
        "name": info.name,
        "content": info.content,
        "star": info.star,
        "data": info.date,
        "image": info.image
    } for info in infos]

    return jsonify({
        "data": data_list
    }), 200