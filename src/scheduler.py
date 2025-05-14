from abc import ABC, abstractmethod

class Scheduler(ABC):
    @abstractmethod
    def planificar(self, procesos):
        pass
