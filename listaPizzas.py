from nodoPizza import nodoPizza

class listaPizzas:
    def __init__(self):
        self.cabeza = None

    def insertarPizza(self, Pizza):
        if self.cabeza is None:
            self.cabeza = nodoPizza(Pizza=Pizza)
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodoPizza(Pizza=Pizza)
    
    def recorrer(self):
        actual = self.cabeza
        while actual != None:
            print("Pizza de:",actual.Pizza.ingrediente,",  tiempo aproximado de preparación:",actual.Pizza.tiempo,"minutos")
            actual=actual.siguiente

    def tiempoEspera(self):
        actual = self.cabeza
        tiempo = 0
        while actual != None:
            tiempo = tiempo + int(actual.Pizza.tiempo)
            actual=actual.siguiente
        return tiempo