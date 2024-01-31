from enum import Enum

class Sexo(Enum):
    M = "Masculino"
    F = "Femenino"

class Persona:
    def __init__(self, id, nombre, edad, sexo, comidas_favs):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.comidas_favs = comidas_favs

    def saludo(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

    def agregar_comida(self, comida):
        self.comidas_favs.append(comida)

    def cenar_juntos(self, otra_persona):
        cenas_en_comun = set(self.comidas_favs).intersection(otra_persona.comidas_favs)
        return list(cenas_en_comun)
    
    def __str__(self):
        return f"""
        -----------
        Persona:(id:{self.id}, nombre:{self.nombre}, Edad: {self.edad}, Sexo: {self.sexo.value}, Comidas favoritas: {', '.join(self.comidas_favs)})"""

def cargar_datos_predefinidos(personas):
    # aqui vamos a cargar los datos determinados para que el usuario pueda ver la función al instante
    personas.extend([
        Persona(1, "Ulises", 21, Sexo.M, ["Pizza", "Hamburguesa", "Pasta"]),
        Persona(2, "Fatima", 19, Sexo.F, ["Ensalada", "Pizza", "Sushi"]),
        Persona(3, "Maira", 27, Sexo.F, ["Pizza", "Asado", "Lomito"]),
        Persona(4, "Silvina", 47, Sexo.F, ["Lomito", "Ravioles", "Helado", "Pizza"])
    ])
    print("Datos precargados exitosamente.")


    persona1 = Persona(1, "Ulises", 21, Sexo.M, ["Pizza", "Hamburguesa", "Pasta"])
    persona2 = Persona(2, "Fatima", 19, Sexo.F, ["Ensalada", "Pizza", "Sushi"])
    persona3 = Persona(3, "Maira", 27, Sexo.F, ["Pizza", "Asado", "Lomito"])
    persona4 = Persona(4, "Silvina", 47, Sexo.F, ["Lomito", "Ravioles", "Helado", "Pizza"])

    personas = [persona1, persona2, persona3, persona4]

    def interactuar_con_personas(personas):
        for persona in personas:
            print(persona.saludo())

    while True:
        print("\n--- Opciones ---")
        print("1. Saludar entre personas")
        print("2. Ver cenas en común")
        print("3. Volver al menú principal")
        opcion = input("Ingrese la opción deseada (1-3): ")

        if opcion == "1":
            saludar_entre_personas(personas)
        elif opcion == "2":
            cenas_en_comun_1_2 = persona1.cenar_juntos(persona2)
            cenas_en_comun_1_3 = persona1.cenar_juntos(persona3)
            cenas_en_comun_1_4 = persona1.cenar_juntos(persona4)

            print(f"Cenas en común entre {persona1.nombre} y {persona2.nombre}: {cenas_en_comun_1_2}")
            print(f"Cenas en común entre {persona1.nombre} y {persona3.nombre}: {cenas_en_comun_1_3}")
            print(f"Cenas en común entre {persona1.nombre} y {persona4.nombre}: {cenas_en_comun_1_4}")
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def saludar_entre_personas(personas):
    print("\n--- Personas Disponibles ---")
    for i, persona in enumerate(personas):
        if isinstance(persona, Persona):
            print(f"{i + 1}. {persona.nombre}")

    seleccion1 = int(input("Seleccione el número de la primera persona para saludar: "))
    seleccion2 = int(input("Seleccione el número de la segunda persona para saludar: "))

    try:
        persona1 = personas[seleccion1 - 1]
        persona2 = personas[seleccion2 - 1]

        if isinstance(persona1, Persona) and isinstance(persona2, Persona):
            print(f"\n{persona1.saludo()} y {persona2.saludo()}")
        else:
            print("Selección no válida. Ambas selecciones deben ser personas.")
    except (IndexError, ValueError):
        print("Selección no válida. Asegúrese de ingresar números válidos.")





def cargar_datos():
    personas = []
    try:
        with open("datos_personas.csv", "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                campos = linea.strip().split(',')
                id, nombre, edad, sexo, comidas_favs = int(campos[0]), campos[1], int(campos[2]), Sexo(sexo), campos[4].split(',')
                personas.append(Persona(id, nombre, edad, sexo, comidas_favs))
    except FileNotFoundError:
        print("No se encontró el archivo de datos. Se iniciará con una lista vacía.")
    
    return personas

def guardar_datos(personas):
    with open("datos_personas.csv", "w") as archivo:
        for persona in personas:
            archivo.write(f"{persona.id},{persona.nombre},{persona.edad},{persona.sexo.value},{','.join(persona.comidas_favs)}\n")

# ACORDATE QUE ESTAMOS 
personas = []

cargar_datos=()

def mostrar_menu():
    print("\n ---Menú ---")
    print("1. Crear persona")
    print("2. Mostrar lista de las personas")
    print("3. Actualizar persona de la lista")
    print("4. Eliminar persona de la lista")
    print("5. Guardar los datos y salir")
    print("6. Guardar su preset de datos")
    print("7. Saludar con su preset")
    print("8. CARGAR LOS DATOS PREDETERMINADO DEL SISTEMA")
    print("0. Presione el número 0 para salir del programa")

def crear_persona(personas):
    id = len(personas) + 1
    nombre = input("Ingrese el nombre: ")

    while not nombre.strip():
        print("¡NOMBRE OBLIGATORIO! Por favor, ingrese su nombre.")
        nombre = input("Ingrese el nombre: ")

    edad = int(input("Ingrese la edad: "))

    sexo_input = input("Ingrese el sexo (M/F): ").upper()
    while sexo_input not in ['M', 'F']:
        print("Por favor, ingrese 'M' o 'F' para el sexo.")
        sexo_input = input("Ingrese el sexo (M/F): ").upper()
    sexo = Sexo.M if sexo_input == 'M' else Sexo.F

    comidas_favs = input("Ingrese las comidas favoritas (por favor separadas por comas): ")
    while not comidas_favs or not any(c.isalpha() for c in comidas_favs):
        print("¡Al menos una comida favorita es obligatoria! Por favor, ingrese las comidas separadas por comas.")
        comidas_favs = input("Ingrese las comidas favoritas (por favor separadas por comas): ")

    persona_nueva = Persona(id, nombre, edad, sexo, comidas_favs.split(","))
    personas.append(persona_nueva)
    print(f"\nPersona creada:\n{persona_nueva}")

def guardar_preset(personas):
    accepted = False
    nombre_preset = input("Ingrese el nombre que quiere guardar: ")
    while not nombre_preset.strip():
        print("¡NOMBRE OBLIGATORIO! Por favor, ingrese su nombre.")
        nombre_preset = str(input("Ingrese el nombre: "))
    
    if nombre_preset:
        while not accepted:
            try:
                edad_preset = int(input("Ingrese la edad del preset: "))
                accepted = True
            except ValueError:
                print("Debe ingresar un numero entero de su edad:")
        sexo_input = str(input("Ingrese el sexo del preset (M/F): ")).upper()
        while sexo_input not in ['M', 'F']:
            print("Por favor, ingrese 'M' o 'F' para el sexo.")
            sexo_input = input("Ingrese el sexo del preset (M/F): ").upper()
        sexo_preset = Sexo.M if sexo_input == 'M' else Sexo.F

        comidas_favs_preset = input("Ingrese las comidas favoritas del preset (separadas por comas): ")
        while not comidas_favs_preset or not any(c.isalpha() for c in comidas_favs_preset):
            print("¡Al menos una comida favorita es obligatoria! Por favor, ingrese las comidas separadas por comas.")
            comidas_favs_preset = input("Ingrese las comidas favoritas del preset (separadas por comas): ")

        preset = Persona(len(personas) + 1, nombre_preset, edad_preset, sexo_preset, comidas_favs_preset.split(","))
        personas.append(preset)
        print(f"\nPreset '{nombre_preset}' guardado:\n{preset}")
        return preset
    else:
        print("El nombre del preset no puede estar vacío.")
        return None

def saludar_con_preset(personas):
    print("\n--- Personas Disponibles ---")
    for i, persona in enumerate(personas):
        if isinstance(persona, Persona):
            print(f"{i + 1}. {persona.nombre}")

    seleccion = input("Seleccione el número de persona o preset para saludar: ")
    try:
        seleccion = int(seleccion)
        if 1 <= seleccion <= len(personas):
            seleccionado = personas[seleccion - 1]
            nombre_persona = seleccionado.nombre
            if isinstance(seleccionado, Persona):
                nombre_persona = seleccionado.nombre
                print(f"\n¡Hola! Saludos a {nombre_persona}.")
            elif isinstance(seleccionado, dict):
                print("\n¡Hola! Saludos al preset:")
                print(f"Nombre: {seleccionado['nombre']}")
                print(f"Edad: {seleccionado['edad']}")
                print(f"Sexo: {seleccionado['sexo'].value}")
                print(f"Comidas favoritas: {', '.join(seleccionado['comida_favs'])}")
            else:
                print("Selección no válida.")
        else:
            print("Selección no válida.")
    except ValueError:
        print("Ingrese un número válido.")

def mostrar_personas(personas):
    print("\n--- Lista de Personas ---")
    for persona in personas:
        if isinstance(persona, Persona):
            print(persona)

def actualizar_persona(personas):
    id_actualizar = int(input("Ingrese el ID de la persona a actualizar: "))
    persona_encontrada = None

    for persona in personas:
        if isinstance(persona, Persona) and persona.id == id_actualizar:
            persona_encontrada = persona
            break

    if persona_encontrada:
        print(f"\nPersona encontrada:\n{persona_encontrada.__dict__}")
        nombre = input("Ingrese el nuevo nombre: ")
        edad = int(input("Ingrese la nueva edad: "))
        sexo_input = input("Ingrese el nuevo sexo (M/F): ").upper()
        while sexo_input not in ['M', 'F']:
            print("Por favor, ingrese 'M' o 'F' para el sexo.")
            sexo_input = input("Ingrese el nuevo sexo (M/F): ").upper()
        sexo = Sexo.M if sexo_input == 'M' else Sexo.F

        comidas_favs = str(input("Ingrese las nuevas comidas favoritas (por favor separadas por comas): ").split(','))
        while not comidas_favs or not any(c.isalpha() for c in comidas_favs):
            print("¡Al menos una comida favorita es obligatoria! Por favor, ingrese las comidas separadas por comas.")
            comidas_favs = input("Ingrese las nuevas comidas favoritas (por favor separadas por comas): ")

        persona_encontrada.nombre = nombre
        persona_encontrada.edad = edad
        persona_encontrada.sexo = sexo
        persona_encontrada.comidas_favs = comidas_favs.split(',')

        print("\nPersona actualizada:\n", persona_encontrada.__dict__)
    else:
        print(f"No se encontró ninguna persona con ID {id_actualizar}")

def eliminar_persona(personas):
    id_eliminar = int(input("Ingrese el ID de la persona a eliminar: "))
    persona_encontrada = None

    for persona in personas:
        if isinstance(persona, Persona) and persona.id == id_eliminar:
            persona_encontrada = persona
            break

    if persona_encontrada:
        personas.remove(persona_encontrada)
        print(f"\nPersona eliminada:\n{persona_encontrada.__dict__}")
    else:
        print(f"No se encontró ninguna persona con ID {id_eliminar}")

if __name__ == "__main__":


    while True:
        mostrar_menu()
        opcion = input("Ingrese la opción deseada (1-0): ")

        if opcion == "1":
            crear_persona(personas)
        elif opcion == "2":
            mostrar_personas(personas)
        elif opcion == "3":
            actualizar_persona(personas)
        elif opcion == "4":
            eliminar_persona(personas)
        elif opcion == "5":
            guardar_datos(personas)
        elif opcion == "6":
            guardar_preset(personas)
        elif opcion == "7":
            saludar_con_preset(personas)
        elif opcion =="8":
            cargar_datos_predefinidos(personas)
        elif opcion == "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
