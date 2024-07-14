class Archivo:
    def __init__(self, nombre):
        """
        Constructor de la clase Archivo.

        Este método se ejecuta automáticamente al crear un nuevo objeto de tipo Archivo.
        Aquí, inicializamos el nombre del archivo y abrimos el archivo.

        Args:
        - nombre: str, nombre del archivo a abrir.
        """
        self.nombre = nombre
        self.archivo = open(self.nombre, 'w')
        print(f'Se ha creado el archivo {self.nombre}')

    def escribir(self, texto):
        """
        Método para escribir en el archivo.

        Args:
        - texto: str, texto a escribir en el archivo.
        """
        self.archivo.write(texto)

    def __del__(self):
        """
        Destructor de la clase Archivo.

        Este método se ejecuta automáticamente justo antes de que el objeto sea eliminado.
        Aquí, cerramos el archivo para liberar recursos.
        """
        self.archivo.close()
        print(f'Se ha cerrado el archivo {self.nombre}')


# Ejemplo de uso del programa
if __name__ == "__main__":
    # Creamos un objeto de tipo Archivo
    archivo = Archivo('ejemplo.txt')

    # Escribimos en el archivo
    archivo.escribir('Hola, mundo!\n')
    archivo.escribir('Este es un ejemplo de archivo en Python.\n')

    # No es necesario llamar explícitamente a __del__, se llamará automáticamente al finalizar el programa.