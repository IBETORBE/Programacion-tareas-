import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import datetime

# Función para agregar un nuevo evento
def agregar_evento():
    fecha = fecha_entry.get()
    hora = hora_entry.get()
    descripcion = descripcion_entry.get()

    # Validar que no estén vacíos los campos
    if not fecha or not hora or not descripcion:
        messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
        return

    # Agregar los datos a la TreeView
    eventos_tree.insert("", "end", values=(fecha, hora, descripcion))

    # Limpiar los campos de entrada
    fecha_entry.set_date(datetime.date.today())
    hora_entry.delete(0, tk.END)
    descripcion_entry.delete(0, tk.END)

# Función para eliminar un evento seleccionado
def eliminar_evento():
    seleccion = eventos_tree.selection()
    if not seleccion:
        messagebox.showwarning("Selección", "Selecciona un evento para eliminar.")
        return

    confirmacion = messagebox.askyesno("Confirmación", "¿Estás seguro de eliminar este evento?")
    if confirmacion:
        eventos_tree.delete(seleccion)

# Función para cerrar la aplicación
def salir():
    ventana.destroy()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("500x400")

# Crear el contenedor para los campos de entrada
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

# Etiquetas y entradas para la fecha, hora y descripción
tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=10, pady=5)
fecha_entry = DateEntry(frame_entrada, width=15, background='darkblue', foreground='white', date_pattern='yyyy-mm-dd')
fecha_entry.grid(row=0, column=1, padx=10, pady=5)
fecha_entry.set_date(datetime.date.today())

tk.Label(frame_entrada, text="Hora (HH:MM):").grid(row=1, column=0, padx=10, pady=5)
hora_entry = tk.Entry(frame_entrada, width=15)
hora_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=10, pady=5)
descripcion_entry = tk.Entry(frame_entrada, width=40)
descripcion_entry.grid(row=2, column=1, padx=10, pady=5)

# Botones para agregar y eliminar eventos
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

agregar_boton = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
agregar_boton.grid(row=0, column=0, padx=10)

eliminar_boton = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
eliminar_boton.grid(row=0, column=1, padx=10)

salir_boton = tk.Button(frame_botones, text="Salir", command=salir)
salir_boton.grid(row=0, column=2, padx=10)

# Tabla para mostrar los eventos
eventos_tree = ttk.Treeview(ventana, columns=("Fecha", "Hora", "Descripción"), show="headings", height=10)
eventos_tree.pack(pady=10)

eventos_tree.heading("Fecha", text="Fecha")
eventos_tree.heading("Hora", text="Hora")
eventos_tree.heading("Descripción", text="Descripción")

eventos_tree.column("Fecha", width=100)
eventos_tree.column("Hora", width=100)
eventos_tree.column("Descripción", width=250)

# Iniciar el loop de la aplicación
ventana.mainloop()
