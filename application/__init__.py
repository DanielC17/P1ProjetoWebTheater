from flask import Flask, render_template, request, url_for
import os
from application.model.entity.video import Video
from application.model.entity.categoria import Categoria

template_folder = os.path.abspath('application/view/templates')
static_folder = os.path.abspath("application/view/static")

app = Flask(__name__, template_folder = template_folder, static_folder = static_folder)


listvideo = []
listvideo.append(Video("/videos/vingadores.mp4", "/img/vingadores.png", "Vingadores Ultimato", "Ação", 0, 0, "25/04/2019"))
listvideo.append(Video("/videos/ultimomen.mp4", "/img/ultimomen.png", "Ultimo Homem", "Realidade", 0, 0, "26/01/2017"))
listvideo.append(Video("/videos/peakyblienders1.mp4", "/img/pky.jpg", "Peaky Blinders", "by order of the peaky blinders", 0, 0, "12/09/2013"))
listvideo.append(Video("/videos/break1.mp4", "/img/break.png", "Breaking Bad", "Drogas", 0, 0, "17/07/2008"))
listvideo.append(Video("/videos/onepiece1.mp4", "/img/onepiecezada.png", "One Piece", "Piratas", 0, 0, "22/07/1997"))
listvideo.append(Video("/videos/tatakae.mp4", "/img/tatakae.png", "Atack ao titan", "Titans", 0, 0, "10/11/2010"))

categorylist = []
categorylist.append(Categoria(1, "Filmes", "Melhores filmes", "", listvideo[0:2]))
categorylist.append(Categoria(2, "Series", "Melhores Series", "", listvideo[2:4]))
categorylist.append(Categoria(3, "Animes", "Melhores Animes", "", listvideo[4:6]))


from application.controller import home_controller