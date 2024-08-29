class Animal:
    # Constructor de la clase Animal, inicializa nombre, especie, área y la lista de tratamientos
    def __init__(self, nombre, especie, area):
        self.nombre = nombre
        self.especie = especie
        self.area = area
        self.tratamientos = []

    # Método para agregar un tratamiento a la lista de tratamientos del animal
    def agregar_tratamiento(self, medicamento, dosis, frecuencia):
        tratamiento = {
            "medicamento": medicamento,
            "dosis": dosis,
            "frecuencia": frecuencia
        }
        self.tratamientos.append(tratamiento)

    # Método para mostrar los tratamientos actuales del animal
    def mostrar_tratamientos(self):
        if self.tratamientos:  # Si hay tratamientos en la lista
            print(f"\nTratamientos para {self.nombre} ({self.especie}):")
            for i, tratamiento in enumerate(self.tratamientos, 1):  # Enumeramos los tratamientos
                print(f"{i}. Medicamento: {tratamiento['medicamento']}, "
                      f"Dosis: {tratamiento['dosis']}, "
                      f"Frecuencia: {tratamiento['frecuencia']}")
        else:  # Si no hay tratamientos, lo indicamos
            print(f"\n{self.nombre} ({self.especie}) no tiene tratamientos.")

    # Método para mostrar un resumen del animal (nombre, especie, área)
    def mostrar_resumen(self):
        print(f"Nombre: {self.nombre}, Especie: {self.especie}, Área: {self.area}")

# Función para crear un animal solicitando datos al usuario
def ingresar_datos_animal():
    nombre = input("Ingrese el nombre del animal: ")
    especie = input("Ingrese la especie del animal: ")
    area = input("Ingrese el área donde se encuentra el animal: ")
    return Animal(nombre, especie, area)  # Devuelve un objeto Animal con los datos ingresados

# Función para agregar tratamientos a un animal de manera interactiva
def agregar_tratamientos_interactivo(animal):
    while True:  # Bucle para agregar múltiples tratamientos
        medicamento = input(f"Ingrese el medicamento para {animal.nombre} (o 'salir' para terminar): ")
        if medicamento.lower() == 'salir':  # Condición de salida del bucle
            break
        dosis = input(f"Ingrese la dosis del medicamento {medicamento}: ")
        frecuencia = input(f"Ingrese la frecuencia del medicamento {medicamento}: ")
        animal.agregar_tratamiento(medicamento, dosis, frecuencia)  # Se añade el tratamiento al animal
        print(f"Tratamiento agregado para {animal.nombre}.\n")

# Ejecución principal del programa
animales = []  # Lista para almacenar los animales creados

while True:  # Bucle principal del programa
    print("\n--- Gestión de Animales del Zoológico ---")
    opcion = input("1. Ingresar nuevo animal\n2. Mostrar tratamientos de animales\n3. Mostrar registro completo\n4. Salir\nSeleccione una opción: ")
    
    if opcion == '1':  # Opción para ingresar un nuevo animal
        nuevo_animal = ingresar_datos_animal()
        animales.append(nuevo_animal)  # Añadimos el nuevo animal a la lista
        agregar_tratamientos_interactivo(nuevo_animal)  # Llamamos a la función para agregar tratamientos
    elif opcion == '2':  # Opción para mostrar los tratamientos de todos los animales registrados
        for animal in animales:  # Recorremos la lista de animales y mostramos sus tratamientos
            animal.mostrar_tratamientos()
    elif opcion == '3':  # Opción para mostrar el registro completo de animales
        if animales:  # Si hay animales en la lista
            print("\n--- Registro Completo de Animales ---")
            for animal in animales:
                animal.mostrar_resumen()  # Mostramos un resumen de cada animal
                animal.mostrar_tratamientos()  # Mostramos sus tratamientos (si tiene)
        else:
            print("\nNo hay animales registrados.")
    elif opcion == '4':  # Opción para salir del programa
        print("Saliendo del programa.")
        break
    else:  # Manejo de entradas inválidas
        print("Opción no válida. Intente de nuevo.")





