from os import system
from manejadorFacultad import manejador as mane

def menu():
    opcion = 0
    salir = False
    while not salir:
        print('\n----------------MENU DE OPCIONES-------------')
        print('\n1- Mostrar nombre de facultad, nombre y duracion de todas las carreras.')
        print('\n2- Dada una carrera, mostrar informacion de la facultad.')
        print('\n3 Eliminar las carreras.')
        print('\n4- Salir')
        opcion = int(input('\nIngrese opcion: '))

        if(opcion == 1):
            nro = input('\nIngrese numero de facultad: ')
            objeto.mostrar(nro)
            system('pause')

        if(opcion == 2):
            nombre = input('\nIngrese nombre de carrera: ')
            objeto.mostrarNombre(nombre)

        if(opcion == 3):
            objeto.borrar()

        if(opcion == 4):
            salir = True



if __name__ == '__main__':
    objeto = mane()
    objeto.testManejador()
    menu()