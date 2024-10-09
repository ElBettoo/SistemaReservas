class AnoInvalido(Exception):
    pass

class MesInvalido(Exception):
    pass

class DiaInvalido(Exception):
    pass

class HoraInvalido(Exception):
    pass

class MinutoInvalido(Exception):
    pass

class SegundoInvalido(Exception):
    pass

class ReservaInvalida(Exception):
    pass

class SalaNoExistente(Exception):
    pass

class ReservaInvalida(Exception):
    pass

class SalaOcupada(Exception):
    pass

class InvalidOperation(Exception):
    def __init__(self, message):
        self.__message = message