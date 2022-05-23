class Contrato:

    def __init__(self,inicio,fin,pago,jugador,equipo):
        self.__inicio = inicio
        self.__fin = fin
        self.__pago = int(pago)
        self.__jugador = jugador
        self.__equipo = equipo

    def __str__(self):
        cadena = str(self.__equipo)
        cadena += str(self.__jugador)
        cadena += '\nFecha Inicio: ' + str(self.__inicio) + '\n'
        cadena +='Fecha Fin:    ' + str(self.__fin)    + '\n'
        cadena +='Pago Mensual: ' + str(self.__pago)   + '\n'
        return cadena

    def getInicio(self):
        return self.__inicio
    def getFin(self):
        return self.__fin
    def getSueldo(self):
        return self.__pago

    def busca(self,dni):
        if (self.__jugador.getDNI() == dni):
            return self.__equipo.getNombre()
        else:
            return False

    def acumular(self,nombre):
        if (self.__equipo.getNombre() == nombre):
            return 1
        else:
            return 0

    def getEquipo(self):
        return '%s' % (self.__equipo.getNombre())
    def getJugador(self):
        return '%s' % (self.__jugador.getDNI())
    def getDatoJugador(self):
        return 'Nombre: %s DNI: %s Ciudad: %s' % (self.__jugador.getNombre(),self.__jugador.getDNI,self.__jugador.getCiudad())