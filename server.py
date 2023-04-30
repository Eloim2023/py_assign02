from flask import Flask
import json
from config import db

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from Flask"

@app.get("/test")
def test():
    return "This is another page"


#### API ENDPOINTS ####
######   JSON      ###

@app.get("/api/about")
def about():
    me = {"name": "Eloim Arreola"}
    return json.dumps(me)

app.run(debug=True)