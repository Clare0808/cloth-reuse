from flask import request, jsonify
from . import api_bp
from database import db
from model.like import Like

@api_bp.route("/store-like", methods=["POST"])
def storeLike():
    data = request.get_json()

    name = data.get("name")
    type = data.get("type")
    size = data.get("size")
    situation = data.get("situation")
    time = data.get("time")
    place = data.get("place")
    image = data.get("image")

    like = Like(
        name = name,
        type = type,
        size = size,
        situation = situation,
        time = time,
        place = place,
        image = image
    )

    db.session.add(like)
    db.session.commit()

    return jsonify({
        "message": "儲存成功!"
    }), 200

@api_bp.route("/get-like", methods=["GET"])
def getLike():
    infos = Like.query.all()

    data_list = [{
        "name": info.name,
        "type": info.type,
        "size": info.size,
        "situation": info.situation,
        "time": info.time,
        "place": info.place,
        "image": info.image
    } for info in infos]

    return jsonify({
        "data": data_list
    }), 200

@api_bp.route('/delete-like', methods=['POST'])
def deleteLike():
    data = request.get_json()

    name = data.get("name")

    like = Like.query.filter_by(name = name).first()

    db.session.delete(like)
    db.session.commit()

    return jsonify({
        "message": "刪除成功"
    }), 200
