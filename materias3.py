print(" ")
print("Roman De la Cruz leonardo Antonio.3-w")
print(" ")#define una linea en blanco
# Almacenar las materias en una lista
materias = [
    "Pensamiento matemático",
    "humanidades",
    "Inglés",
    "ecosistemas",
    "metodologias",
    "Frameworks",
    "sociemocional",
    "lengua y comunicacion",
]
print(" ")#define una linea en blanco
# Crear un diccionario para almacenar las calificaciones
calificaciones = {}
print(" ")#define una linea en blanco
# Pedir al usuario que ingrese la calificación para cada materia
for materia in materias:
    calificacion = input(f"Ingrese la calificación para {materia}: ")
    calificaciones[materia] = calificacion
print(" ")#define una linea en blanco
# Desplegar las calificaciones
print("\nCalificaciones obtenidas:")
for materia, calificacion in calificaciones.items():
    print(f"En {materia} has obtenido {calificacion}.")
    print(" ")#define una linea en blanco