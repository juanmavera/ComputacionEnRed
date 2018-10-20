import numpy as np
import re

from flask import Flask
from urllib import urlopen

class webHandler():
    def __init__(self):
        self.web = 'https://www.meneame.net/'

    def get_web(self):
        page = urlopen(self.web).read()
        # print(page)
        return page

    def get_data(self, page):

        # Obteninendo Clics
        patronClics = re.compile('<div class="clics">(.*?)</div>')
        listaClics = patronClics.findall(page)
        listaClics = listaClics[5:]
        Clics = np.zeros(np.array(listaClics).shape[0])

        print('Clics obtenidos')

        for index, lista in enumerate(listaClics):
            aux = str(lista).split(' ')
            Clics[index] = int(aux[2])
            print(index, Clics[index])

        # Obteniendo Meneos
        patronMeneos = re.compile('<div class="votes"> <a (.*?)>(.*?)</a> meneos </div>')
        listaMeneos = patronMeneos.findall(page)
        Meneos = np.zeros(np.array(listaMeneos).shape[0])

        print('Meneos Obtenidos')

        for index, lista in enumerate(listaMeneos):
            Meneos[index] = int(lista[1])
            print(index, Meneos[index])

        # Obteniendo Titulos
        patronNews = re.compile('<h2> <a href=(.*?) > (.*?) </a>(.*?)</h2>')
        listaNews = patronNews.findall(page)
        News = np.array(listaNews)[:, 1]

        print('Titulos Obtenidos')

        for index, lista in enumerate(listaNews):
            print(index, str(News[index]))


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Aplicacion </h1>'


@app.route('/loc')
def location():
    return'<p> UAH </p>'


if __name__ == '__main__':

    WWW = webHandler()
    page = WWW.get_web()
    WWW.get_data(page)

    # app.debug = True
    # app.run(host='0.0.0.0')
