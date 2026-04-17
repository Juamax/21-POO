from dominio.mazo import Mazo
from dominio.jugador import Jugador
from dominio.crupier import Crupier
from ui.consola import Consola

class Juego:

    def __init__(self):
        self.__mazo = Mazo()
        self.__jugador = Jugador("Jugador")
        self.__crupier = Crupier()
        self.__ui = Consola()
        self.__activo = True
        self.__objetos = [self.__mazo, self.__jugador, self.__crupier]

    def ejecutar(self):
        self.__iniciar()
        while self.__activo:
            self.__turno_jugador()
            self.__turno_crupier()
            self.__determinar_ganador()
            self.__activo = False

    def __iniciar(self):
        for _ in range(2):
            self.__jugador.agregar_carta(self.__mazo.robar_carta())
            self.__crupier.agregar_carta(self.__mazo.robar_carta())
        self.__actualizar_objetos()

    def __turno_jugador(self):
        while True:
            self.__ui.mostrar_mano(self.__crupier)
            self.__ui.mostrar_mano(self.__jugador)

            if self.__jugador.valor_mano() > 21:
                return

            opcion = self.__ui.pedir_accion()

            if opcion == "p":
                self.__jugador.agregar_carta(self.__mazo.robar_carta())
                self.__actualizar_objetos()
            else:
                return

    def __turno_crupier(self):
        while self.__crupier.debe_pedir():
            self.__crupier.agregar_carta(self.__mazo.robar_carta())
            self.__actualizar_objetos()

    def __determinar_ganador(self):
        self.__ui.mostrar_resultado(self.__jugador, self.__crupier)

    def __actualizar_objetos(self):
        for objeto in self.__objetos:
            objeto.actualizar()