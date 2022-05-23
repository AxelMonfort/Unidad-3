from manejadorEquipo import maneEquipo
from manejadorJugador import maneJugador
from manejadorContrato import maneContrato
from claseJugador import Jugador
from claseContrato import Contrato
from datetime import date

def menu(equipo,jugador,contra):
    opcion = 0
    salir = False
    while not salir:
        print('\n=================MENU DE OPCIONES=================')
        print('\n1- Crear un contrato para un jugador en un equipo: Se genera un contrato para un jugador en un equipo.')
        print('\n2- Consultar jugadores Contratados: Ingresar el DNI de un jugador, si está contratado, mostrar el nombre del Equipo en el que fue contratado, y la fecha de finalización de contrato.')
        print('\n3- Consultar Contratos: Ingresar el identificador de un Equipo y listar los datos de los Jugadores cuyo contrato vence en 6 meses.')
        print('\n4- Obtener importe de contratos: Para un nombre de equipo leído desde teclado, determinar el importe total de los contratos que posee con los jugadores del equipo.')
        print('\n5- Guardar Contratos: Generar un nuevo archivo que contenga los siguientes datos de los contratos: DNI del jugador, Nombre del equipo, fecha de inicio, fecha de fin, y el pago mensual.')
        print('\n6- Salir.')
        opcion = int(input('\nIngrese opcion: '))

        if opcion == 1:
            nom = input('\nIngrese nombre del jugador: ')
            DNI = input('\nDNI: ')
            ciudad = input('\nCiudad Natal: ')
            pais = input('\nPais: ')
            fecha = input('\nFecha Nacimiento: ')
            juga = Jugador(nom,DNI,ciudad,pais,fecha)
            jugador.agregar(juga)                         #Agrego jugador

            equi = input('\nIngrese en que equipo juega: ')
            j = equipo.busca(equi)
            while j == 0:
                equi = input('\nError, ingrese nuevamente equipo: ')
                j = equipo.busca(equi)                   #Busco equipo

            inicio = input('\nIngrese fecha de inicio(EJ: 2022.3.4): ')
            fin = input('\nIngrese fecha de finalizacion(EJ: 2022.1.2): ')
            pago= input('\nIngrese pago: ')

            contrato = Contrato(inicio,fin,pago,juga,j)
            contra.agregarContrato(contrato)                   #Agrego contrato en manejadorContrato
            equipo.agregarContrato(contrato,j)         #Agrego contrato en equipo

        if opcion == 2:
            dni = input('\nIngrese dni a buscar: ')
            condicion = contra.buscaJugador(dni)     #Busco jugador en los contratos
            if condicion[0] != False:
                print('Equipo: '+str(condicion[0]))
                print('Fecha de finzalizacion: '+str(condicion[1]))
            else:
                print('\nNo se encuentra ese jugador con ese dni.')

        if opcion == 3:
            nombre = input('\nIngrese nombre de equipo: ')
            j = equipo.busca(nombre)
            while j == 0:
                nombre = input('\nError, ingrese nuevamente equipo: ')
                j = equipo.busca(nombre)
            contra.vencimiento()

        if opcion == 4:
            nombre = input('\nIngrese nombre de equipo: ')
            j = equipo.busca(nombre)
            while j == 0:
                nombre = input('\nError, ingrese nuevamente equipo: ')
                j = equipo.busca(nombre)
            l = contra.acumula(nombre)
            print('\nEQUIPO: ',nombre, 'Importe Total: $',l)

        if opcion == 5:
            contra.generarArchivo()

        if opcion == 6:
            salir = True


if __name__ == '__main__':
    objeto = maneEquipo()
    objeto1 = maneJugador()
    objeto2 = maneContrato()
    objeto.testManejador()
    menu(objeto,objeto1,objeto2)