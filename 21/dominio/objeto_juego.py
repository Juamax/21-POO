from abc import ABC, abstractmethod

class ObjetoJuego(ABC):

    @abstractmethod
    def actualizar(self):
        pass

    @abstractmethod
    def estado(self):
        pass