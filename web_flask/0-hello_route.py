#!/usr/bin/python3
""" Flask first app """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_HBTN():
    return 'Hello HBNB!'
