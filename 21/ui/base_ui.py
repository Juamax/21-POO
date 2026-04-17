from abc import ABC, abstractmethod

class BaseUI(ABC):

    @abstractmethod
    def mostrar_mano(self, jugador):
        pass

    @abstractmethod
    def pedir_accion(self):
        pass

    @abstractmethod
    def mostrar_resultado(self, jugador, crupier):
        pass