from flask import request, jsonify
from . import api_bp
from database import db
from model.finish import Finish

@api_bp.route("/send-finish", methods=["POST"])
def sendFinish():
    data = request.get_json()

    rEmail = data.get("rEmail")
    rName = data.get("rName")
    name = data.get("name")
    code = data.get("code")
    type = data.get("type")
    size = data.get("size")
    time = data.get("time")
    oTime = data.get("oTime")
    place = data.get("place")
    pEmail = data.get("pEmail")
    pName = data.get("pName")
    image = data.get("image")


    finish = Finish(
        rEmail = rEmail,
        rName = rName,
        name = name,
        code = code,
        type = type,
        size = size,
        time = time,
        oTime = oTime,
        place = place,
        pEmail = pEmail,
        pName = pName,
        image = image,
    )

    db.session.add(finish)
    db.session.commit()

    return jsonify({
        "message": "儲存成功!"
    }), 200

@api_bp.route("/get-finish", methods=["GET"])
def getFinish():
    infos = Finish.query.all()

    data_list = [{
        "rEmail": info.rEmail,
        "rName": info.rName,
        "name": info.name,
        "code": info.code,
        "type": info.type,
        "size": info.size,
        "time": info.time,
        "oTime": info.oTime,
        "place": info.place,
        "pEmail": info.pEmail,
        "pName": info.pName,
        "image": info.image
    } for info in infos]

    return jsonify({
        "data": data_list
    }), 200
