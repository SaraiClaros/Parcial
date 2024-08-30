from datetime import datetime
# Clase para representar un producto en la tienda
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
# Clase para gestionar una venta
class Venta:
    def __init__(self):
        self.productos = []
        self.total = 0
    # Método para agregar un producto a la venta
    def agregar_producto(self, producto, cantidad):
        self.productos.append((producto, cantidad))
        self.total += producto.precio * cantidad # Calcula el total acumulado
   # Método para mostrar los detalles de la venta
    def mostrar_detalles(self):
        print("-----------------------------------------------------------")
        print("\n--- Detalles de la Venta ---")
        # Muestra el nombre, cantidad y precio unitario de cada producto
        for producto, cantidad in self.productos:
            print(f"Producto: {producto.nombre}, Cantidad: {cantidad}, Precio Unitario: ${producto.precio:.2f}")
            # Muestra el total a pagar
        print(f"Total a pagar: ${self.total:.2f}")
    # Método para calcular el vuelto dado el monto pagado por el cliente
    def calcular_vuelto(self, monto_pagado):
        if monto_pagado < self.total:
            print("Monto insuficiente para cubrir la venta.")
            return 0
        return monto_pagado - self.total
# Clase para gestionar la tienda
class Tienda:
    def __init__(self):
        self.proveedores = []
   # Método para registrar una venta
    def registrar_venta(self):
        venta = Venta()
        
        print("\n--- Registro de Venta ---")
        while True:
            nombre_producto = input("Ingrese el nombre del producto (o presione Enter para terminar): ")
            if nombre_producto == "":
                break # Sale del bucle si no se ingresa un nombre de producto
            cantidad = int(input(f"Ingrese la cantidad de {nombre_producto}: "))
            precio = float(input(f"Ingrese el precio unitario de {nombre_producto}: "))
            producto = Producto(nombre_producto, precio)
            venta.agregar_producto(producto, cantidad)
        venta.mostrar_detalles()  # Muestra los detalles de la venta
        monto_pagado = float(input("Ingrese el monto pagado por el cliente: "))
        vuelto = venta.calcular_vuelto(monto_pagado)
        print(f"Vuelto a entregar: ${vuelto:.2f}")
     # Método para registrar un proveedor
    def registrar_proveedor(self):
        nombre_proveedor = input("Ingrese el nombre del proveedor: ")
        nombre_producto = input("Ingrese el nombre del producto entregado: ")
        precio_sugerido = float(input(f"Ingrese el precio sugerido para {nombre_producto}: "))
        producto = Producto(nombre_producto, precio_sugerido)
        self.proveedores.append((nombre_proveedor, producto))
        print(f"Producto '{nombre_producto}' registrado con precio sugerido de ${precio_sugerido:.2f}.")

    # Método para mostrar los detalles de los proveedores
    def mostrar_proveedores(self):
        if self.proveedores:
            print("\n--- Detalles de Proveedores ---")
            for proveedor, producto in self.proveedores:
                print(f"Proveedor: {proveedor}")
                print(f"Producto: {producto.nombre}, Precio Sugerido: ${producto.precio:.2f}")
                print("-----------------------------")
              
        else:
            # Muestra un mensaje si no hay proveedores registrados
            print("No hay proveedores registrados.")


tienda = Tienda()

while True:
    print("\n--- Sistema de Gestión de la Tienda ---")
    print("1. Registrar venta")
    print("2. Registrar proveedor")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        tienda.registrar_venta() # Llama al método para registrar una venta
    elif opcion == "2":
        tienda.registrar_proveedor() # Llama al método para registrar un proveedor
    elif opcion == "3":
        print("Saliendo del sistema...")
        break
    else: # Sale del bucle y termina el programa
        print("Opción no válida. Por favor, intente nuevamente.")


print("-----------------------------------------------------------")


