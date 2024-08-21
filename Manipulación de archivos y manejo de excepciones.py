import os

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters y setters
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def to_file_format(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}\n"

    @staticmethod
    def from_file_format(line):
        id, nombre, cantidad, precio = line.strip().split(',')
        return Producto(id, nombre, int(cantidad), float(precio))


class Inventario:
    FILE_NAME = "inventario.txt"

    def __init__(self):
        self.productos = []
        self.cargar_productos()

    def guardar_productos(self):
        try:
            with open(self.FILE_NAME, 'w') as file:
                for producto in self.productos:
                    file.write(producto.to_file_format())
            print("Inventario guardado con éxito.")
        except (IOError, PermissionError) as e:
            print(f"Error al guardar el inventario: {e}")

    def cargar_productos(self):
        if os.path.exists(self.FILE_NAME):
            try:
                with open(self.FILE_NAME, 'r') as file:
                    lines = file.readlines()
                    self.productos = [Producto.from_file_format(line) for line in lines]
            except (IOError, ValueError) as e:
                print(f"Error al cargar el inventario: {e}")
                self.productos = []
        else:
            print("Archivo de inventario no encontrado, se creará uno nuevo.")

    def añadir_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID del producto ya existe.")
        else:
            self.productos.append(producto)
            self.guardar_productos()
            print("Producto añadido con éxito.")

    def eliminar_producto(self, id):
        producto = next((p for p in self.productos if p.get_id() == id), None)
        if producto:
            self.productos.remove(producto)
            self.guardar_productos()
            print("Producto eliminado con éxito.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        producto = next((p for p in self.productos if p.get_id() == id), None)
        if producto:
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            self.guardar_productos()
            print("Producto actualizado con éxito.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos_los_productos(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacío.")


def mostrar_menu():
    print("\n--- Menú de Gestión de Inventario ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje en blanco si no desea cambiarla): ")
            precio = input("Ingrese el nuevo precio (deje en blanco si no desea cambiarlo): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == '5':
            inventario.mostrar_todos_los_productos()

        elif opcion == '6':
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
