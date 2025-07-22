from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import app, db
from factory import oportunidades_db

with app.app_context():
    db.create_all()

@app.get("/")
def index():
    valores_oportunidades = oportunidades_db.query.all()
    return render_template("index.html", oportunidades=valores_oportunidades)

@app.post("/add")
def add_oportunity():
    title = request.form.get('titulo')
    subtitle = request.form.get('subtitulo')
    detalhe = request.form.get('detalhes')
    img = request.form.get('img')
    new_oportunity = oportunidades_db(title=title, subtitle=subtitle, img=img, detalhes=detalhe)
    db.session.add(new_oportunity)
    db.session.commit()
    return redirect(url_for("index"))

@app.get("/add")
def get_form():
    return render_template("form.html")

@app.get("/contato")
def get_contato():
    return render_template("contato.html")

@app.get("/detalhe/<int:id>")
def detalhes(id):
    oportunidade = oportunidades_db.query.get_or_404(id)
    return render_template("detalhes.html", oportunidade=oportunidade)


if __name__ == "__main__":
    app.run(debug=True)