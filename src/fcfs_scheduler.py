from src.scheduler import Scheduler

class FCFSScheduler(Scheduler):
    def planificar(self, procesos):
        tiempo_actual = 0
        gantt = []

        for p in procesos:
            p.tiempo_inicio = tiempo_actual
            tiempo_final = tiempo_actual + p.duracion
            p.tiempo_fin = tiempo_final
            gantt.append((p.pid, p.tiempo_inicio, p.tiempo_fin))
            tiempo_actual = tiempo_final

        return gantt
