import numpy as np
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Aplicacion </h1>'


@app.route('/loc')
def location():
    return'<p> UAH </p>'


if __name__ == '__main__':
    # app = flask(__name__)
    app.debug = True
    app.run(host='0.0.0.0')
