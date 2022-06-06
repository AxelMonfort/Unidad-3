from zope.interface import Interface

class Elemento(Interface):
    def insertarElemento(posicion,elemento):
        print('ENTRO A LA INTERFAZ------------------------------------')
        pass
    def agregarElemento(elemento):
        pass
    def mostrarElemento(posicion):
        pass