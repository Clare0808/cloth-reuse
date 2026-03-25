from database import db

class Login(db.Model):
    __tablename__ = 'login'
    
    login_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    role = db.Column(db.Text, nullable=False)
    phone = db.Column(db.Text, nullable=True)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Login {self.login_id}>'