import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        self.task_entry.bind('<Return>', self.add_task_event)

        # Botón para añadir tarea
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10)

        # Lista para mostrar las tareas
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.task_listbox.bind('<Double-1>', self.complete_task)

        # Botón para marcar tarea como completada
        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.grid(row=2, column=0, padx=10, pady=5)

        # Botón para eliminar tarea
        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=5)

        # Lista para guardar las tareas
        self.tasks = []

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, escribe una tarea.")

    def add_task_event(self, event):
        self.add_task()

    def complete_task(self, event=None):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            completed_task = f"[Completada] {task}"
            self.tasks[selected_task_index[0]] = completed_task
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(selected_task_index, completed_task)
        else:
            messagebox.showwarning("Ninguna tarea seleccionada", "Por favor, selecciona una tarea para marcarla como completada.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Ninguna tarea seleccionada", "Por favor, selecciona una tarea para eliminar.")

# Configuración de la ventana principal
root = tk.Tk()
app = TodoApp(root)
root.mainloop()
