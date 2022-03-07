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

    def recorrerSinDetalles(self):
        actual = self.cabeza
        contador = 0
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")
        print("La lista de ordenes es:")
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

