import tkinter as tk
from tkinter import messagebox


class App:
    def __init__(self, root):
        # Configuración de la ventana principal
        self.root = root
        self.root.title("Aplicación de Gestión de Datos")

        # Crear una etiqueta
        self.label = tk.Label(root, text="Ingrese información:")
        self.label.pack(pady=10)

        # Crear un campo de texto
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        # Crear un botón "Agregar"
        self.add_button = tk.Button(root, text="Agregar", command=self.add_data)
        self.add_button.pack(pady=5)

        # Crear un botón "Limpiar"
        self.clear_button = tk.Button(root, text="Limpiar", command=self.clear_data)
        self.clear_button.pack(pady=5)

        # Crear una lista para mostrar los datos
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)

    def add_data(self):
        # Obtener el texto del campo de texto
        data = self.entry.get()

        if data:
            # Agregar el dato a la lista
            self.listbox.insert(tk.END, data)
            # Limpiar el campo de texto
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese algún dato.")

    def clear_data(self):
        # Borrar todos los datos en la lista
        self.listbox.delete(0, tk.END)
        # Limpiar el campo de texto
        self.entry.delete(0, tk.END)


# Crear la ventana principal
root = tk.Tk()

# Crear una instancia de la aplicación
app = App(root)

# Ejecutar el bucle principal
root.mainloop()
