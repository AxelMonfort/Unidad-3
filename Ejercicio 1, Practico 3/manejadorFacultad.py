import csv
from claseCarrera import Carrera as carrera
from claseFacultad import Facultad as facu

class manejador:
    def __init__(self):
        self.__lista = []

    def __str__(self):
        s = ''
        for facu in self.__lista:
            s += str(facu) + '\n'
        return s

    def agregar(self, facultad):
        self.__lista.append(facultad)

    def testManejador(self):
        archi = open('facultad')
        reader = csv.reader(archi, delimiter=',')
        linea = -1
        for i in reader:
            if(len(i) == 5):
                facultad = facu(i[0],i[1],i[2],i[3],i[4])
                self.agregar(facultad)
                linea +=1
            elif(len(i) == 4):
                objeto = carrera(i[0],i[1],i[2],i[3])
                self.__lista[linea].agregaCarrera(objeto)
        archi.close()

    def mostrar(self,nro):
        for facu in self.__lista:
            if(nro == facu.getCodigo()):
                print('\n Nombre de facultad: {}.'.format(facu.getNombre()))
                facu.mostrar()

    def mostrarNombre(self,nombre):
        for facu in self.__lista:
            cod = facu.buscarCarrera(nombre)
            if(cod == facu.getCodigo()):
                print(facu)

    def borrar(self):
        for facu in self.__lista:
            facu.borrar()