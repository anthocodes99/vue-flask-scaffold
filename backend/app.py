import os

from flask import Flask, url_for, send_from_directory

app = Flask(__name__, root_path=os.path.abspath("../"), static_url_path='/', static_folder='dist')

app.config["DEBUG"] = True
# app.config["APPLICATION_ROOT"]

@app.route("/")
def index():
    return send_from_directory('dist', 'index.html')