from flask import Flask, flash, redirect, render_template, request, json
import os
import urllib.request
from jinja2 import ext
from datetime import datetime

app = Flask(__name__)

with urllib.request.urlopen("http://apis.is/petrol") as url:
    gogn = json.loads(url.read().decode())
    li = gogn['results']

app.jinja_env.add_extension(ext.do)

def minPetrol():
    minverd = 10000000000
    for x in li:
        if x['bensin95'] < minverd:
            nafn = x['company']
            minverd = x['bensin95']
    return [minverd ,nafn]

def minDiesel():
    minverd = 10000000000
    for x in li:
        if x['diesel'] < minverd:
            minverd = x['diesel']
            nafn =x['company']
    return [minverd, nafn]

def stadir():
    stodvar = {}
    for x in li:
        nafn = x["company"]
        if nafn not in stodvar:
            stodvar[nafn] = [{
                "bensin": x["bensin95"],
                "diesel": x["diesel"],
                "geo": x["geo"],
                "nafn": x["name"],
                "company": x["company"]
                }]
        else:
            stodvar[nafn].append({
                "bensin":x["bensin95"],
                "diesel":x["diesel"],
                "geo":x["geo"],
                "nafn":x["name"],
                "company":x["company"]})
    return stodvar



#-----------------------routes--------------------------------------

@app.route("/")
def index():
    oneco = []
    for x in li:
        if x['company'] not in oneco:
            oneco.append(x['company'])

    return render_template("index.html",oneco = oneco, minP=minPetrol(), minD=minDiesel())

def header():
    pass


@app.route("/company/<nafn>")
def fyrirtaeki(nafn):
    listi = stadir()
    return render_template("stadir.html",nafn = nafn, stodvar = listi[nafn])

@app.route("/<company>/<nafn>")
def stod(nafn,company):
    listi = stadir()[company]
    for i in listi:
        if i["nafn"] == nafn:
            dic = i
            break
    return render_template("stod.html",nafn=dic["nafn"],lat=dic["geo"]["lat"],lon=dic["geo"]["lon"],company = company, bensin=dic["bensin"],diesel=dic["diesel"])

@app.errorhandler(404)
def pagenotfound(error):
    return render_template("404.html"), 404

#-------------------run---------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)

