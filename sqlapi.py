from flask import Flask, request

import tools.postdata as pos
import tools.getdata as get

#Para renderizar el readme en formato html
import markdown.extensions.fenced_code 
from flask import jsonify

app = Flask(__name__)

#------------------------------------------
#GET
#------------------------------------------

#README

@app.route("/")
def index():
    readme_file = open("Readme.md", "r")
    md_template = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )
    return md_template

#Director info

@app.route("/director_info/<name>")
def inform_director(name):
    info = get.info_director(name)
    return jsonify(info)

#Season info

@app.route("/season_info/<num>")
def inform_season(num):
    info = get.info_season(num)
    return jsonify(info)

#Episodes by name

@app.route("/episodes_name/<name>")
def info_cap_nombre(name):
    episodio = get. info_capitulo_nombre(name)
    return jsonify(episodio)

#Episodes by season

@app.route("/episodes_temp/<num>")
def info_cap_temp(num):
    temp = get.info_capitulo_temporada(num)
    return jsonify(temp)

#Episodes by director

@app.route("/episodes_by_director/<name>")
def epi_by_director(name):
    episodios = get.episodios_director(name)
    return jsonify(episodios)

#All info

@app.route("/all_info")
def toda_info():
    todo = get.toda_informacion()
    return jsonify(todo)

#------------------------------------------
#POST 
#------------------------------------------

#New director

@app.route("/new_director", methods=["POST"])
def inserta_dir():
    dir_id = request.form.get("Director_id")
    nombre = request.form.get("Name")
    num_epi = request.form.get("Episodes")

    pos.inserta_dir(dir_id, nombre, num_epi)

    return "New data have been succesfully updated"

#New Season

@app.route("/new_season", methods=["POST"])
def inserta_temp():
    temp_id = request.form.get("Season_id")
    temp = request.form.get("Season")
    ano = request.form.get("Year")
    capitulo = request.form.get("Episodes")

    pos.inserta_tempo(temp_id, temp, ano, capitulo)

    return "New Season have been succesfully uploaded"

#New Episode

@app.route("/new_episode", methods=["POST"])
def inserta_epis():
    epi_id = request.form.get("Episode_id")
    sea_id = request.form.get("Season_id")
    sea = request.form.get("Season")
    dir_id = request.form.get("Director_id")
    epi_num = request.form.get("Episode_Number")
    epi_tit = request.form.get("Episode_title")
    dur = request.form.get("Duration")
    suma = request.form.get("Summary")

    pos.inserta_epis(epi_id, sea_id, sea, dir_id, epi_num, epi_tit, dur, suma)

    return "New data have been succesfully updated"

#New ranking

@app.route("/new_rank", methods=["POST"])
def inserta_ranking():
    epi_id = request.form.get("Episode_id")
    estre = request.form.get("Stars")
    votos = request.form.get("Votes")
    ana = request.form.get("SIA")

    pos.inserta_rank(epi_id, estre, votos, ana)

    return "New ranking have been uploaded"

#----------------------------------
#TO DO
#----------------------------------
#Pedir capitulos cuyo SIA sea mayor que o menor que
#Valorar SIA en positivo solo?
#Buscar capitulo por palabra usando regex





#This is necessary to automatically update the endpoints

app.run("0.0.0.0",5000, debug=True)