from capa_negocio.time_values.time_value import TimeValue
from capa_negocio.excepciones import *

class Ano(TimeValue):
    def __init__(self, value):
        MIN_ANO = 2020
        MAX_ANO = 2030
        super().__init__(value)
        self.__value = value
        self.check_value(MIN_ANO, MAX_ANO)

    def check_value(self, min_value, max_value):
        if self.__value < min_value or self.__value > max_value:
            raise AnoInvalido