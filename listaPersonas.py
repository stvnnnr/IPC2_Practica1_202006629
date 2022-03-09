import sys
from os import startfile, system
from tkinter.messagebox import NO
from nodoPersona import nodoPersona

class listaPersonas:
    def __init__(self):
        self.cabeza = None

    def insertarPersona(self, Persona):
        if self.cabeza is None:
            self.cabeza = nodoPersona(Persona=Persona)
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodoPersona(Persona=Persona)

    def eliminarEleccion(self,nombre):
        if self.cabeza != None:
            actual=self.cabeza
            anterior = None
            print("Orden de:",nombre,"eliminada")
            while actual and actual.Persona.nombre != nombre:
                anterior=actual
                actual=actual.siguiente

            if anterior is None:
                self.cabeza = actual.siguiente
                actual.siguiente = None
            elif actual:
                anterior.siguiente = actual.siguiente
                actual.siguiente = None
        else:
            print("No hay nadie haciendo fila para eliminar pedido")

    def eliminarPrimero(self):
        if self.cabeza != None:
            self.despachada(self.cabeza.Persona.nombre)
            self.cabeza = self.cabeza.siguiente
            actual=self.cabeza
            if self.cabeza != None:
                while actual.siguiente:
                    actual=actual.siguiente
                actual.siguiente = None
        else:
            print("No hay nadie haciendo fila para despacharle")

    def despachada(self, nombre):
        actual = self.cabeza
        while actual != None:
            if actual and actual.Persona.nombre == nombre:
                print("Orden de:",actual.Persona.nombre,"fue despachada con éxito")
                print("su pedido era:")
                listaPizza = actual.Persona.getLista()
                listaPizza.recorrer()
            actual = actual.siguiente

    def menuEliminar(self):
        actual = self.cabeza
        print("")
        print("")
        print("")
        print("|                          MENU PEDIDOS                          |")
        n=1
        while actual != None:
            print("  ",n,".",actual.Persona.nombre,".                     ")
            n = n+1
            actual=actual.siguiente
        print("   0 . Volver .")

    def mantenerMenuEliminar(self):
        correcto = False
        actual = self.cabeza
        while (not correcto):
            try:
                if actual != None:
                    self.menuEliminar()
                    select = int(input("Que pedido desea eliminar:"))
                    print("\n")
                    n = 1
                    while actual != None:
                        if select == 0:
                            correcto = True
                        elif select == n:
                            self.eliminarEleccion(actual.Persona.nombre)
                            correcto = True
                            break
                        n = n+1
                        actual=actual.siguiente
                    if select != n and select !=0:
                        print("esa opcion no existe")
                else:
                    print("No hay personas haciendo fila, el lugar esta vacio :(")
                    correcto = True
            except:
                print("ocurrio un error, vuelve a intentarlo")
                print("El error fue:", sys.exc_info()[0])

    def recorrerSinDetalles(self):
        actual = self.cabeza
        contador = 0
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")
        print("La lista de ordenes es:")
        print("------------------------------------------------")
        if actual == None:
            print("No hay personas haciendo fila, el lugar esta vacio :(")
        while actual != None:
            actualitUno = self.cabeza
            contador = contador+1
            tAcomulado = 0
            for i in range(contador):
                tiempoUno = actualitUno.Persona.tiempoEspera
                tAcomulado = tAcomulado+tiempoUno
                actualitUno = actualitUno.siguiente
            print(contador,".","Orden de:",actual.Persona.nombre, ", y su pedido estara en:",tAcomulado,"minutos")
            print("------------------------------------------------")
            actual=actual.siguiente
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")

    def recorrerConDetalles(self):
        actual = self.cabeza
        contador = 0
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")
        print("La lista de ordenes es:")
        print("------------------------------------------------")
        if actual == None:
            print("No hay personas haciendo fila, el lugar esta vacio :(")
        while actual != None:
            actualitUno = self.cabeza
            contador = contador+1
            tAcomulado = 0
            for i in range(contador):
                tiempoUno = actualitUno.Persona.tiempoEspera
                tAcomulado = tAcomulado+tiempoUno
                actualitUno = actualitUno.siguiente
            listaPizza = actual.Persona.getLista()
            print(contador,".","Orden de:",actual.Persona.nombre, ", y su pedido estara listo en:",tAcomulado,"minutos")
            listaPizza.recorrer()
            print("------------------------------------------------")
            actual=actual.siguiente
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")

    def pintar(self):
        if self.cabeza != None:
            actual = self.cabeza.siguiente
            lista = "Mostrador -> "+self.cabeza.Persona.nombre+"; \n"
            lista = lista + self.cabeza.Persona.nombre +" -> "
            while actual != None:
                lista = lista + actual.Persona.nombre + " -> "
                actual=actual.siguiente
            lista = lista[:-3]
            lista = lista + ";\n"
            return lista

    def graficar(self):
        actual = self.cabeza
        if actual != None:
            try:
                listaFila = self.pintar()
                Archivo = open('cola.dot', 'w')
                cabeza = '''digraph G {
                                fontname="Arial"
                                node [fontname="Arial" shape=box3d]
                                edge [fontname="Arial"]

                                subgraph cluster_1 {
                                    Mostrador [shape=house];
                                    node [style=filled fillcolor=skyblue];\n'''
                Archivo.write(cabeza)
                Archivo.write(listaFila)
                luegoDelName = '''label = "FILA DE PEDIDOS";
                                    color=red
                                }
                            }'''
                Archivo.write(luegoDelName)
                Archivo.close()
                system('dot -Tpng cola.dot -o cola.png')
                startfile('cola.png')
            except:
                print("ocurrio un error, vuelve a intentarlo")
                print("El error fue:", sys.exc_info()[0])
        else:
            try:
                listaFila = self.pintar()
                Archivo = open('cola.dot', 'w')
                cabeza = '''digraph G {
                                fontname="Arial"
                                node [fontname="Arial" shape=box3d]
                                edge [fontname="Arial"]

                                subgraph cluster_1 {
                                    Mostrador [shape=house];
                                    node [style=filled fillcolor=skyblue];
                                    label = "FILA DE PEDIDOS";
                                    color=red
                                }
                            }'''
                Archivo.write(cabeza)
                Archivo.close()
                system('dot -Tpng cola.dot -o cola.png')
                startfile('cola.png')
            except:
                print("ocurrio un error, vuelve a intentarlo")
                print("El error fue:", sys.exc_info()[0])
