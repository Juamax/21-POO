from dominio.objeto_juego import ObjetoJuego
from dominio.mano import Mano

class Jugador(ObjetoJuego):

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__mano = Mano()

    def agregar_carta(self, carta):
        self.__mano.agregar_carta(carta)

    def valor_mano(self):
        return self.__mano.valor()

    def cartas(self):
        return self.__mano.cartas()

    def nombre(self):
        return self.__nombre

    def actualizar(self):
        pass

    def estado(self):
        return (self.__nombre, self.valor_mano())