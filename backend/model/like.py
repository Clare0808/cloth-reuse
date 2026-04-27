from database import db

class Like(db.Model):
    __tablename__ = 'like'
    
    like_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text, nullable=True)
    size = db.Column(db.Text, nullable=True)
    situation = db.Column(db.Text, nullable=True)
    time = db.Column(db.Text, nullable=True)
    place = db.Column(db.Text, nullable=True)
    pEmail = db.Column(db.Text, nullable=False)
    pName = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Like {self.like_id}>'