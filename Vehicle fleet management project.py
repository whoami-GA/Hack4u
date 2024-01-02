#!/usr/bin/env python3

class Vehiculo:

    def __init__(self, matricula, modelo, precio, combustible=10):
        self.matricula = matricula  # Asigna la matrícula del vehículo
        self.modelo = modelo  # Asigna el modelo del vehículo
        self.disponible = True  # Indica si el vehículo está disponible para alquilar
        self.precio = precio  # Asigna el precio del vehículo
        self.combustible = combustible  # Asigna el nivel de combustible por defecto como 10 litros

    def __str__(self):
        return f"Vehiculo(matricula={self.matricula}, modelo={self.modelo}, disponibilidad={self.disponible}, combustible={self.combustible}, precio = {self.precio})"
        # Devuelve una representación de cadena del vehículo

    def alquilar(self):
        if self.disponible:
            self.disponible = False  # Cambia el estado de disponibilidad a no disponible si el vehículo está disponible

    def devolver(self):
        if not self.disponible:
            self.disponible = True  # Cambia el estado de disponibilidad a disponible si el vehículo no está disponible

    def verificacion(self):
        if self.combustible >= 10:  # Verifica si el nivel de combustible es suficiente (10 litros en este caso)
            print(f"El vehículo con matrícula {self.matricula} tiene {self.combustible} litros de combustible suficiente.")
        else:
            print(f"El vehículo con matrícula {self.matricula} necesita reabastecimiento de combustible.")

    def verificacion_precio(self, precio, dias):
        print(f"\nEl precio por dia del coche es {precio} y los dias que queres alquilarlo son {dias}, el precio final por esos dias son: ({precio * dias})\n")



class Flota:

    def __init__(self):
        self.vehiculos = []  # Inicializa una lista vacía de vehículos

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)  # Agrega un vehículo a la lista de vehículos

    def alquilar_vehiculo(self, matricula, persona):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                print(f"{persona} Ha alquilado el coche con la matricula ({matricula})")
                vehiculo.alquilar()  # Llama al método 'alquilar' del vehículo correspondiente

    def devolver_vehiculo(self, matricula, persona):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                print(f"{persona} ha devuelto el coche con la matricula: {matricula}")
                vehiculo.devolver()  # Llama al método 'devolver' del vehículo correspondiente

    def __str__(self):
        return "\n".join(str(vehiculo) for vehiculo in self.vehiculos)
        # Devuelve una representación de cadena de la flota y sus vehículos

    def verificacion_combustible(self, matricula, nuevo_combustible):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.combustible = nuevo_combustible
                vehiculo.verificacion()  # Llama al método 'verificacion' del vehículo correspondiente

    def precio(self, matricula, dias):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                precio_vehiculo = vehiculo.precio
                vehiculo.verificacion_precio(precio_vehiculo ,dias)  # Llama al método 'verificacion_precio' del vehículo correspondiente

if __name__ == '__main__':

    flota = Flota() # instanciar la clase

    flota.agregar_vehiculo(Vehiculo("BAB 33 CJ", "Toyota Corolla", 50)) # crear objeto sobre la marcha
    flota.agregar_vehiculo(Vehiculo("SDF 23 AB", "Honda Civic", 75))

    print("\nFlota Inicial: \n")
    print(flota)

    flota.alquilar_vehiculo("SDF 23 AB", "Javier")

    print(f"\nMostrando la flota despues de haber alquilado el Toyota:\n")
    print(flota)

    flota.devolver_vehiculo("SDF 23 AB", "Javier")
    print(f"\nMostrando flota despues de devolver los vehiculos:\n")
    print(flota)

    flota.devolver_vehiculo("SDF 23 AB", "Javier")
    
    flota.verificacion_combustible("BAB 33 CJ", 78)

    flota.precio("SDF 23 AB", 15) 
