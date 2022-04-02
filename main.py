import pythonSouls.Palacio as Ar
import pythonSouls.Introduccion as Intro

intro = Intro.Introduccion()
palacio = Ar.Palacio()


def main():
    print("¡BIENVENIDO a PythonSouls!")
    salir_juego = False
    while not salir_juego:
        teclado_inicial = int(input("""
        0. Salir
        1. Modo Introducción
        2. Modo Palacio
        3. Modo Desafío (Proximamente)
        Opción: """))
        if teclado_inicial == 0:
            print("¡Gracias por jugar!")
            salir_juego = True
        elif teclado_inicial == 1:
            print("\nINICIANDO INTRODUCCION... \n")
            intro.preparar_introduccion()
        elif teclado_inicial == 2:
            print("\nINICIANDO ASEDIO... \n")
            palacio.preparar_palacio()
        elif teclado_inicial == 3:
            print("Proximamente")
        else:
            print("Opción incorrecta \n")


if __name__ == '__main__':
    main()
