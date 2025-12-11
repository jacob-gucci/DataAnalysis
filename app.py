from flask import Flask, render_template
from data_reader import *

app = Flask(__name__)

@app.route('/')
def test():
    data = get_agent_time("data/FY20-25.csv").to_json(orient='records')
    print(data)
    return render_template("test.html", data=data)