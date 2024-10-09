from capa_negocio.time_values.time_value import TimeValue
from capa_negocio.excepciones import *

class Dia(TimeValue):
    def __init__(self, value):
        MIN_DIA = 1
        MAX_DIA = 31
        super().__init__(value)
        self.__value = value
        self.check_value(MIN_DIA, MAX_DIA)

    def check_value(self, min_value, max_value):
        if self.__value < min_value or self.__value > max_value:
            raise DiaInvalido