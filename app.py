from flask import Flask, flash, redirect, render_template, request, json
import os
import urllib.request
from jinja2 import ext
from Datatime import datatime

app = Flask(__name__)

with urllib.request.urlopen("http://apis.is/petrol") as url:
    gogn = json.loads(url.read().decode)

#-----------------------routes--------------------------------------

@app.route("/")
def index()
    return render_template("index.tpl",gogn =gogn, minP=minPetrol(), minD=minDiesel)
