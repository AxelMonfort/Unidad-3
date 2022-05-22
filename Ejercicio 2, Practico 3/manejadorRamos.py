from claseRamo import Ramo as ramo
from claseFlores import Flor
from manejadorFlores import maneFlor

class maneRamo:
    def __init__(self):
        self.__ramos = []

    def __str__(self):
        s = ''
        for ramo in self.__ramos:
            s += str(ramo) + '\n'
        return s

    def agregarFlor(self,objeto):
        if (type(objeto) == ramo):
            self.__ramos.append(objeto)
            print('\nCarga exitosa en manejadorRamo')
        else:
            print('\nNo se pudo cargar la flor en el ramo.')

    def buscar(self,tipo):
        for ramo in self.__ramos:
            if(ramo.getTamanio() == tipo):
                print(ramo)