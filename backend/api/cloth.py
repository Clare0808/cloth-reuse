from flask import request, jsonify
from . import api_bp
import os
import json
import shutil
from werkzeug.utils import secure_filename

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA_FILE = os.path.join(BASE_DIR, "backend", "static", "data", "clothData.json")
UPLOAD_CLOTH_DIR = os.path.join(BASE_DIR, "upload", "cloth")
STATIC_CLOTH_DIR = os.path.join(BASE_DIR, "backend", "static", "img", "cloth")

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

    src_path = os.path.join(UPLOAD_CLOTH_DIR, data.get("image"))
    dst_path = os.path.join(STATIC_CLOTH_DIR, data.get("image"))

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
    os.makedirs(UPLOAD_CLOTH_DIR, exist_ok=True)
    save_path = os.path.join(UPLOAD_CLOTH_DIR, new_filename)

    image.save(save_path)
    return jsonify({
        "message": "儲存成功!",
        "data": new_filename
    }), 200

@api_bp.route("/delete-cloth", methods=['POST'])
def deleteCloth():
    data = request.get_json()

    id = data.get("id")

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        cloths = json.load(f)

    new_cloths = [c for c in cloths if c.get("id") != id]

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(new_cloths, f, ensure_ascii=False, indent=2)

    return jsonify({
        "message": "刪除成功"
    }), 200

@api_bp.route("/modify-cloth", methods=['POST'])
def modifyCloth():
    data = request.get_json()

    id = data.get("id")

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        cloths = json.load(f)

    id = data.get("id")
    for cloth in cloths:
        if cloth.get("id") == id:
            cloth["name"] = data.get("name", cloth["name"])
            cloth["description"] = data.get("situation", cloth["description"])
            cloth["size"] = data.get("size", cloth["size"])
            cloth["image"] = data.get("image", cloth["image"])
            cloth["place"] = data.get("place", cloth["place"])
            cloth["time"] = data.get("time", cloth["time"])
            cloth["category"] = data.get("category", cloth["category"])
            cloth["lock"] = data.get("lock", cloth["lock"])
            
            break

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(cloths, f, ensure_ascii=False, indent=2)

    return jsonify({
        "message": "修改成功"
    }), 200
