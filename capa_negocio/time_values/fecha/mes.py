from capa_negocio.time_values.time_value import TimeValue
from capa_negocio.excepciones import *

class Mes(TimeValue):
    def __init__(self, value):
        MIN_MES = 1
        MAX_MES = 12
        self.__value = value
        super().__init__(value)
        self.check_value(MIN_MES, MAX_MES)

    def check_value(self, min_value, max_value):
        if self.__value < min_value or self.__value > max_value:
            raise MesInvalido