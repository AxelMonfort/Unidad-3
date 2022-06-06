from zope.interface import implementer
from claseTelevisor import Televisor
from claseHeladera import Heladera
from claseLavarropa import Lavarropa

from claseNodo import Nodo
from Interfaz import Elemento


@implementer(Elemento)
class Lista:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            dato = self.__actual.getDato()
            self.__indice += 1
            self.__actual = self.__actual.getSiguiente()
            return dato

    def agregarAparato(self, aparato):
        try:
            if type(aparato) == Televisor or type(aparato) == Heladera or type(aparato) == Lavarropa:
                nodo = Nodo(aparato)
                if self.__comienzo == None:
                    nodo.setSiguiente(self.__comienzo)
                    self.__comienzo = nodo
                    self.__actual = nodo
                    self.__tope += 1
                else:
                    aux = self.__comienzo
                    while aux.getSiguiente() != None:
                        aux = aux.getSiguiente()
                    nodo.setSiguiente(aux.getSiguiente())
                    aux.setSiguiente(nodo)
                    self.__tope += 1
                print("*** APARATO AGREGADO CON EXITO ***")
            else:
                raise TypeError()
        except TypeError:
            print('No es un aparato')


    def insertarElemento(self, posicion, aparato):  # INCISO 1
        if posicion <= self.__tope:
            nodo = Nodo(aparato)
            if posicion == 0:
                nodo.setSiguiente(self.__comienzo)
                self.__comienzo = nodo
                self.__tope += 1
            else:
                num = 1
                aux = self.__comienzo
                while num < posicion:
                    aux = aux.getSiguiente()
                    num += 1
                nodo.setSiguiente(aux.getSiguiente())
                aux.setSiguiente(nodo)
                self.__tope += 1
            print('\nAparato cargado exitosamente.')

    def agregar(self, aparato):  # INCISO 2
        nodo = Nodo(aparato)
        if self.__comienzo == None:
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nodo
            self.__actual = nodo
            self.__tope += 1
        else:
            aux = self.__comienzo
            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            nodo.setSiguiente(aux.getSiguiente())
            aux.setSiguiente(nodo)
            self.__tope += 1
        print('\nAparato agregado con exito.')

    def buscaXPosicion(self,posicion):                  #INCISO 3
        if posicion == 0:
            print('\nEl objeto es del tipo {}'.format(self.__comienzo.getNombreClase()))
        else:
            aux = self.__comienzo.getSiguiente()
            band,nro = False,1
            while (aux != None) and (band == False):
                if nro == posicion:
                    band = True
                else:
                    aux = aux.getSiguiente()
                    nro += 1
            if band == True:
                print('\nEl objeto es del tipo {}'.format(aux.getNombreClase()))


    def buscaMarca(self,marca):                 #INCISO 4
        aux = self.__comienzo
        while aux != None:
            if aux.getDato().getMarca() == marca:
                print('\nEste aparato '+str(aux.getNombreClase()+'  tiene marca '+str(aux.getDato().getMarca())))
            aux = aux.getSiguiente()

    def buscaCarga(self,carga):             #INCISO 5
        aux = self.__comienzo
        while aux != None:
            if aux.getNombreClase() == 'Lavarropa':
                if aux.getDato().getTipo() == carga:
                    print('\nHay un lavarropas con carga '+str(aux.getDato().getTipo()))
            aux = aux.getSiguiente()

    def importe(self):                  #INCISO 6
        aux = self.__comienzo
        while aux != None:
            print('\nMARCA: '+str(aux.getDato().getMarca()))
            print('\nPAIS: '+str(aux.getDato().getPais()))
            print('\nIMPORTE: ',aux.getDato().calculo())
            aux = aux.getSiguiente()

    def toJson(self):
        aparatos = []
        for v in self:
            aparatos.append(v.toJson())
        dic = dict(__class__=self.__class__.__name__, datos=aparatos)
        return dic

    def mostrar(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()