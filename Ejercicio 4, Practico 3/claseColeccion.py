from claseCalefactor import Calefactor
from claseElectrico import Electrico
from claseNatural import Natural
import csv
import numpy as np

class Coleccion:
    def __init__(self,tamaño):
        self.__coleccion = np.empty(tamaño,dtype=Calefactor)
        self.__indice = 0

    def __str__(self):
        s = ''
        for Electrico in self.__coleccion:
            s += str(Electrico) + '\n'
        return s

    def agregar(self):
        archi = open('calefactor-electrico')
        reader = csv.reader(archi,delimiter = ',')
        next(reader)
        for i in reader:
            objeto = Electrico(i[0],i[1],int(i[2]))
            self.__coleccion[self.__indice] = objeto
            self.__indice += 1
        archi.close()

        archi = open('calefactor-a-gas')
        reader = csv.reader(archi,delimiter = ',')
        next(reader)
        for i in reader:
            objeto = Natural(i[0],i[1],i[2],int(i[3]))
            self.__coleccion[self.__indice] = objeto
            self.__indice += 1
        archi.close()

    def buscar(self):
        min = 9999
        datos = ''
        i = 0
        while (i < len(self.__coleccion)):
            if type(self.__coleccion[i]) == Natural:
                if self.__coleccion[i].getCalorias() < min:
                    min = self.__coleccion[i].getCalorias()
                    datos = self.__coleccion[i].getMarca(),self.__coleccion[i].getModelo()
            i += 1
        return datos

    def buscar2(self):
        min = 9999
        info = ''
        i = 0
        while (i < len(self.__coleccion)):
            if type(self.__coleccion[i]) == Electrico:
               if self.__coleccion[i].getPotencia() < min:
                   min1 = self.__coleccion[i].getPotencia()
                   info = self.__coleccion[i].getMarca(), self.__coleccion[i].getModelo()
            i += 1
        return info