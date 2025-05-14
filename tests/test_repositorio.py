import pytest
from src.repositorio import RepositorioProcesos
from src.proceso import Proceso

def test_agregar_y_listar():
    repo = RepositorioProcesos()
    p1 = Proceso("X", 3, 1)
    repo.agregar(p1)
    assert repo.listar() == [p1]

def test_pid_duplicado():
    repo = RepositorioProcesos()
    repo.agregar(Proceso("Y", 2, 1))
    with pytest.raises(ValueError):
        repo.agregar(Proceso("Y", 4, 2))
