class Nodo:
    __personal = None
    __siguiente = None

    def __init__(self,personal):
        self.__personal = personal
        self.__siguiente = None

    def getSiguiente(self):
        return self.__siguiente

    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente

    def getDato(self):
        return self.__personal

    def getNombreClase(self):
        return self.__personal.__class__.__name__