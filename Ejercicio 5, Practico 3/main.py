from zope.interface import Interface

class Elemento(Interface):
    def insertarElemento(posicion,elemento):
        pass
    def agregarElemento(elemento):
        pass
    def mostrarElemento(posicion):
        pass