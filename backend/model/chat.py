from database import db

class Chat(db.Model):
    __tablename__ = 'chat'
    
    chat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sender_email = db.Column(db.Text, nullable=False)
    receiver_email = db.Column(db.Text, nullable=False)
    message = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Chat {self.chat_id}>'