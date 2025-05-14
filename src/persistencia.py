import json
import csv
from src.proceso import Proceso

def guardar_json(ruta, procesos):
    with open(ruta, 'w') as f:
        json.dump([p.__dict__ for p in procesos], f, indent=2)

def cargar_json(ruta):
    with open(ruta, 'r') as f:
        data = json.load(f)
        return [Proceso(**p) for p in data]

def guardar_csv(ruta, procesos):
    with open(ruta, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['pid', 'duracion', 'prioridad'])
        for p in procesos:
            writer.writerow([p.pid, p.duracion, p.prioridad])

def cargar_csv(ruta):
    procesos = []
    with open(ruta, 'r') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            procesos.append(Proceso(row['pid'], int(row['duracion']), int(row['prioridad'])))
    return procesos
