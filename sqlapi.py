from flask import Flask, request

import tools.postdata as pos
import tools.getdata as get

#Para renderizar el readme en formato html
import markdown.extensions.fenced_code 
from flask import jsonify

app = Flask(__name__)

@app.route("/episodes_name/<name>")
def info_cap_nombre(name):
    episodio = get. info_capitulo_nombre(name)
    return jsonify(episodio)

@app.route("/episodes_by_director/<name>")
def epi_by_director(name):
    episodios = get.episodios_director(name)
    return jsonify(episodios)












app.run("0.0.0.0",5000, debug=True)