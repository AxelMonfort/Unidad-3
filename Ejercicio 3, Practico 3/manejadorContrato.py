import numpy as np
from datetime import date
from claseContrato import Contrato

class maneContrato:
    __cantidad = 0
    __dimension = 0
    __incremento = 11

    def __init__(self, dimension=1, incremento=11):
        self.__contratos = np.empty(dimension, dtype=Contrato)
        self.__cantidad = 0
        self.__dimension = dimension

    def agregar(self, objeto):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__contratos.resize(self.__dimension)
        self.__contratos[self.__cantidad] = objeto
        self.__cantidad += 1

    def __str__(self):
        s = ''
        for Contrato in self.__contratos:
            s += str(Contrato) + '\n'
        return s

    def agregarContrato(self, objeto):
        if(type(objeto) == Contrato):
            self.__contratos[self.__cantidad] = objeto
            self.__cantidad += 1
            print('\nSe agrego contrato en manejadorContrato.')
        else:
            print('\n No se pudo agregar el contrato.')

    def buscaJugador(self,dni):
        i = 0
        band,info = False,False
        while (i < len(self.__contratos) and (band == False)):
            info = self.__contratos[i].busca(dni)
            if(info != False):
                band = True
            else:
                i += 1
        return info,self.__contratos[i].getFin()

    def acumula(self,nombre):
        acum,band = 0,0
        for Contrato in self.__contratos:
            band = Contrato.acumular(nombre)
            if(band == 1):
                acum += Contrato.getSueldo()
        return acum

    def vencimiento(self):
        for Contrato in self.__contratos:
            i,i1,i2 = Contrato.getInicio().split('.')
            fin,fin1,fin2 = Contrato.getFin().split('.')
            if i1 < fin1:
                c = i1-fin1
                if c < 6:
                    print('\nEquipo: %s'+str(Contrato.getEquipo()))
                    print(Contrato.getDatoJugador())
                else:
                    print('\nNo tiene contratos de jugadores proximos a vencerse en 6 meses.')


    def generarArchivo(self):
        archi = open('jugador','w')
        archi.write('DNI;Nombre equipo;Inicio;Fin;Pago mensual')
        archi.write('\n')
        for Contrato in self.__contratos:
            dni = str(Contrato.getJugador())
            nombre = str(Contrato.getEquipo())
            inicio = str(Contrato.getInicio())
            fin = str(Contrato.getFin())
            pago = str(Contrato.getSueldo())
            archi.write(dni + ';')
            archi.write(nombre + ';')
            archi.write(inicio + ';')
            archi.write(fin + ';')
            archi.write(pago + ';')
            archi.write('\n')
        print('\nArchivo creado exitosamente.')
        archi.close()
