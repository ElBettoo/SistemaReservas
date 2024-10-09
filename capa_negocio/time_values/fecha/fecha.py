from capa_negocio.time_values.fecha.ano import Ano
from capa_negocio.time_values.fecha.mes import Mes
from capa_negocio.time_values.fecha.dia import Dia

class Fecha:
    def __init__(self, ano: Ano, mes: Mes, dia: Dia):
        self.__ano = Ano(ano)
        self.__mes = Mes(mes)
        self.__dia = Dia(dia)

    def __eq__(self, otro: "Fecha"):
        return (self.__ano == otro.__ano and self.__mes == otro.__mes and self.__dia == otro.__dia)

    def __gt__(self, otro: "Fecha"):
        return (self.__ano > otro.__ano) or (self.__ano == otro.__ano and self.__mes > otro.__mes) or (self.__ano == otro.__ano and self.__mes == otro.__mes and self.__dia > otro.__dia)

    def __lt__(self, otro: "Fecha"):
        return (self.__ano < otro.__ano) or (self.__ano == otro.__ano and self.__mes < otro.__mes) or (self.__ano == otro.__ano and self.__mes == otro.__mes and self.__dia < otro.__dia)
    
    def __ge__(self, otro: "Fecha"):
        return self.__gt__(otro) or self.__eq__(otro)
    
    @property
    def expresion(self):
        return f"{self.__ano.expresion}-{self.__mes.expresion}-{self.__dia.expresion}"