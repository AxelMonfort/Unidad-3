import numpy as np
import csv

from claseEquipo import Equipo

class maneEquipo:
    __cantidad = 0

    def __init__(self, cant=1):
        self.__equipos = np.empty(cant, dtype=Equipo)

    def __str__(self):
        s = ''
        for Equipo in self.__equipos:
            s += str(Equipo) + '\n'
        return s

    def agregar(self, objeto):
        self.__equipos[self.__cantidad] = objeto
        self.__cantidad +=1

    def testManejador(self):
        archi = open('Equipos')
        reader = csv.reader(archi,delimiter = ';')
        for i in reader:
            if (len(i) == 1):
                cant = int(i[0])
                self.__equipos.resize(cant,refcheck=False)
            else:
                objeto = Equipo(i[0],i[1])
                self.agregar(objeto)
        archi.close()

    def busca(self,nombre):
        i = 0
        band = False
        while(i < len(self.__equipos) and (band == False)):
            if(nombre == self.__equipos[i].getNombre()):
                band = True
            else:
                i += 1
        if(band == True):
            return self.__equipos[i]
        else:
            return 0

    def agregarContrato(self,contrato,j):
        i = 0
        band = False
        while (i < len(self.__equipos) and (band == False)):
            if(j.getNombre() == self.__equipos[i].getNombre()):
                band = True
            else:
                i += 1
        if (band == True):
            self.__equipos[i].agregarContrato(contrato)
