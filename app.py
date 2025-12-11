from flask import Flask, render_template
from data_reader import *
import json

app = Flask(__name__)

@app.route('/')
def test():
    data = json.dumps(get_agent_time("data/FY20-25.csv"))
    return render_template("test.html", data=data)