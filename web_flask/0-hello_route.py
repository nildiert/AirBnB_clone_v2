#!/usr/bin/python3
""" Flask first app """
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_hbtn():
    return 'Hello HBNB!'
