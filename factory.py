from config import app, db

class oportunidades_db(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    subtitulo = db.Column(db.String(100), nullable=False)
    detalhes = db.Column(db.String(3000))
    img = db.Column(db.String(500))
    link = db.Column(db.String(500))

class mulheres_db(db.Model):
    __bind_key__ = 'mulheres'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    texto = db.Column(db.String(100), nullable=False)
    data = db.Column(db.String(20), nullable=False)
    img = db.Column(db.String(500))
