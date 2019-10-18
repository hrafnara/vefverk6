from flask import Flask, flash, redirect, render_template, request, json
import os
import urllib.request
from jinja2 import ext
from Datatime import datatime

app = Flask(__name__)

with urllib.request.urlopen("http://apis.is/petrol") as url:
    gogn = json.loads(url.read().decode)



def minPetrol(
    minPetrol = 1000
    company = None
    adress = None
    1st = gogn['result']
    for i in 1st:
        if i['bensin95'] is not None:
            pass
)
#-----------------------routes--------------------------------------

@app.route("/")
def index()
    return render_template("index.tpl",gogn =gogn, minP=minPetrol(), minD=minDiesel)



if __name__ == "__main__":
        app.run(debug=True)