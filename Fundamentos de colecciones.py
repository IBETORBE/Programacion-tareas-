import json


class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        self.producto_id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.producto_id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __repr__(self):
        return f"Producto(ID: {self.producto_id}, Nombre: '{self.nombre}', Cantidad: {self.cantidad}, Precio: {self.precio})"


class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print(f"El producto con ID {producto.get_id()} ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print(f"Producto '{producto.get_nombre()}' añadido.")

    def eliminar_producto(self, producto_id):
        if producto_id in self.productos:
            del self.productos[producto_id]
            print(f"Producto con ID {producto_id} eliminado.")
        else:
            print(f"Producto con ID {producto_id} no encontrado.")

    def actualizar_producto(self, producto_id, cantidad=None, precio=None):
        if producto_id in self.productos:
            producto = self.productos[producto_id]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            print(f"Producto con ID {producto_id} actualizado.")
        else:
            print(f"Producto con ID {producto_id} no encontrado.")

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    def mostrar_todos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_a_archivo(self, archivo):
        with open(archivo, 'w') as f:
            productos_dict = {p.get_id(): p.__dict__ for p in self.productos.values()}
            json.dump(productos_dict, f, indent=4)
        print(f"Inventario guardado en {archivo}.")

    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, 'r') as f:
                productos_dict = json.load(f)
                self.productos = {pid: Producto(**datos) for pid, datos in productos_dict.items()}
            print(f"Inventario cargado desde {archivo}.")
        except FileNotFoundError:
            print(f"No se encontró el archivo {archivo}.")
        except json.JSONDecodeError:
            print("Error al leer el archivo.")


def mostrar_menu():
    print("\n--- Menú de Gestión de Inventario ---")
    print("1. Añadir Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar Producto por Nombre")
    print("5. Mostrar Todos los Productos")
    print("6. Guardar Inventario en Archivo")
    print("7. Cargar Inventario desde Archivo")
    print("8. Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        eleccion = input("Selecciona una opción: ")

        if eleccion == '1':
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif eleccion == '2':
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif eleccion == '3':
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco si no se actualiza): ")
            precio = input("Nuevo precio (dejar en blanco si no se actualiza): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif eleccion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif eleccion == '5':
            inventario.mostrar_todos()

        elif eleccion == '6':
            archivo = input("Nombre del archivo para guardar el inventario: ")
            inventario.guardar_a_archivo(archivo)

        elif eleccion == '7':
            archivo = input("Nombre del archivo para cargar el inventario: ")
            inventario.cargar_desde_archivo(archivo)

        elif eleccion == '8':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
