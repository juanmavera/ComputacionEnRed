from flask import Flask, render_template, request, redirect
from DataObtainer import *
from MongoHandler import *
from BeebotteHandler import *

import threading
import time
import numpy as np

app = Flask(__name__)

usedDB = True
uri_grafica = 'https://beebotte.com/dash/1d32c290-d561-11e8-b923-173fcb1c50d5?shareid=shareid_4xcsYsSRzoGqMlN6'


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


def NoticiasUmbral(umbral, Mongo=True):
    if Mongo:
        mongoDB = MongoHandler()
        Noticias = mongoDB.LeerNoticias()

    else:
        bbtDB = BeebotteHandler()
        Noticias = bbtDB.LeerNoticias()

    # mediaClics = np.mean(Noticias[0])
    # mediaMeneos = np.mean(Noticias[1])

    umbralNoticias = []
    # print('\nNoticias\n--------\n')
    for noticia in Noticias[2]:
        if noticia[0] > umbral:
            umbralNoticias.append(noticia)
            print(noticia[2])

    # print('\n\nEstadisticas\n------------\n')
    # print('Numero medio de clics obtenidos: %.2f\n'
    #       'Numero medio de meneos obtenidos: %.2f\n'
    #       'Numero de noticias: %d\n'
    #       % (mediaClics, mediaMeneos, len(Noticias[2])))

    return umbralNoticias


@app.route('/', methods=['GET','POST'])
def index():
    global usedDB
    global uri_grafica

    if request.method is 'POST':
        boton = request.form['boton']
        if boton is 'Media':
            mediaClics, mediaMeneos, nNoticias = CalculaMedia(Mongo=usedDB)

            if usedDB:
                BD = 'Mongo DB'
            else:
                BD = 'BeeBotte DB'

            usedDB = not usedDB
            cadena = []
            cadena = "Media de Clicks: %.2f || Media Meneos: %.2f || Noticias analizadas: %d || Base de datos utilizada: %s" % (mediaClics, mediaMeneos, nNoticias, BD)

            return render_template('index.html', summaryNews=cadena)

        elif boton is 'Umbral':
            valorUmbral = request.form['UmbralText']
            cadena = []
            Noticias = NoticiasUmbral(umbral=valorUmbral, Mongo=True)

            for noticia in Noticias:
                cadena.append("Clicks: %d || Meneos: %d || Noticia: %s || Fecha: %s || Hora: %s" % (int(float(noticia[0])), int(float(noticia[1])), str(noticia[2]), str(noticia[3]), str(noticia[4])))

            if len(cadena) < 10:
                return render_template('index.html', noticias=cadena)
            else:
                return render_template('index.html', noticias=cadena[-10:-1])

        elif boton is 'Grafica':
            return redirect(uri_grafica)

    else:
        mongoDB = MongoHandler()
        Noticias = mongoDB.LeerNoticias()

        cadena = []
        for noticia in Noticias:
            cadena.append("Clicks: %d || Meneos: %d || Noticia: %s || Fecha: %s || Hora: %s" % (int(float(noticia[0])), int(float(noticia[1])), str(noticia[2]), str(noticia[3]), str(noticia[4])))

        return render_template('index.html', noticias=cadena[-10:-1])

    # Data = DataObtainer()
    # page = Data.get_web()
    # Noticia = Data.get_web_data(page)
    #
    # cadena = "Clicks: %d || Meneos: %d || Noticia: %s || Fecha: %s || Hora: %s" % (int(float(Noticia[0])), int(float(Noticia[1])), str(Noticia[2]), str(Noticia[3]), str(Noticia[4]))
    # return '<p> %s </p>' %(cadena)


@app.route('/loc')
def location():
    return'<p> UAH </p>'


if __name__ == '__main__':

    InitPeriodicDataObtainer()
    # CalculaMedia(Mongo=True)
    # CalculaMedia(Mongo=False)

    app.debug = True
    app.run(host='0.0.0.0')
