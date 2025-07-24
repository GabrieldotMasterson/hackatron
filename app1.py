from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import app, db
from factory import oportunidades_db, mulheres_db

with app.app_context():
    db.create_all()

@app.get("/")
def index():
    valores_oportunidades = oportunidades_db.query.all()
    return render_template("index.html", oportunidades=valores_oportunidades)

@app.post("/add_oportunidade")
def add_oportunidade():
    title = request.form.get('titulo')
    subtitle = request.form.get('subtitulo')
    detalhe = request.form.get('detalhes')
    img = request.form.get('img')
    link = request.form.get('link')
    nova_oportunidade = oportunidades_db(titulo=title, subtitulo=subtitle, img=img, detalhes=detalhe, link=link)
    db.session.add(nova_oportunidade)
    db.session.commit()
    return redirect(url_for("index"))

@app.get("/add_oportunidade")
def form_oportunidade():
    return render_template("form_oportunidade.html")

@app.get("/add_mulher")
def form_mulher():
    return render_template("form_mulheres.html")

from datetime import date

@app.post("/add_mulher")
def add_mulher():
    nome = request.form.get('nome')
    texto = request.form.get('texto')
    img = request.form.get('img')
    data = request.form.get('data')
    nova_mulher = mulheres_db(nome=nome, texto=texto, img=img, data=data)
    db.session.add(nova_mulher)
    db.session.commit()
    return redirect(url_for("index"))


@app.get("/contato")
def contato():
    return render_template("contato.html")

@app.get("/sobre")
def sobre():
    return render_template("Sobre-nos.html")

@app.get("/museu")
def museu():
    valores_mulheres = mulheres_db.query.all()
    return render_template("museu.html" , mulheres = valores_mulheres)

@app.get("/detalhe/<int:id>")
def detalhes(id):
    oportunidade = oportunidades_db.query.get_or_404(id)
    return render_template("detalhes.html", detalhe=oportunidade)


if __name__ == "__main__":
    app.run(debug=True)