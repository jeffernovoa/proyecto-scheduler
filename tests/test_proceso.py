import pytest
from src.proceso import Proceso

def test_proceso_valido():
    p = Proceso("P1", 5, 1)
    assert p.pid == "P1"
    assert p.duracion == 5
    assert p.prioridad == 1
    assert p.tiempo_restante == 5

def test_proceso_duracion_invalida():
    with pytest.raises(ValueError):
        Proceso("P2", 0, 1)

def test_proceso_pid_vacio():
    with pytest.raises(ValueError):
        Proceso("", 5, 1)