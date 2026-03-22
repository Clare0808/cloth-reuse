from flask import request, jsonify
from . import api_bp
from database import db
from model.pickup import Pickup
import json

DATA_FILE = "C:\\Users\\user\\Documents\\Self_Practice\\cloth-reuse\\public\\data\\clothData.json"

@api_bp.route("/send-pickup", methods=["POST"])
def sendPickup():
    data = request.get_json()

    rEmail = data.get("rEmail")
    rName = data.get("rName")
    name = data.get("name")
    type = data.get("type")
    size = data.get("size")
    situation = data.get("situation")
    time = data.get("time")
    place = data.get("place")
    pEmail = data.get("pEmail")
    pName = data.get("pName")
    image = data.get("image")

    pickup = Pickup(
        rEmail = rEmail,
        rName = rName,
        name = name,
        type = type,
        size = size,
        situation = situation,
        time = time,
        place = place,
        pEmail = pEmail,
        pName = pName,
        image = image
    )

    db.session.add(pickup)
    db.session.commit()

    return jsonify({
        "message": "儲存成功!"
    }), 200

@api_bp.route("/modify-file", methods=["POST"])
def modifyFile():
    data = request.get_json()

    name = data.get("name")
    
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        cloths = json.load(f)

    for item in cloths:
        if item["name"] == name:
            item["lock"] = not item["lock"]
            break

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(cloths, f, ensure_ascii=False, indent=2)

    return jsonify({
        "message": "修改成功!"
    }), 200

@api_bp.route("/get-pickup", methods=["GET"])
def getPickup():
    infos = Pickup.query.all()

    data_list = [{
        "id": info.pickup_id,
        "rEmail": info.rEmail,
        "rName": info.rName,
        "name": info.name,
        "type": info.type,
        "size": info.size,
        "situation": info.situation,
        "time": info.time,
        "place": info.place,
        "pEmail": info.pEmail,
        "pName": info.pName,
        "image": info.image
    } for info in infos]

    return jsonify({
        "data": data_list
    }), 200

@api_bp.route("/delete-pickup", methods=["POST"])
def deletePickup():
    data = request.get_json()

    id = data.get("id")

    pickup = Pickup.query.filter_by(pickup_id = id).first()

    db.session.delete(pickup)
    db.session.commit()

    return jsonify({
        "message": "刪除成功"
    }), 200
