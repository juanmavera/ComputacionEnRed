import numpy as np
import re

from urllib import urlopen


class DataObtainer():
    def __init__(self):
        self.web = 'https://www.meneame.net/'

    def get_web(self):
        page = urlopen(self.web).read()
        # print(page)
        return page

    def get_clics(self, page):

        patronClics = re.compile('<div class="clics">(.*?)</div>')
        listaClics = patronClics.findall(page)
        listaClics = listaClics[5:]
        Clics = np.zeros(np.array(listaClics).shape[0])

        # print('\nClics obtenidos\n---------------\n')

        for index, lista in enumerate(listaClics):
            aux = str(lista).split(' ')
            Clics[index] = int(aux[2])
            # print(Clics[index])

        return Clics

    def get_meneos(self, page):

        patronMeneos = re.compile('<div class="votes"> <a (.*?)>(.*?)</a> meneos </div>')
        listaMeneos = patronMeneos.findall(page)
        Meneos = np.zeros(np.array(listaMeneos).shape[0])

        # print('\nMeneos Obtenidos\n----------------\n')

        for index, lista in enumerate(listaMeneos):
            Meneos[index] = int(lista[1])
            # print(Meneos[index])

        return Meneos

    def get_news(self, page):
        patronNews = re.compile('<h2> <a href=(.*?) > (.*?) </a>(.*?)</h2>')
        listaNews = patronNews.findall(page)
        News = np.array(listaNews)[:, 1]

        # print('\nTitulos Obtenidos\n-----------------\n')
        #
        # for index, lista in enumerate(listaNews):
        #     print(str(News[index]))

        return News

    def get_web_data(self, page):

        # Obteninendo Clics
        Clicks = self.get_clics(page)

        # Obteniendo Meneos
        Meneos = self.get_meneos(page)

        # Obteniendo Titulos
        News = self.get_news(page)

        Datos = zip(list(Clicks), list(Meneos), list(News))
        Datos = np.array(Datos)

        # for _, data in enumerate(Datos):
        #     print(data)

        Noticia = Datos[0, :]           # Solo se almacena la primera noticia encontrada

        return Noticia