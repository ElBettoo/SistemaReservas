from capa_negocio.time_values import *

class DateTime():
    def __init__(self, ano, mes, dia, hora, minuto, segundo=0):
        self.__fecha = Fecha(ano, mes, dia)
        self.__tiempo = Tiempo(hora, minuto, segundo)

    def __eq__(self, otro: "DateTime"):
        return (self.__fecha == otro.__fecha and self.__tiempo == otro.__tiempo)

    def __gt__(self, otro: "DateTime"):
        return (self.__fecha > otro.__fecha) or (self.__fecha == otro.__fecha and self.__tiempo > otro.__tiempo) 

    def __lt__(self, otro: "DateTime"):
        return (self.__fecha < otro.__fecha) or (self.__fecha == otro.__fecha and self.__tiempo < otro.__tiempo) 
    
    def __ge__(self, otro: "DateTime"):
        return self.__gt__(otro) or self.__eq__(otro)
    
    @property
    def expresion(self):
        return f"{self.__fecha.expresion} {self.__tiempo.expresion}"

    @staticmethod
    def string_to_object(fecha_str, tiempo_str):
        ano, mes, dia = fecha_str.split("-")
        hora, minuto = tiempo_str.split(":")

        return DateTime(int(ano), int(mes), int(dia), int(hora), int(minuto))