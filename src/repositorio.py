class RepositorioProcesos:
    def __init__(self):
        self.procesos = {}

    def agregar(self, proceso):
        if proceso.pid in self.procesos:
            raise ValueError("PID duplicado")
        self.procesos[proceso.pid] = proceso

    def eliminar(self, pid):
        del self.procesos[pid]

    def listar(self):
        return list(self.procesos.values())

    def obtener(self, pid):
        return self.procesos.get(pid)
