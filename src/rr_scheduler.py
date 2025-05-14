from src.scheduler import Scheduler
from collections import deque

class RoundRobinScheduler(Scheduler):
    def __init__(self, quantum):
        self.quantum = quantum

    def planificar(self, procesos):
        tiempo_actual = 0
        gantt = []
        cola = deque(procesos)

        for p in cola:
            p.tiempo_restante = p.duracion

        while cola:
            p = cola.popleft()
            if p.tiempo_inicio is None:
                p.tiempo_inicio = tiempo_actual

            tiempo_ejec = min(self.quantum, p.tiempo_restante)
            p.tiempo_restante -= tiempo_ejec
            tiempo_actual += tiempo_ejec
            gantt.append((p.pid, tiempo_actual - tiempo_ejec, tiempo_actual))

            if p.tiempo_restante > 0:
                cola.append(p)
            else:
                p.tiempo_fin = tiempo_actual

        return gantt
