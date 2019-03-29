import urllib.request
from flask import Flask, Response


app = Flask(__name__)

@app.route("/")
def hello():
    return "My name is Ella"

@app.route("/weather/<LAT>/<LONG>")
def weather(LAT, LONG):

    with urllib.request.urlopen('https://api.met.no/weatherapi/locationforecast/1.9/?lat=' + LAT + '&lon=' + LONG) as response:
        html = response.readlines()


    responses = str()

    for line in html:

        if "<time" in line.decode("utf-8"):
            time = line.decode("utf-8")

        if "<minTemperature" in line.decode("utf-8"):
            mintemp = line.decode("utf-8")

        if "<maxTemperature" in line.decode("utf-8"):
            maxtemp = line.decode("utf-8")
            break
       

    responses += "<h1>Ella's Weather Report</h1><xmp>"
    responses += mintemp
    responses += time
    responses += maxtemp
    responses += "</xmp>"

    return Response(responses)