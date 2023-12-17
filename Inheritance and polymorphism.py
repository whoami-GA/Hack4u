#    def __init__(self, nombre):
        
#        self.nombre = nombre

#    def hablar(self):

#        raise NotImplementedError("Las subclases definidas deben implementar este metodo")

#class Gato(Animal): #Gato(Animal(gato, nombre))
    
#    def hablar(self):

#        return f"{self.nombre} dice miau!"

#class Perro(Animal):

#    def hablar(self):

#        return f"{self.nombre} dice WOW"


#gato = Gato("Firulais")
#perro = Perro("Alfredo")
#gato_dos = Animal("mimi")

#print(gato.hablar())
#print(perro.hablar())
#print(gato_dos.hablar()



    #Polimorfismo
#class Animal:

#    def __init__(self, nombre):
        
#        self.nombre = nombre

#    def hablar(self):

#        raise NotImplementedError("Las subclases definidas deben implementar este metodo")

#class Gato(Animal): #Gato(Animal(gato, nombre))
    
#    def hablar(self):

#        return f"miau!"

#class Perro(Animal):

#    def hablar(self):

#        return f"WOW"


#def hacer_hablar(objeto):

#      print(f"{objeto.nombre} dice {objeto.hablar()}")


#gato = Gato("Firulais")
#perro = Perro("Alfredo")

#hacer_hablar(gato)
#hacer_hablar(perro)

    #Herencia
#class Automobil:

#    def __init__(self, marca, modelo):

#        self.marca = marca
#        self.modelo = modelo

#    def describir(self):

#        return f"Vehiculo: {self.marca} {self.modelo}"

#class Coche(Automobil):

#    def describir(self):

#        return f"Coche: {self.marca} {self.modelo}"

#class Moto(Automobil):

#    def describir(self):

#        return f"Moto: {self.marca} {self.modelo}"

#coche = Coche("Toyota", "corolla")
#moto = Moto("Honda", "Shadow")
#print(moto.describir())
#print(coche.describir())


    # Polimorfismo

#class Automobil:

#    def __init__(self, marca, modelo):

#        self.marca = marca
#        self.modelo = modelo

#    def describir(self):

#        return f"Vehiculo: {self.marca} {self.modelo}"

#class Coche(Automobil):

#    def describir(self):

#        return f"Coche: {self.marca} {self.modelo}"

#class Moto(Automobil):

#    def describir(self):

        #        return f"Moto: {self.marca} {self.modelo}"

#def describir_vehiculo(vehiculo):   # Polimorfismo
    
    #    print(vehiculo.describir())



#coche = Coche("Toyota", "corolla")
#moto = Moto("Honda", "Shadow")

#describir_vehiculo(coche)
#describir_vehiculo(moto)

class Dispositivo:

    def __init__(self, modelo):
        
        self.modelo = modelo

    def escanear_Vuln(self):

        raise NotImplementedError("Este metodo debe de ser definido para el resto de subclases existentes")

class Ordenador(Dispositivo):

    def escanear_Vuln(self):
        
        return f"[+] Analisis de Vulns concluido: Actualizacion de software necesaria, multiples desactualizacionesde software detectadas"

class Router(Dispositivo):

    def escanear_Vuln(self):

        return f"[+] Analisis de Vulns concluido: Multiples puertos criticos detectados como abiertos, es recomendable cerrar estos puertos"
 
class TelefonoMovil(Dispositivo):

    def escanear_Vuln(self):

        return f"[+] Analisis de Vulns concluido: Multiples aplicaciones detectadas con permisos excesivos"

def realizar_escaneo(dispositivo):

    print(dispositivo.escanear_Vuln())

pc = Ordenador("Dell XPS")
router = Router("Tp-Link Archer C50")
movil = TelefonoMovil("Samsung Galaxy S21")


realizar_escaneo(pc)
realizar_escaneo(router)
realizar_escaneo(movil)

# -----------
#    def __init__(self, x):
#        self.x = x
#        print(f"Valor en x: {self.x}")

#class B(A):
    
#    def __init__(self, x, y):
#        self.y = y
#        super().__init__(x) # Pasar por el proceso que sea el de la clase padre
#        print(f"Valor en y: {self.y}")

#b = B(2, 10)

# Valor en x: 2
# valor en y: 10


#class A:

#    def saludo(self):
        
#        return "Salduo desde A"

#class B(A):

#    def saludo(self):
        #        original = super().saludo()
#        print(f"{original}, pero tambien salduo desde B")

# Saludo desde A pero tambien saludo desde B

#saludo = A()
#print(saludo.saludo())

# Super Herencia y polimorfismo

class Persona:

    def __init__(self, nombre, edad):
        
        self.nombre = nombre
        self.edad = edad

    def saludo(self):

         return f"Hola, soy {self.nombre} y tengo {self.edad} anos"

class Empleado(Persona):

    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def saludo(self):

        return f"{super().saludo()}, y cobro {self.salario} euros Brutos Anuales"

persona = Empleado("Alicia", 23, 32000)
print(persona.saludo())

