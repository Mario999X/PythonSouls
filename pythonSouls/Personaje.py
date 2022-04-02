class Personaje:

    def __init__(self, nombre="", salud=0, aquellus=0, carga_arma=0, damage=0):
        self.__nombre = nombre
        self.__salud = salud
        self.__aquellus = aquellus
        self.__carga_arma = carga_arma
        self.__damage = damage

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, n):
        self.__nombre = n

    @property
    def salud(self):
        return self.__salud

    @salud.setter
    def salud(self, s):
        self.__salud = s

    @property
    def aquellus(self):
        return self.__aquellus

    @aquellus.setter
    def aquellus(self, a):
        self.__aquellus = a

    @property
    def carga_arma(self):
        return self.__carga_arma

    @carga_arma.setter
    def carga_arma(self, ca):
        self.__carga_arma = ca

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, d):
        self.__damage = d
