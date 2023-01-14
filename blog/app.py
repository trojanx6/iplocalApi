
from flask import Flask, redirect, url_for, request, render_template, session
from ip2geotools.databases.noncommercial import DbIpCity

app = Flask(__name__)

@app.route("/iplocal")
def index():
    geoip  = request.args.get("ip")
    geolocal = DbIpCity.get(geoip, api_key="free")
    return geolocal.to_json()

if __name__ == "__main__":
    app.run(debug=True,port=1453)
