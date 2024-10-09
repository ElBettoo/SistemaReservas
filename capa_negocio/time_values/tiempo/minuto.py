from capa_negocio.time_values.time_value import TimeValue
from capa_negocio.excepciones import *

class Minuto(TimeValue):
    def __init__(self, value):
        MIN_MINUTO = 0
        MAX_MINUTO = 59
        super().__init__(value)
        self.__value = value
        self.check_value(MIN_MINUTO, MAX_MINUTO)

    def check_value(self, min_value, max_value):
        if self.__value < min_value or self.__value > max_value:
            raise MinutoInvalido