from database import db

class Review(db.Model):
    __tablename__ = "revuew"
    
    review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    star = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Text, nullable=True)
    image = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Review {self.review_id}>'