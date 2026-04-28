from flask import request, jsonify
from . import api_bp
from database import db
from model.chat import Chat
from flask_socketio import SocketIO
from extensions import socketio
from flask_socketio import join_room as socketio_join_room
import pytz
from datetime import datetime, timezone
from sqlalchemy import or_, and_

import logging
logging.basicConfig(level=logging.INFO)

@socketio.on("join_room")
def joinRoom(data):
    room = data.get("room")

    if room :
        socketio_join_room(room)

@socketio.on("new_msg")
def sendMsg(data):
    sender_email = data.get("sender_email")
    receiver_email = data.get("receiver_email")
    message = data.get("message")
    time_str = data.get("time")
    room = data.get("room")

    taipei_zone = pytz.timezone("Asia/Taipei")  # 設定台灣時區

    # 將 ISO 時間字串轉為 datetime 物件
    if time_str:
        try:
            time = datetime.fromisoformat(time_str.replace("Z", "+00:00")).astimezone(taipei_zone)
        except ValueError:
            time = datetime.now(timezone.utc).replace(tzinfo=pytz.utc).astimezone(taipei_zone)
    else:
        time = datetime.now(timezone.utc)

    # 格式化時間
    taiwan_time = time.astimezone(pytz.timezone("Asia/Taipei"))
    formatted_time = taiwan_time.strftime("%p %I:%M")
    formatted_time = formatted_time.replace("AM", "上午").replace("PM", "下午")

    chat = Chat(
        sender_email = sender_email,
        receiver_email = receiver_email,
        message = message,
        time = time,
    )

    db.session.add(chat)
    db.session.commit()

    socketio.emit("new_msg", {
        "sender_email": sender_email,
        "receiver_email": receiver_email,
        "message": message,
        "time": formatted_time
    }, room = room)

@api_bp.route("/chat-history", methods=["GET"])
def getChatHistory():
    sender_email = request.args.get("sender_email", 0)
    receiver_email = request.args.get("receiver_email", 0)

    # 從資料庫中找出符合條件的訊息
    chat = Chat.query.filter(
        or_(
            and_(Chat.sender_email == sender_email, Chat.receiver_email == receiver_email),
            and_(Chat.sender_email == receiver_email, Chat.receiver_email == sender_email)
        )
    ).order_by(Chat.time).all() # 訊息案時間排序
    
    return jsonify([
        {
            "sender_email": msg.sender_email, 
            "receiver_email": msg.receiver_email,
            "message": msg.message, 
            "timestamp": msg.time.isoformat()}
        for msg in chat
    ])

@api_bp.route("/all-chat", methods=["GET"])
def returnAllChat():
    all_chats = Chat.query.all()
    return jsonify([
        {
            "sender_email": c.sender_email, 
            "receiver_email": c.receiver_email, 
            "message": c.message,
            "time": c.time,
        } for c in all_chats
    ])