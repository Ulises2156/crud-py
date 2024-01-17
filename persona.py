""" CRUD es un acrónimo que representa las operaciones básicas que se pueden realizar en un sistema de gestión de bases de datos o, de manera más general, en cualquier sistema que involucre almacenamiento y recuperación de datos. Las letras CRUD representan:

--C (Create): Crear nuevos registros o datos en la base de datos.
--R (Read): Leer o recuperar información existente de la base de datos.
--U (Update): Actualizar o modificar registros o datos existentes en la base de datos.
--D (Delete): Eliminar registros o datos existentes de la base de datos.
"""

from enum import Enum

class Sexo(Enum):
    M = "Masculino"
    F = "Femenino"

class Persona():
    def __init__(self, id, nombre, edad, sexo, comidas_favs):
        self.id : int = id
        self.nombre : str = nombre
        self.edad : int = edad
        self.sexo : Sexo = sexo
        self.comidas_favs : list = comidas_favs

    def saludo(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

    def agregar_comida(self, comida):
        self.comidas_favs.append(comida)

    def cenar_juntos(self, otra_persona):
        cenas_en_comun = set(self.comidas_favs).intersection(otra_persona.comidas_favs)
        return list(cenas_en_comun)
    
    def __str__(self) -> str:
        return f"""
        ---------------
        El nombre es: {self.nombre} y tiene {self.edad}
        Es de sexo: {self.sexo.value} y sus comidas favoritas son: {self.comidas_favs.__str__()}"""

# Ahora inicializamos una lista de personas 

personas= []

def mostrar_menu():
    print("\n ---Menú ---")
    print("1. Crear persona")
    print("2. Mostrar lista de las personas")
    print("3. Actualizar las persona de la lista")
    print("4. Eliminar persona de la lista")
    print("0. Presione el número 0 para salir del programa")

def crear_persona():
    accepted = False

    id = len(personas) + 1
    nombre = input("Ingrese el nombre: ")

    while not accepted:
        try:
            edad = int(input("Ingrese la edad: "))
            accepted = True
        except ValueError:
            print("Debe ingresar un numero entero.")

    accepted = False
    while not accepted:
        sexo = str(input("Ingrese el sexo (M/F): "))
        if sexo == 'M' or sexo == 'm':
            sexo = Sexo.M
            accepted = True
        elif sexo == 'F' or sexo == 'f':
            sexo = Sexo.F
            accepted = True

    comidas_favs = input("Ingrese las comidas favoritas (por favor separadas por comas): ").split(',')

    persona_nueva = Persona(id, nombre, edad, sexo, comidas_favs)
    personas.append(persona_nueva)
    print(f"\nPersona creada:\n{persona_nueva}")

def mostrar_personas():
    print("\n--- Lista de Personas ---")
    for persona in personas:
        print(persona)

def actualizar_persona():
    id_actualizar= int(input("Ingrese el ID de la persosa a actualizar: "))
    persona_encontrada= None

    for persona in personas:
        if persona.id == id_actualizar:
            persona_encontrada = persona
        break

    if persona_encontrada:
        print(f"\nPersona encontrada:\n{persona_encontrada.__dict__}")
        nombre = input("Ingrese el nuevo nombre: ")
        edad = int(input("Ingrese la nueva edad: "))
        sexo = str(input("Ingrese el nuevo sexo (M/F): "))
        comidas_favs = input("Ingrese las nuevas comidas favoritas (por favor separadas por comas): ").split(',')

        persona_encontrada.nombre = nombre
        persona_encontrada.edad = edad
        persona_encontrada.sexo = sexo
        persona_encontrada.comidas_favs = comidas_favs

        print("\nPersona actualizada:\n", persona_encontrada.__dict__)
    else:
        print(f"No se encontró ninguna persona con ID {id_actualizar}")

def eliminar_persona():
    id_eliminar = int(input("Ingrese el ID de la persona a eliminar: "))
    persona_encontrada = None

    for persona in personas:
        if persona.id == id_eliminar:
            persona_encontrada = persona
            break

    if persona_encontrada:
        personas.remove(persona_encontrada)
        print(f"\nPersona eliminada:\n{persona_encontrada.__dict__}")
    else:
        print(f"No se encontró ninguna persona con ID {id_eliminar}")


while True:
    mostrar_menu()
    opcion = input("Ingrese la opción deseada (1-0):")

    if opcion == "1":
        crear_persona()
    elif opcion == "2":
        mostrar_personas()
    elif opcion == "3":
        actualizar_persona()
    elif opcion == "4":
        eliminar_persona()
    elif opcion == "0":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opcion no válida. Intente nuevamente.")


persona1 = Persona(1, "Ulises", 21, Sexo.M, ["Pizza", "Hamburguesa", "Pasta"])
persona2 = Persona(2, "Fatima", 19, Sexo.F, ["Ensalada", "Pizza", "Sushi"])
persona3 = Persona(3,"Maira", 27, Sexo.F, ["Pizza", "Asado", "Lomito"])
persona4 = Persona(4, "Silvina", 47, Sexo.F, ["Lomito", "Ravioles", "Helado", "Pizza"])


for persona in [persona1, persona2, persona3, persona4]:
    print(persona.saludo())

cenas_en_comun_1_2 = persona1.cenar_juntos(persona2)
cenas_en_comun_1_3 = persona1.cenar_juntos(persona3)
cenas_en_comun_1_4 = persona1.cenar_juntos(persona4)

print(f"Cenas en común entre {persona1.nombre} y {persona2.nombre}: {cenas_en_comun_1_2}")
print(f"Cenas en común entre {persona1.nombre} y {persona3.nombre}: {cenas_en_comun_1_3}")
print(f"Cenas en común entre {persona1.nombre} y {persona4.nombre}: {cenas_en_comun_1_4}")