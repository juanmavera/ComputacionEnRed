from flask import Flask
from DataObtainer import *
from MongoHandler import *
from BeebotteHandler import *

import threading
import time

app = Flask(__name__)


def InitPeriodicDataObtainer():
    Data = DataObtainer()
    page = Data.get_web()
    Noticia = Data.get_web_data(page)

    mongoDB = MongoHandler()
    mongoDB.InsertNew(Noticia)

    bbtDB = BeebotteHandler()
    bbtDB.InsertNew(Noticia)

    print("Clicks: %d || Meneos: %d || Noticia: %s || Fecha: %s || Hora: %s\n" % (int(float(Noticia[0])), int(float(Noticia[1])), str(Noticia[2]), str(Noticia[3]), str(Noticia[4])))

    threading.Timer(120, InitPeriodicDataObtainer).start()


@app.route('/')
def index():
    Data = DataObtainer()
    page = Data.get_web()
    Noticia = Data.get_web_data(page)

    cadena = "Clicks: %d || Meneos: %d || Noticia: %s || Fecha: %s || Hora: %s" % (int(float(Noticia[0])), int(float(Noticia[1])), str(Noticia[2]), str(Noticia[3]), str(Noticia[4]))
    return '<p> %s </p>' %(cadena)


@app.route('/loc')
def location():
    return'<p> UAH </p>'


if __name__ == '__main__':

    InitPeriodicDataObtainer()

    # app.debug = True
    # app.run(host='0.0.0.0')
