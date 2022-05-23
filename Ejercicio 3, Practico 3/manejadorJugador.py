import csv
from claseJugador import Jugador

class maneJugador:
    def __init__(self):
        self.__jugador = []

    def __str__(self):
        s = ''
        for Jugador in self.__jugador:
            s += str(Jugador) + '\n'
        return s

    def agregar(self,objeto):
        if (type(objeto) == Jugador):
            self.__jugador.append(objeto)
            print('\nSe agrego correctamente.')
        else:
            print('\nError, no se pudo agregar.')