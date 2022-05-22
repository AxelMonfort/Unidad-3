from claseFlores import Flor

class Ramo:
    def __init__(self,tamanio):
        self.__tamanio = tamanio
        self.__flor = []

    def __str__(self):
        s = ''
        for Flor in self.__flor:
            s += 'Tamaño: %s ' % (self.__tamanio) + str(Flor) + '\n'
        return s

    def getTamanio(self):
        return self.__tamanio

    def agregar(self,objeto):
        if (type(objeto) == Flor):
            self.__flor.append(objeto)
            print('\nCarga exitosa en claseRamo.')
        else:
            print('\nNo se pudo cargar.')