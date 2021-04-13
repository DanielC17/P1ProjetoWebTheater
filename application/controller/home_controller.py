from application import app
from flask import Flask, render_template, request, url_for
from application.model.dao.categoriaDAO import CategoriaDAO
from application.model.entity.categoria import Categoria
from application.model.entity.video import Video
from application import categorylist
from application import listvideo


@app.route('/')
def index():
    categoriaDAO = CategoriaDAO()
    return render_template("index.html", categoria_list = categoriaDAO.get_categorylist())

@app.route('/<titulo>')
def video(titulo):
    for video in listvideo:
        if video.get_titulo() == titulo:
            return render_template("video.html", video = video)
    return render_template("index.html", categoria_list = categorylist)
