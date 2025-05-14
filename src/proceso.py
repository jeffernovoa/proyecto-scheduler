from dataclasses import dataclass

@dataclass
class Proceso:
    pid: str
    duracion: int
    prioridad: int
    tiempo_restante: int = None
    tiempo_llegada: int = 0
    tiempo_inicio: int = None
    tiempo_fin: int = None

    def __post_init__(self):
        if self.duracion <= 0:
            raise ValueError("Duración debe ser mayor a 0")
        if not self.pid:
            raise ValueError("PID no puede estar vacío")
        self.tiempo_restante = self.duracion
