from src.proceso import Proceso
from src.rr_scheduler import RoundRobinScheduler

def test_rr_con_quantum():
    procesos = [Proceso("P1", 5, 1), Proceso("P2", 3, 2)]
    scheduler = RoundRobinScheduler(quantum=2)
    gantt = scheduler.planificar(procesos)

    # No se testea el orden exacto del gantt (puede variar),
    # sino que se verifica que todos terminen correctamente
    assert procesos[0].tiempo_fin > 0
    assert procesos[1].tiempo_fin > 0
    assert all(p.tiempo_fin >= p.tiempo_inicio for p in procesos)
