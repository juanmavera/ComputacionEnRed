from flask import Flask
from DataObtainer import *


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Aplicacion </h1>'


@app.route('/loc')
def location():
    return'<p> UAH </p>'


if __name__ == '__main__':

    Data = DataObtainer()
    page = Data.get_web()
    Noticia = Data.get_web_data(page)

    print("Clicks: %d || Meneos: %d || Noticia: %s" % (int(float(Noticia[0])), int(float(Noticia[1])), str(Noticia[2])))
    # app.debug = True
    # app.run(host='0.0.0.0')
