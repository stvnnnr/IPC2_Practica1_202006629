from glob import glob
import sys
from listaPizzas import listaPizzas
from Pizza import pizzaPepperoni
from Pizza import pizzaSalchicha
from Pizza import pizzaCarne
from Pizza import pizzaQueso
from Pizza import pizzaPiña
from listaPersonas import listaPersonas
from Persona import Persona
global listaPeople

def menuPrincipal():#esqueleto menu principal
    print("                                                                ")
    print("-------------Bienvenido a Pizzeria The blue  cheese-------------")
    print("|                                                              |")
    print("|************************MENU PRINCIPAL************************|")
    print("|                                                              |")
    print("|  1. Ordenes.                                                 |")
    print("|  2. Datos del desarrollador                                  |")
    print("|  0. Salir.                                                   |")
    print("----------------------------------------------------------------")

def menuOrdenes():#esqueleto menu ordenes
    print("                                                                ")
    print("-------------Bienvenido a Pizzeria The blue  cheese-------------")
    print("|                                                              |")
    print("|***********************MENU DE ORDENES************************|")
    print("|                                                              |")
    print("|  1. Ver Ordenes.                                             |")
    print("|  2. Despachar Orden                                          |")
    print("|  3. Agregar Orden                                            |")
    print("|  4. Eliminar Orden.                                          |")
    print("|  0. Regresar.                                                |")
    print("----------------------------------------------------------------")

def mostrarMisDatos():#moestro mis datos
    global listaPeople
    listaPeople = listaPersonas()
    listaPeople.recorrerSinDetalles()
    print("Wilber Steven Zúñiga Ruano")
    print("202006629")
    print("Introducción a la programación y computación 2 sección \"C\"")
    print("Ingeniería en Ciencias y Sistemas")
    print("1er Semestre 2022")

def mantenerMenuOrdenes():#metodo para entrar y mantener menu de ordenes
    while (True):
        # try:
            menuOrdenes()
            select = int(input("Selecciona alguna opción:"))
            print("\n")
            if select == 1:
                print("JAJAJAJA")
            elif select == 2:
                print("JAJAJAJA")
            elif select == 3:
                print("JAJAJAJA")
            elif select == 4:
                print("JAJAJAJA")
            elif select == 0:
                print("volviendo...")
                break
            else:
                print("No existe esa opción")
        # except:
        #     print("ocurrio un error, vuelve a intentarlo")
        #     print("El error fue:", sys.exc_info()[0])


while True:#Este while me ayuda a mantener activo el menu principal siempre
    # try:
        menuPrincipal()
        select = int(input("Selecciona alguna opción:"))
        print("\n")
        if select == 1:
            mantenerMenuOrdenes()
        elif select == 2:
            print("Datos del programador:")
            mostrarMisDatos()
            # a = pizzaSalchicha()
            # b = pizzaQueso()
            # c = pizzaCarne()
            # listaa = listaPizzas()
            # listaPe = listaPersonas()
            # listaa.insertarPizza(a)
            # listaa.insertarPizza(b)
            # listaa.insertarPizza(c)
            # timeee = listaa.tiempoEspera()
            # p1 = Persona("Josesito", "49981171",timeee)
            # p1.setLista(listaa)
            # listaPe.insertarPersona(p1)

            # d = pizzaSalchicha()
            # e = pizzaQueso()
            # f = pizzaCarne()
            # listae = listaPizzas()
            # listae.insertarPizza(d)
            # listae.insertarPizza(e)
            # listae.insertarPizza(f)
            # timeea = listae.tiempoEspera()
            # p2 = Persona("Juanito", "49981171",timeea)
            # p2.setLista(listae)
            # listaPe.insertarPersona(p2)
            # listaPe.recorrerSinDetalles()
            # listaPe.recorrerConDetalles()
        elif select == 0:
            print("------          Gracias por usar mi programa :3           ------")
            print("----------------------------------------------------------------")
            break
        else:
            print("No existe esa opción")
    # except:
    #     print("ocurrio un error, vuelve a intentarlo")
    #     print("El error fue:", sys.exc_info()[0])