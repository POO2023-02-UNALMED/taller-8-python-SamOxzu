class Persona:
    def __init__(self, nombre, edad, altura, sexo):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.sexo = sexo

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura

    def get_sexo(self):
        return self.__sexo

    def set_sexo(self, sexo):
        self.__sexo = sexo
