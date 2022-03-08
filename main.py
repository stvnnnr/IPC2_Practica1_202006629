import sys
from listaPizzas import listaPizzas
from Pizza import Pizza, pizzaPepperoni
from Pizza import pizzaSalchicha
from Pizza import pizzaCarne
from Pizza import pizzaQueso
from Pizza import pizzaPiña
from listaPersonas import listaPersonas
from Persona import Persona
global listaPeople
listaPeople = listaPersonas()
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

def menuPizzas():
    print("                                                                ")
    print("-------------Bienvenido a Pizzeria The blue  cheese-------------")
    print("|                                                              |")
    print("|***********************MENU DE PIZZAS*************************|")
    print("|                                                              |")
    print("|  1. Pizza Peperoni.                                          |")
    print("|  2. Pizza Carne.                                             |")
    print("|  3. Pizza Salchicha.                                         |")
    print("|  4. Pizza Queso.                                             |")
    print("|  5. Pizza Piña.                                              |")
    print("----------------------------------------------------------------")

def recorrerMenu():
    print("                                                                ")
    print("-------------Bienvenido a Pizzeria The blue  cheese-------------")
    print("|                                                              |")
    print("|  1. Ver con detalles.                                        |")
    print("|  2. Ver sin detalles.                                        |")
    print("|  0. Regresar.                                                |")
    print("----------------------------------------------------------------")

def agregarOrden():
    global listaPeople
    nameOrden = (input("Nombre  para su orden:"))
    numeroTel= int(input("Número de teléfono:"))
    noPizzas = int(input("¿Cuantas Pizzas desea?"))
    listaPi = listaPizzas()
    for i in range(noPizzas):
        print("seleccione su pizza no:"+str((i+1)))
        while (True):
            try:
                menuPizzas()
                select = int(input("Seleccione su pizza:"))
                print("\n")
                if select == 1:
                    p1 = pizzaPepperoni()
                    listaPi.insertarPizza(p1)
                    break
                elif select == 2:
                    p2 = pizzaCarne()
                    listaPi.insertarPizza(p2)
                    break
                elif select == 3:
                    p3 = pizzaSalchicha()
                    listaPi.insertarPizza(p3)
                    break
                elif select == 4:
                    p4 = pizzaQueso()
                    listaPi.insertarPizza(p4)
                    break
                elif select == 5:
                    p5 = pizzaPiña()
                    listaPi.insertarPizza(p5)
                    break
                else:
                    print("No existe esa opción")
            except:
                print("ocurrio un error, vuelve a intentarlo")
                print("El error fue:", sys.exc_info()[0])
    timee = listaPi.tiempoEspera()
    peopleUno = Persona(nameOrden,numeroTel,timee)
    peopleUno.setLista(listaPi)
    listaPeople.insertarPersona(peopleUno)
    print("\n")
    print("\n")
    print("Orden tomada, espere su pedido")
    print("\n")
    #aca iria lo de graphviz


def mostrarMisDatos():#muestro mis datos
    print("Wilber Steven Zúñiga Ruano")
    print("202006629")
    print("Introducción a la programación y computación 2 sección \"C\"")
    print("Ingeniería en Ciencias y Sistemas")
    print("1er Semestre 2022")

def mantenerMenuOrdenes():#metodo para entrar y mantener menu de ordenes
    global listaPeople
    while (True):
        try:
            menuOrdenes()
            select = int(input("Selecciona alguna opción:"))
            print("\n")
            if select == 1:
                mantenerMenuRecorrer()
            elif select == 2:
                listaPeople.eliminarPrimero()
                #graphviz
            elif select == 3:
                agregarOrden()
            elif select == 4:
                listaPeople.mantenerMenuEliminar()
            elif select == 0:
                print("volviendo...")
                break
            else:
                print("No existe esa opción")
        except:
            print("ocurrio un error, vuelve a intentarlo")
            print("El error fue:", sys.exc_info()[0])

def mantenerMenuRecorrer():#metodo para entrar y mantener menu de ordenes
    while (True):
        try:
            global listaPeople
            recorrerMenu()
            select = int(input("Selecciona alguna opción:"))
            print("\n")
            if select == 1:
                listaPeople.recorrerConDetalles()
                break
            elif select == 2:
                listaPeople.recorrerSinDetalles()
                break
            elif select == 0:
                print("volviendo...")
                break
            else:
                print("No existe esa opción")
        except:
            print("ocurrio un error, vuelve a intentarlo")
            print("El error fue:", sys.exc_info()[0])

while True:#Este while me ayuda a mantener activo el menu principal siempre
    try:
        menuPrincipal()
        select = int(input("Selecciona alguna opción:"))
        print("\n")
        if select == 1:
            mantenerMenuOrdenes()
        elif select == 2:
            print("Datos del programador:")
            mostrarMisDatos()
        elif select == 0:
            print("------          Gracias por usar mi programa :3           ------")
            print("----------------------------------------------------------------")
            break
        else:
            print("No existe esa opción")
    except:
        print("ocurrio un error, vuelve a intentarlo")
        print("El error fue:", sys.exc_info()[0])
