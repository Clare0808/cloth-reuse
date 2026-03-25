from database import db

class Finish(db.Model):
    __tablename__ = "finish"
    
    finish_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rEmail = db.Column(db.Text, nullable=False)
    rName = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    code = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text, nullable=True)
    size = db.Column(db.Text, nullable=True)
    time = db.Column(db.Text, nullable=True)
    oTime = db.Column(db.Text, nullable=False)
    place = db.Column(db.Text, nullable=True)
    pEmail = db.Column(db.Text, nullable=False)
    pName = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Finish {self.finish_id}>'