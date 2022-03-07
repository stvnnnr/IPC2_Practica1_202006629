from listaPizzas import listaPizzas

class Persona:
    def __init__(self, nombre, telefono, tiempoEspera):
        self.nombre = nombre
        self.telefono = telefono
        self.tiempoEspera = tiempoEspera
        self.listaPizzas = listaPizzas

    def setLista(self, listaPizzas):
        self.listaPizzas = listaPizzas

    def getLista(self):
        return self.listaPizzas