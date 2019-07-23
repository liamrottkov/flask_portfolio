from app import app, db
from datetime import datetime

class Contact(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(80))
    message = db.Column(db.String(500))
    date_posted = db.Column(db.DateTime, default=datetime.now().date())
