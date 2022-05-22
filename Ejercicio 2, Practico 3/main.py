from manejadorFlores import maneFlor
from manejadorRamos import maneRamo
from claseRamo import Ramo

def menu(obF,obR):
    opcion = 0
    salir = False
    while not salir:
        print('\n=============MENU DE OPCIONES==================')
        print('\n1- Registrar un ramo vendido (instancia de la clase ramo), solicitando las flores que lo que se pondrán en el ramo.')
        print('\n2- Mostrar el nombre de las 5 flores  más pedidas en un ramo, considerando todos los ramos vendidos.')
        print('\n3- Ingresar por teclado un tipo de ramo y mostrar las flores vendidas en ese tamaño considerando todos los ramos vendidos.')
        print('\n4- Salir.')
        opcion = int(input('\nIngrese opcion: '))

        if(opcion == 1):
            tamanio = input('\nIngrese tamanio de ramo(c,m,g): ')
            ramo = Ramo(tamanio)
            cont = 1
            print('\n-----------ELIJA FLORES (Maximo 4)-----------')
            print(obF)
            flor = input('\n......(f salir): ')
            while cont < 4 and flor != 'f':
                busca = obF.buscar(flor)
                while busca[0] == None:
                      flor = input('\nError, no se encuentra esa flor. Ingrese nuevamente: ')
                      busca = obF.buscar(flor)
                ramo.agregar(busca[0])
                cont +=1
                obR.agregarFlor(ramo)
                flor = input('\n......(f salir): ')

        if(opcion == 2):
            obF.mostrar()

        if(opcion == 3):
            tipo = input('\nIngrese tipo de ramo (c,m,g): ')
            obR.buscar(tipo)

        if(opcion == 4):
                salir=True


if __name__ == '__main__':
    objetoFlor = maneFlor(8)
    objetoRamo = maneRamo()
    objetoFlor.testManejador()
    menu(objetoFlor,objetoRamo)