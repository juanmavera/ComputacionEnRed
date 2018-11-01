from flask import Flask
from DataObtainer import *
from MongoHandler import *
from BeebotteHandler import *

import threading
import time
import numpy as np

app = Flask(__name__)

usedDB = True


def InitPeriodicDataObtainer():
    Data = DataObtainer()
    page = Data.get_web()
    Noticia = Data.get_web_data(page)

    mongoDB = MongoHandler()
    mongoDB.InsertNew(Noticia)

    bbtDB = BeebotteHandler()
    bbtDB.InsertNew(Noticia)

    threading.Timer(120, InitPeriodicDataObtainer).start()


def CalculaMedia(Mongo=True):
    if Mongo:
        mongoDB = MongoHandler()
        Noticias = mongoDB.LeerNoticias()

    else:
        bbtDB = BeebotteHandler()
        Noticias = bbtDB.LeerNoticias()

    mediaClics = np.mean(Noticias[0])
    mediaMeneos = np.mean(Noticias[1])

    print('\nNoticias\n--------\n')
    for noticia in Noticias[2]:
        print(noticia)

    print('\n\nEstadisticas\n------------\n')
    print('Numero medio de clics obtenidos: %.2f\n'
          'Numero medio de meneos obtenidos: %.2f\n'
          'Numero de noticias: %d\n'
          % (mediaClics, mediaMeneos, len(Noticias[2])))

    return mediaClics, mediaMeneos, len(Noticias[2])


@app.route('/', methods=['GET','POST'])
def index():
    global usedDB

    if request.method is 'POST':
        boton = request.form['boton']
        if boton is 'Media':
            mediaCLics, mediaMeneos, nNoticias = CalculaMedia(Mongo=usedDB)
            usedDB = not usedDB
            return render_template('index.html', media=mediaT)
        elif boton is 'Umbral':
            valorUmbral = request.form['UmbralText']
            umbral_superior(valorUmbral)
            umbral_inferior(valorUmbral)
            return render_template('index.html', umbrInf=menorMostrar, umbrSup=mayorMostrar)
        elif boton is 'Grafica':
            return redirect(url_grafica)

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
    CalculaMedia(Mongo=True)
    CalculaMedia(Mongo=False)

    # app.debug = True
    # app.run(host='0.0.0.0')
