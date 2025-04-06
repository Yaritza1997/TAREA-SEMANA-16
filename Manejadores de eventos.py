import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")

        self.task_list = []

        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)
        self.entry.focus()

        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.taskbox = tk.Listbox(root, width=45, height=15, selectmode=tk.SINGLE)
        self.taskbox.pack(pady=10)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.root.bind('<Return>', lambda event: self.add_task())
        self.root.bind('<c>', lambda event: self.complete_task())
        self.root.bind('<d>', lambda event: self.delete_task())
        self.root.bind('<Delete>', lambda event: self.delete_task())
        self.root.bind('<Escape>', lambda event: self.root.quit())

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.task_list.append((task, False))  # False = No completada
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía", "Por favor ingresa una tarea.")

    def complete_task(self):
        selected = self.taskbox.curselection()
        if selected:
            index = selected[0]
            task, _ = self.task_list[index]
            self.task_list[index] = (task, True)
            self.update_listbox()
        else:
            messagebox.showwarning("Sin selección", "Por favor selecciona una tarea para marcar como completada.")

    def delete_task(self):
        selected = self.taskbox.curselection()
        if selected:
            index = selected[0]
            self.task_list.pop(index)
            self.update_listbox()
        else:
            messagebox.showwarning("Sin selección", "Por favor selecciona una tarea para eliminar.")

    def update_listbox(self):
        self.taskbox.delete(0, tk.END)
        for task, completed in self.task_list:
            display_text = f"✓ {task}" if completed else task
            self.taskbox.insert(tk.END, display_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
