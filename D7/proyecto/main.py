""" CUENTA BANCARIA"""

# Primero crear una clase llamada Persona, que tenga solo dos atributos: nombre y apellido. 
# Luego, crear una segunda clase llamada Cliente, y Cliente va a heredar los atributos de Persona, pero también va a tener atributos propios, como número de cuenta y balance, es decir, el saldo que tiene en su cuenta bancaria. 
# Cliente también va a tener tres métodos: 
# - El primero va a ser uno de los métodos especiales y es el que permite que podamos imprimir a nuestro cliente. Este método va a permitir que cuando el código pida imprimir Cliente, se muestren todos sus datos, incluyendo el balance de su cuenta. 
# - Luego, un método llamado Depositar, que le va a permitir decidir cuánto dinero quiere agregar a su cuenta. 
# - Y finalmente, un tercer método llamado Retirar, que le permita decidir cuánto dinero quiere sacar de su cuenta.


class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Hola {self.nombre} {self.apellido}, con N° de Cuenta {self.numero_cuenta}, tu balance es de {self.balance}"
    
    def Depositar(self):
        input("¿Cuánto dinero quieres depositar a tu cuenta?  ")
    
    def Retirar(self):
        input("¿Cuánto dinero quieres retirar de tu cuenta?  ")


persona = Cliente("Mimi", "Succar", 123456789, 1000.00)
print(persona)
persona.Depositar()
persona.Retirar()