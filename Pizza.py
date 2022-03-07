class Pizza(object):
    def __init__(self, ingrediente, tiempo):
        self.ingrediente = ingrediente
        self.tiempo = tiempo

class pizzaPepperoni(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Pepperoni",3)

class pizzaSalchicha(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Salchicha",4)

class pizzaCarne(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Carne",10)

class pizzaQueso(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Queso",5)

class pizzaPiña(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Piña",2)