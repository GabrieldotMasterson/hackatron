from config import app, db

class oportunidades_db(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(100), nullable=False)
    detalhes = db.Column(db.String(3000))
    img = db.Column(db.String(500))
