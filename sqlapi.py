from flask import Flask, request

import tools.postdata as pos
import tools.getdata as get

app = Flask(__name__)














app.run("0.0.0.0",5000, debug=True)