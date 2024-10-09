from abc import ABC, abstractmethod
from capa_negocio.excepciones import InvalidOperation

class TimeValue(ABC):
    def __init__(self, value):
        self.__value = value
        
    @abstractmethod
    def check_value(min_value, max_value):
        pass

    @property
    def expresion(self):
        return str(self.__value).zfill(2)

    def __eq__(self, otro: "TimeValue"):
        if not isinstance(otro, self.__class__):
            raise InvalidOperation(f"Invalid operation. type '{self.__class__}' against '{otro.__class__}'")
        return self.__value == otro.__value

    def __gt__(self, otro: "TimeValue"):
        if not isinstance(otro, self.__class__):
            raise InvalidOperation(f"Invalid operation. type '{self.__class__}' against '{otro.__class__}'")
        return self.__value > otro.__value
    
    def __lt__(self, otro: "TimeValue"):
        if not isinstance(otro, self.__class__):
            raise InvalidOperation(f"Invalid operation. type '{self.__class__}' against '{otro.__class__}'")
        return self.__value < otro.__value