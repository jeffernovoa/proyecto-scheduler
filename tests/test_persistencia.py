import os
from src.proceso import Proceso
from src.persistencia import guardar_json, cargar_json, guardar_csv, cargar_csv

def test_json(tmp_path):
    procesos = [Proceso("P1", 5, 1), Proceso("P2", 3, 2)]
    ruta = tmp_path / "procesos.json"
    guardar_json(ruta, procesos)
    cargados = cargar_json(ruta)
    assert len(cargados) == 2
    assert cargados[0].pid == "P1"

def test_csv(tmp_path):
    procesos = [Proceso("P1", 4, 1), Proceso("P2", 2, 2)]
    ruta = tmp_path / "procesos.csv"
    guardar_csv(ruta, procesos)
    cargados = cargar_csv(ruta)
    assert len(cargados) == 2
    assert cargados[1].duracion == 2
