from deportista import Deportista
from persona import Persona

class Futbolista(Deportista):
    lista_futbolistas = []

    # "Juan Pablo", 30, "1,80", "M", 12, 400, 1, "Derecha"
    def __init__(self, nombre, edad, altura, sexo, años_practicando, goles_marcados, tarjetas_rojas, pierna_habil):
        super().__init__(nombre, edad, altura, sexo, "Futbol", años_practicando)
        self.goles_marcados = goles_marcados
        self.tarjetas_rojas = tarjetas_rojas
        self.pierna_habil = pierna_habil

    def get_goles_marcados(self):
        return self.goles_marcados

    def set_goles_marcados(self, goles_marcados):
        self.goles_marcados = goles_marcados

    def get_tarjetas_rojas(self):
        return self.tarjetas_rojas

    def set_tarjetas_rojas(self, tarjetas_rojas):
        self.tarjetas_rojas = tarjetas_rojas

    def get_pierna_habil(self):
        return self.pierna_habil

    def set_pierna_habil(self, pierna_habil):
        self.pierna_habil = pierna_habil

    def __str__(self):
        return f"Mi nombre es {self.get_nombre()} soy profesional en el deporte {self.get_deporte()}. Tengo {self.get_edad()} años de edad y llevo {self.get_años_practicando()} años en el deporte."
