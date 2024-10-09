import unittest
from date_time import DateTime
from gestion_reserva import GestionReserva
from excepciones import SalaNoExistente, SalaOcupada, ReservaInvalida

class TestGestionReserva(unittest.TestCase):
    def setUp(self):
        self.manager = GestionReserva()
        self.inicio_1 = DateTime(2024, 10, 5, 15, 00, 00)
        self.final_1 = DateTime(2024, 10, 5, 21, 00, 00)
        self.inicio_2 = DateTime(2024, 10, 5, 17, 00, 00)
        self.final_2 = DateTime(2024, 10, 5, 23, 00, 00)
        self.inicio_3 = DateTime(2024, 10, 6, 15, 00, 00)
        self.final_3 = DateTime(2024, 10, 6, 21, 00, 00)

    
    def test_01_constructor(self):
        self.assertTrue(isinstance(self.manager, GestionReserva))

    def test_02_hacer_una_reserva(self):
        self.manager.generar_reserva("Sala 1", self.inicio_1, self.final_1)
        self.assertTrue(len(self.manager.get_reservas_de_sala("Sala 1")) == 1)

    def test_03_hacer_una_reserva_devuelve_SalaNoExistente_cuando_sala_no_existe(self):
        with self.assertRaises(SalaNoExistente):
            self.manager.generar_reserva("Sala 12", self.inicio_1, self.final_1)

    def test_04_hacer_una_reserva_devuelve_ReservaInvalida_cuando_datetime_inicio_mayor_igual_a_datetime_final(self):
        with self.assertRaises(ReservaInvalida):
            self.manager.generar_reserva("Sala 1", self.final_1, self.inicio_1)

    def test_05_hacer_una_reserva_devuelve_SalaOcupada_cuando_interfiere_con_otra_reserva_creada(self):
        self.manager.generar_reserva("Sala 1", self.inicio_1, self.final_1)

        with self.assertRaises(SalaOcupada):
            self.manager.generar_reserva("Sala 1", self.inicio_2, self.final_2)

    def test_06_get_reserva_activa_por_fecha(self):
        self.manager.generar_reserva("Sala 1", self.inicio_1, self.final_1)
        self.manager.generar_reserva("Sala 1", self.inicio_3, self.final_3)

        self.assertTrue(len(self.manager.get_reservas_activas_por_fecha(self.inicio_3)) == 1)

    def test_07_cancelar_reserva(self):
        self.manager.generar_reserva("Sala 1", self.inicio_1, self.final_1)
        self.assertTrue(len(self.manager.get_reservas_de_sala("Sala 1")) == 1)

        self.manager.cancelar_reserva("Sala 1", 0)
        self.assertTrue(len(self.manager.get_reservas_de_sala("Sala 1")) == 0)

    def test_08_singleton_pattern(self):
        self.manager.generar_reserva("Sala 1", self.inicio_1, self.final_1)

        new_manager = GestionReserva()

        self.assertTrue(len(new_manager.get_reservas_de_sala("Sala 1")) == 1)
