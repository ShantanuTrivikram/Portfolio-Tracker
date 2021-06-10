import pandas as pd
import numpy as np
from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
import datetime as dt
from mf_code import *

app = Flask(__name__)
CORS(app)

#Returns a dict with codes as the key and mf names as its value
mf_codelist = mf_code()
@app.route('/home/mfcodes', methods=['GET'])
def api_mfcode():
    return jsonify(mf_codelist)




app.run(debug = True)
