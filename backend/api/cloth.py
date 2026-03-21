from flask import request, jsonify
from . import api_bp
import os
import json
import shutil
from werkzeug.utils import secure_filename

DATA_FILE = "C:\\Users\\user\\Documents\\Self_Practice\\cloth-reuse\\public\\data\\clothData.json"

@api_bp.route("/upload-cloth", methods=["POST"])
def uploadCloth():
    data = request.get_json()

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        cloths = json.load(f)

    new_cloth = {
        "id": data.get("id"),
        "name": data.get("name"),
        "description": data.get("situation"),
        "size": data.get("size"),
        "image": "/img/cloth/" + data.get("image"),
        "email": data.get("pEmail"),
        "pName": data.get("pName"),
        "place": data.get("place"),
        "time": data.get("time"),
        "category": data.get("type"),  
        "lock": data.get("lock")
    }

    cloths.append(new_cloth)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(cloths, f, ensure_ascii=False, indent=2)

    src_path = os.path.join("upload", "cloth", data.get("image"))
    dst_path = os.path.join("public", "img", "cloth", data.get("image"))

    # 確保目標資料夾存在
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)

    # 搬移檔案
    shutil.move(src_path, dst_path)

    return jsonify({
        "message": "儲存成功!"
    }), 200

@api_bp.route("/upload-cloth-image", methods=['POST'])
def uploadClothImage():
    image = request.files.get("image")  # 圖片檔案
    name = request.form.get("name") 

    original_name = secure_filename(image.filename)  # 安全處理原始檔名
    ext = os.path.splitext(original_name)[1]        # 取得副檔名 (.jpg, .png...)

    # 建立新檔名：UUID + 副檔名
    new_filename = f"{name}{ext}"
    save_path = os.path.join("./upload/cloth", new_filename)

    image.save(save_path)
    return jsonify({
        "message": "儲存成功!",
        "data": new_filename
    }), 200

