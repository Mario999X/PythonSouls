# OPERACIONES SALUD
def resta_salud(a, b):
    return a - b


def suma_salud_jugador(a):
    return a + 50


def suma_salud_enemigo(a):
    return a + 45


def proteccion_especial(a):
    return a - 3


# OPERACIONES CARGA
def suma_carga(a):
    return a + 2


def resta_carga(a):
    return a - 2


def resta_salud_carga_jugador(a, b):
    return a - (b + 10)


def resta_salud_carga_enemigo(a, b):
    return a - (b + 5)


# OPERACIONES AQUELLUS
def resta_aquellus(a):
    return a - 1


# OPERACIONES NIVEL DESAFIO
def resta_salud_especial_desafio_jugador(a, b):
    return a - (b + 20)


def siguiente_turno(a):
    return a + 1
