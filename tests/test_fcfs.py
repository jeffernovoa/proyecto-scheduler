from src.proceso import Proceso
from src.fcfs_scheduler import FCFSScheduler

def test_fcfs_basico():
    procesos = [Proceso("A", 4, 1), Proceso("B", 2, 2)]
    scheduler = FCFSScheduler()
    gantt = scheduler.planificar(procesos)

    assert gantt == [("A", 0, 4), ("B", 4, 6)]
    assert procesos[0].tiempo_inicio == 0
    assert procesos[0].tiempo_fin == 4
    assert procesos[1].tiempo_inicio == 4
    assert procesos[1].tiempo_fin == 6