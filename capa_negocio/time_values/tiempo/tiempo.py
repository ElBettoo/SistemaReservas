from capa_negocio.time_values.tiempo.hora import Hora
from capa_negocio.time_values.tiempo.minuto import Minuto
from capa_negocio.time_values.tiempo.segundo import Segundo

class Tiempo:
    def __init__(self, hora: Hora, minuto: Minuto, segundo: Segundo):
        self.__hora = Hora(hora)
        self.__minuto = Minuto(minuto)
        self.__segundo = Segundo(segundo)

    def __eq__(self, otro: "Tiempo"):
        return (self.__hora == otro.__hora and self.__minuto == otro.__minuto and self.__segundo == otro.__segundo)

    def __gt__(self, otro: "Tiempo"):
        return (self.__hora > otro.__hora) or (self.__hora == otro.__hora and self.__minuto > otro.__minuto) or (self.__hora == otro.__hora and self.__minuto == otro.__minuto and self.__segundo > otro.__segundo)

    def __lt__(self, otro: "Tiempo"):
        return (self.__hora < otro.__hora) or (self.__hora == otro.__hora and self.__minuto < otro.__minuto) or (self.__hora == otro.__hora and self.__minuto == otro.__minuto and self.__segundo < otro.__segundo)
    
    @property
    def expresion(self):
        return f"{self.__hora.expresion}:{self.__minuto.expresion}:{self.__segundo.expresion}"