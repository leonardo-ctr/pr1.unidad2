print(" ")#define una linea en blanco
print("Roman De la Cruz leonardo Antonio.3-w")
# Crear una lista para almacenar los números ganadores
numeros_ganadores = []
print(" ")#define una linea en blanco
# Preguntar al usuario cuántos números desea ingresar
cantidad = int(input("¿Cuántos números ganadores desea ingresar? "))
print(" ")#define una linea en blanco
# Recoger los números ganadores
for i in range(cantidad):
    numero = int(input(f"Ingrese el número ganador {i + 1}: "))
    numeros_ganadores.append(numero)
print(" ")#define una linea en blanco
# Ordenar la lista de menor a mayor
numeros_ganadores.sort()
print(" ")#define una linea en blanco
# Mostrar la lista de números ganadores
print("\nNúmeros ganadores de la lotería en orden de menor a mayor:")
for numero in numeros_ganadores:
    print(numero)
    print(" ")#define una linea en blanco