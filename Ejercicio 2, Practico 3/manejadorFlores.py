from audioop import reverse

import numpy as np
import csv
from claseFlores import Flor

class maneFlor:
    __cantidad = 0
    __dimension = 0
    __incremento = 11

    def __init__(self,dimension,incremento=11):
        self.__flor = np.empty(dimension, dtype=Flor)
        self.__cantidad = 0
        self.__dimension = dimension

    def __str__(self):
        s = ''
        for Flor in self.__flor:
            s += str(Flor) + '\n'
        return s

    def agregar(self, objeto):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__flor.resize(self.__dimension)
        self.__flor[self.__cantidad] = objeto
        self.__cantidad += 1

    def testManejador(self):
        archi = open('flores')
        reader = csv.reader(archi,delimiter = ';')
        for i in reader:
            flor = Flor(i[0],i[1],i[2],i[3])
            self.agregar(flor)
        archi.close()

    def buscar(self,flor):
        i = 0
        band = False
        while not band:
            if self.__flor[i].getNom() == flor and i<len(self.__flor):
                self.__flor[i].contar()
                band = True
            i +=1
        i -= 1
        if i<len(self.__flor):
            rta = self.__flor[i]
        else:
            rta = None
        return rta,i

    def mostrar(self):
        i = 0
        self.__flor.sort(axis=0)
        while i < 5:
            print(self.__flor[i])
            i +=1