#!/usr/bin/python3
""" First route Flask """
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_HBTN():
    return 'Hello HBTN!'


@app.route('/hbnb')
def HBNB():
    return 'HBNB'


@app.route('/c/<text>')
def c_function(text):
    return 'C ' + text.replace("_", " ")


@app.route('/python/')
@app.route('/python/<text>')
def python_function(text="is_cool"):
    return 'Python ' + text.replace("_", " ")


@app.route('/number/<int:n>')
def number_function(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
