from capa_negocio.time_values.time_value import TimeValue
from capa_negocio.excepciones import *

class Hora(TimeValue):
    def __init__(self, value):
        MIN_HORA = 0
        MAX_HORA = 23
        super().__init__(value)
        self.__value = value
        self.check_value(MIN_HORA, MAX_HORA)

    def check_value(self, min_value, max_value):
        if self.__value < min_value or self.__value > max_value:
            raise HoraInvalido