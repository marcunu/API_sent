from flask import Flask, request

import tools.postdata as pos
import tools.getdata as get

#Para renderizar el readme en formato html
import markdown.extensions.fenced_code 
from flask import jsonify

app = Flask(__name__)

#GET

@app.route("/episodes_name/<name>")
def info_cap_nombre(name):
    episodio = get. info_capitulo_nombre(name)
    return jsonify(episodio)

@app.route("/episodes_temp/<num>")
def info_cap_temp(num):
    temp = get.info_capitulo_temporada(num)
    return jsonify(temp)

@app.route("/episodes_by_director/<name>")
def epi_by_director(name):
    episodios = get.episodios_director(name)
    return jsonify(episodios)


#POST 

@app.route("/new_director", methods=["POST"])
def inserta_dir():
    dir_id = request.form.get("Director_id")
    nombre = request.form.get("Name")
    num_epi = request.form.get("Episodes")
    pos.inserta_dir(dir_id, nombre, num_epi)

    return "New data have been succesfully updated"


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












app.run("0.0.0.0",5000, debug=True)