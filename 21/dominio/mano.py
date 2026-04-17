from dominio.objeto_juego import ObjetoJuego

class Mano(ObjetoJuego):

    def __init__(self):
        self.__cartas = []

    def agregar_carta(self, carta):
        self.__cartas.append(carta)

    def valor(self):
        total = sum(c.obtener_puntos() for c in self.__cartas)

        ases = sum(1 for c in self.__cartas if c.obtener_puntos() == 11)

        while total > 21 and ases:
            total -= 10
            ases -= 1

        return total

    def cartas(self):
        return list(self.__cartas)

    def actualizar(self):
        pass

    def estado(self):
        return self.valor()