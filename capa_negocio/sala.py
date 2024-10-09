class Sala():
    def __init__(self, nombre, capacidad):
        self.__nombre = nombre
        self.__capacidad = capacidad

    def __eq__(self, sala_nombre: str):
        return self.__nombre == sala_nombre
    
    def __hash__(self):
        return hash((self.__nombre, self.__capacidad))
    
    @property
    def nombre(self):
        return self.__nombre