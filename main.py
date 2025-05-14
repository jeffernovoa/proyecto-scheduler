# main.py
import tkinter as tk
from tkinter import messagebox, filedialog
from src.proceso import Proceso
from src.repositorio import RepositorioProcesos
from src.fcfs_scheduler import FCFSScheduler
from src.rr_scheduler import RoundRobinScheduler
from src.persistencia import guardar_json, cargar_json

repo = RepositorioProcesos()

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Planificador de Procesos")
        
        self.pid_var = tk.StringVar()
        self.duracion_var = tk.StringVar()
        self.prioridad_var = tk.StringVar()
        self.quantum_var = tk.StringVar(value="2")
        self.algoritmo_var = tk.StringVar(value="FCFS")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(text="PID").grid(row=0, column=0)
        tk.Entry(textvariable=self.pid_var).grid(row=0, column=1)

        tk.Label(text="Duración").grid(row=1, column=0)
        tk.Entry(textvariable=self.duracion_var).grid(row=1, column=1)

        tk.Label(text="Prioridad").grid(row=2, column=0)
        tk.Entry(textvariable=self.prioridad_var).grid(row=2, column=1)

        tk.Button(text="Agregar Proceso", command=self.agregar_proceso).grid(row=3, column=0, columnspan=2, pady=5)

        tk.Label(text="Algoritmo").grid(row=4, column=0)
        tk.OptionMenu(self.root, self.algoritmo_var, "FCFS", "RoundRobin").grid(row=4, column=1)

        tk.Label(text="Quantum").grid(row=5, column=0)
        tk.Entry(textvariable=self.quantum_var).grid(row=5, column=1)

        tk.Button(text="Simular", command=self.simular).grid(row=6, column=0, columnspan=2, pady=5)

        tk.Button(text="Guardar JSON", command=self.guardar_json).grid(row=7, column=0)
        tk.Button(text="Cargar JSON", command=self.cargar_json).grid(row=7, column=1)

        tk.Label(text="Procesos").grid(row=8, column=0, columnspan=2)
        self.lista_procesos = tk.Text(self.root, width=40, height=10)
        self.lista_procesos.grid(row=9, column=0, columnspan=2)

        tk.Label(text="Resultado").grid(row=10, column=0, columnspan=2)
        self.resultado = tk.Text(self.root, width=40, height=10)
        self.resultado.grid(row=11, column=0, columnspan=2)

    def agregar_proceso(self):
        try:
            p = Proceso(
                self.pid_var.get(),
                int(self.duracion_var.get()),
                int(self.prioridad_var.get())
            )
            repo.agregar(p)
            self.mostrar_procesos()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def mostrar_procesos(self):
        self.lista_procesos.delete("1.0", tk.END)
        for p in repo.listar():
            self.lista_procesos.insert(tk.END, f"{p.pid}: dur={p.duracion}, pri={p.prioridad}\n")

    def simular(self):
        procesos = repo.listar()
        if self.algoritmo_var.get() == "FCFS":
            scheduler = FCFSScheduler()
        else:
            scheduler = RoundRobinScheduler(int(self.quantum_var.get()))

        gantt = scheduler.planificar(procesos)

        salida = "Gantt:\n"
        for pid, inicio, fin in gantt:
            salida += f"{pid}: {inicio} -> {fin}\n"

        n = len(procesos)
        total_espera = sum(p.tiempo_espera() for p in procesos)
        total_respuesta = sum(p.tiempo_respuesta() for p in procesos)
        total_retorno = sum(p.tiempo_retorno() for p in procesos)

        salida += f"\nMedia espera: {total_espera/n:.2f}\n"
        salida += f"Media respuesta: {total_respuesta/n:.2f}\n"
        salida += f"Media retorno: {total_retorno/n:.2f}\n"

        self.resultado.delete("1.0", tk.END)
        self.resultado.insert(tk.END, salida)

    def guardar_json(self):
        ruta = filedialog.asksaveasfilename(defaultextension=".json")
        if ruta:
            guardar_json(ruta, repo.listar())

    def cargar_json(self):
        ruta = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if ruta:
            procesos = cargar_json(ruta)
            repo.reemplazar(procesos)
            self.mostrar_procesos()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
