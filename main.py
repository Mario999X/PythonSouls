import pythonSouls.palacio as ar

juego = ar.Palacio()


def main():
    print("¡BIENVENIDO a PythonSouls!")
    salir_juego = False
    while not salir_juego:
        teclado_inicial = int(input("""
        0. Salir
        1. Jugar: Historia
        Opción: """))
        if teclado_inicial == 0:
            print("¡Gracias por jugar, nos vemos!")
            salir_juego = True
        elif teclado_inicial == 1:
            print("\nINICIANDO ASEDIO... \n")
            juego.preparar_palacio()
        else:
            print("Opción incorrecta \n")


if __name__ == '__main__':
    main()
