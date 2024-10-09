from capa_negocio.sala import Sala
from capa_negocio.date_time import DateTime
from capa_negocio.time_values.fecha.fecha import Fecha
from capa_negocio.excepciones import SalaNoExistente, ReservaInvalida, SalaOcupada
from capa_negocio.reserva import Reserva

class GestionReserva:
    __instance = None

    def __new__(self):
        if not self.__instance:
            self.__instance = super().__new__(self)
            self.__salas: dict = {Sala("Sala 1", 10): [], Sala("Sala 2", 2): []}
        return self.__instance        
    
    def get_salas_disponibles(self):
        return self.__salas.keys()
    
    def get_reservas_de_sala(self, sala_name):
        sala = self.__get_sala_por_nombre(sala_name)
        return [reserva for reserva in self.__salas[sala]]
    
    def cancelar_reserva(self, sala_name, reserva_index):
        sala = self.__get_sala_por_nombre(sala_name)
        self.__salas[sala].pop(reserva_index)

    def get_reservas(self):
        return self.__salas.copy()

    def get_reservas_activas_por_fecha(self, full_time: DateTime):
        reservas_activas = []
        fecha = full_time._DateTime__fecha  

        for reservas_de_salas in self.__salas.values():
            reservas_activas += [reserva for reserva in reservas_de_salas if reserva.is_activa_en_fecha(fecha)]

        return reservas_activas

    def generar_reserva(self, sala_name: str, inicio: DateTime, final: DateTime):
        sala = self.__get_sala_por_nombre(sala_name)

        if inicio >= final:
            raise ReservaInvalida
        
        new_reserva = Reserva(sala, inicio, final)
        if not self.is_reserva_posible(new_reserva):
            raise SalaOcupada
        
        self.__salas[sala].append(new_reserva)

    def is_reserva_posible(self, new_reserva: Reserva):
        for reservas_de_salas in self.__salas.values():
            return not any([reserva for reserva in reservas_de_salas if reserva.interfiere_con(new_reserva)])

    def __get_sala_por_nombre(self, sala_name):
        for sala in self.__salas.keys():
            if sala == sala_name:
                return sala
        raise SalaNoExistente