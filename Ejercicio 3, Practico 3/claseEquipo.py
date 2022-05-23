from claseContrato import Contrato

class Equipo:
    def __init__(self,nombre,ciudad):
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__contrato = []

    def __str__(self):
        return '\nNombre: %s  Ciudad: %s' % (self.__nombre,self.__ciudad)

    def getNombre(self):
        return self.__nombre
    def getCiudad(self):
        return self.__ciudad

    def agregarContrato(self,contrato):
        if(type(contrato) == Contrato):
            self.__contrato.append(contrato)
            print('\nSe agrego exitosamente contrato en equipo.')
        else:
            print('\nNo se agrego contrato en equipo.')