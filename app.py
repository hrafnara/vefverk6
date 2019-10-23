from flask import Flask, flash, redirect, render_template, request, json
import os
import urllib.request
from jinja2 import ext
from datetime import datetime

app = Flask(__name__)

with urllib.request.urlopen("http://apis.is/petrol") as url:
    gogn = json.loads(url.read().decode())
#    print(gogn)

app.jinja_env.add_extension(ext.do)

def minPetrol():
    return 100
#    minPetrol = 1000
#    company = None
#    adress = None
#    lst = gogn['results']
#    for i in lst:
#        if i['bensin95'] is not None:
#            pass
def minDiesel():
    return 1000

#-----------------------routes--------------------------------------

@app.route("/")
def index():
    return render_template("index.tpl",gogn =gogn, minP=minPetrol(), minD=minDiesel())


#-------------------run---------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)