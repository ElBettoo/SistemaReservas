from capa_negocio.time_values.time_value import TimeValue
from capa_negocio.excepciones import *

class Segundo(TimeValue):
    def __init__(self, value):
        MIN_SEGUNDO = 0
        MAX_SEGUNDO = 59
        super().__init__(value)
        self.__value = value
        self.check_value(MIN_SEGUNDO, MAX_SEGUNDO)

    def check_value(self, min_value, max_value):
        if self.__value < min_value or self.__value > max_value:
            raise SegundoInvalido