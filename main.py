from src.repositorio import RepositorioProcesos
from src.fcfs_scheduler import FCFSScheduler
from src.rr_scheduler import RoundRobinScheduler
from src.simulador import calcular_metricas
from src.proceso import Proceso

repo = RepositorioProcesos()

def menu():
    while True:
        print("\n1. Agregar proceso\n2. Listar procesos\n3. Ejecutar FCFS\n4. Ejecutar Round Robin\n5. Salir")
        op = input("Opción: ")

        if op == '1':
            pid = input("PID: ")
            dur = int(input("Duración: "))
            pri = int(input("Prioridad: "))
            repo.agregar(Proceso(pid, dur, pri))

        elif op == '2':
            for p in repo.listar():
                print(p)

        elif op == '3':
            scheduler = FCFSScheduler()
            procesos = repo.listar()
            gantt = scheduler.planificar(procesos)
            print("Gantt:", gantt)
            print("Métricas:", calcular_metricas(procesos))

        elif op == '4':
            q = int(input("Quantum: "))
            scheduler = RoundRobinScheduler(q)
            procesos = repo.listar()
            gantt = scheduler.planificar(procesos)
            print("Gantt:", gantt)
            print("Métricas:", calcular_metricas(procesos))

        elif op == '5':
            break

if __name__ == "__main__":
    menu()
