import pythonSouls.Palacio as Ar
import pythonSouls.Introduccion as Intro
import pythonSouls.DesafioFinal as Desa

intro = Intro.Introduccion()
palacio = Ar.Palacio()
desafio_final = Desa.Desafio_Final()

def main():
    print("¡BIENVENIDO a PythonSouls!")
    salir_juego = False
    while not salir_juego:
        teclado_inicial = int(input("""
        0. Salir
        1. Introducción
        2. Palacio
        3. Desafío
        Opción: """))
        if teclado_inicial == 0:
            print("\n¡Gracias por jugar!")
            salir_juego = True
        elif teclado_inicial == 1:
            print("\nINICIANDO INTRODUCCIÓN... \n")
            intro.preparar_introduccion()
        elif teclado_inicial == 2:
            print("\nINICIANDO ASEDIO... \n")
            palacio.preparar_palacio()
        elif teclado_inicial == 3:
            print("\nINICIANDO DESAFIO FINAL... \n")
            desafio_final.preparar_desafio_final()
        else:
            print("Opción incorrecta \n")


if __name__ == '__main__':
    main()
