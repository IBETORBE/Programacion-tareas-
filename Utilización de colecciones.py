class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', categoria='{self.categoria}', isbn='{self.isbn}')"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __repr__(self):
        return f"Usuario(nombre='{self.nombre}', id_usuario='{self.id_usuario}', libros_prestados={self.libros_prestados})"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # ISBN como clave, Libro como valor
        self.usuarios = {}  # ID de usuario como clave, Usuario como valor

    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"No se encontró el libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")

    def prestar_libro(self, isbn, id_usuario):
        if isbn not in self.libros:
            print(f"No se encontró el libro con ISBN {isbn}.")
            return
        if id_usuario not in self.usuarios:
            print(f"No se encontró el usuario con ID {id_usuario}.")
            return

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]

        if libro in usuario.libros_prestados:
            print(f"El libro '{libro.titulo}' ya está prestado al usuario '{usuario.nombre}'.")
        else:
            usuario.libros_prestados.append(libro)
            print(f"Libro '{libro.titulo}' prestado a '{usuario.nombre}'.")

    def devolver_libro(self, isbn, id_usuario):
        if id_usuario not in self.usuarios:
            print(f"No se encontró el usuario con ID {id_usuario}.")
            return
        usuario = self.usuarios[id_usuario]

        libro_a_devolver = None
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                libro_a_devolver = libro
                break

        if libro_a_devolver is None:
            print(f"El libro con ISBN {isbn} no está prestado al usuario con ID {id_usuario}.")
            return

        usuario.libros_prestados.remove(libro_a_devolver)
        print(f"Libro '{libro_a_devolver.titulo}' devuelto por '{usuario.nombre}'.")

    def buscar_libro(self, **kwargs):
        resultados = []
        for libro in self.libros.values():
            match = True
            for key, value in kwargs.items():
                if not getattr(libro, key, None) == value:
                    match = False
                    break
            if match:
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario not in self.usuarios:
            print(f"No se encontró el usuario con ID {id_usuario}.")
            return
        usuario = self.usuarios[id_usuario]
        return usuario.libros_prestados


# Ejemplo de uso del sistema de biblioteca

# Crear la biblioteca
biblioteca = Biblioteca()

# Añadir libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "978-3-16-148410-0")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela", "978-84-376-0494-7")
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Juan Pérez", "U001")
usuario2 = Usuario("Ana López", "U002")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("978-3-16-148410-0", "U001")

# Devolver libros
biblioteca.devolver_libro("978-3-16-148410-0", "U001")

# Buscar libros
resultados_busqueda = biblioteca.buscar_libro(titulo="Don Quijote de la Mancha")
print("Resultados de búsqueda:", resultados_busqueda)

# Listar libros prestados
prestados = biblioteca.listar_libros_prestados("U001")
print("Libros prestados a U001:", prestados)
