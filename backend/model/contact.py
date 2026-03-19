from database import db

class Contact(db.Model):
    __tablename__ = 'contact'
    
    contact_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.Text, nullable=True)
    name = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=True)
    time = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Contact {self.contact_id}>'