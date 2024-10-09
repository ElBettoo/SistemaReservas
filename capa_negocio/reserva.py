from capa_negocio.time_values.fecha.fecha import Fecha
from capa_negocio.date_time import DateTime
from capa_negocio.sala import Sala

class Reserva:
    def __init__(self, sala: Sala, inicio: DateTime, final: DateTime):
        self.__sala = sala
        self.__inicio = inicio
        self.__final = final

    def is_activa_en_fecha(self, fecha: Fecha):
        return (self.__inicio._DateTime__fecha <= fecha) and (fecha <= self.__final._DateTime__fecha)
    
    def interfiere_con(self, otra_reserva: "Reserva"):
        salas_iguales = self.__sala == otra_reserva.__sala
        fechas_interpuestas = (self.__inicio < otra_reserva.__final) and (self.__final > otra_reserva.__inicio)

        return (salas_iguales and fechas_interpuestas)
    
    @property
    def inicio(self):
        return self.__inicio
    
    @property
    def final(self):
        return self.__final
    
    @property
    def sala(self):
        return self.__sala