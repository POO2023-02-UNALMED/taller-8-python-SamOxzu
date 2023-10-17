from deportista import Deportista

class Futbolista(Deportista):
    def __init__(self, nombre, edad, altura, sexo, años_practicando, goles_marcados, tarjetas_rojas, pierna_habil):
        super().__init__(nombre, edad, altura, sexo, "Futbol", años_practicando)
        self.__goles_marcados = goles_marcados
        self.__tarjetas_rojas = tarjetas_rojas
        self.__pierna_habil = pierna_habil

    def get_goles_marcados(self):
        return self.__goles_marcados

    def set_goles_marcados(self, goles_marcados):
        self.__goles_marcados = goles_marcados

    def get_tarjetas_rojas(self):
        return self.__tarjetas_rojas

    def set_tarjetas_rojas(self, tarjetas_rojas):
        self.__tarjetas_rojas = tarjetas_rojas

    def get_pierna_habil(self):
        return self.__pierna_habil

    def set_pierna_habil(self, pierna_habil):
        self.__pierna_habil = pierna_habil
