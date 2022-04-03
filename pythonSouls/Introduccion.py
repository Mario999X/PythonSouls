import pythonSouls.Personaje as Per
import pythonSouls.Operaciones as Op


class Introduccion:
    def preparar_introduccion(self):
        # PREPARACION JUGADOR
        jugador = Per.Personaje()
        jugador.nombre = "Usurpador"
        jugador.salud = 25
        jugador.aquellus = 1
        jugador.carga_arma = 7
        jugador.damage = 5

        # PREPARACION ENEMIGO
        # NOMBRE, SALUD BASE, AQUELLUS, CARGA INICIAL, DAÑO BASE
        voz_desconocida = Per.Personaje("Espantapájaros", 75, 0, 0)

        # PREPARACION DIALOGOS
        guiones_separacion = "-------------------------"
        guiones_sep_jugador = "------------ DETALLES USURPADOR -------------"
        guiones_sep_jug_accion = "------------ ACCIÓN USURPADOR -------------"
        golpe_rapido_acierto = "¡GOLPE DIRECTO!"
        menu_jugador = """
            --- TURNO JUGADOR ---
            0.Terminar Entrenamiento
            1.Espada - Ataque rápido (+ 2 cargas)
            2.Espada - Ataque Especial (Mínimo 10 cargas + 10 daño adicional)
            3.Escudo - Defensa básica (Frente ataques rápidos)
            4.Escudo - Defensa específica (Frente ataques especiales, en caso de detener uno, -3 de salud)
            5.Aquellus - Curación (+ 50 salud)
            Opción: """

        voz_desconocida_intro = voz_desconocida.nombre + ": Hola " + jugador.nombre + ", conozco toda tu historia con " \
                                                                                      "la familia real... noto tu sed " \
                                                                                      "de sangre,\nhe decidido " \
                                                                                      "prepararte para " \
                                                                                      "tu cometido.\nMe presento en " \
                                                                                      "forma de espantapájaros para " \
                                                                                      "que entrenes usándome,\nno te " \
                                                                                      "preocupes, tus golpes no me " \
                                                                                      "harán mucho daño."
        voz_desconocida_tutorial = voz_desconocida.nombre + ": Usa las técnicas que prefieras hasta destruir este cuerpo inerte."

        voz_desconocida_tutorial_ataque_especial_fallido = voz_desconocida.nombre + ": Necesitaras un mínimo de " \
                                                                                    "cargas para lanzar un ataque " \
                                                                                    "especial. "
        voz_desconocida_tutorial_ataque_especial_acierto = voz_desconocida.nombre + ": Acertaste, esto reduce tu " \
                                                                                    "carga a 5. "

        voz_desconocida_tutorial_escudo_basico = voz_desconocida.nombre + ": Si el rival hubiera hecho un golpe " \
                                                                          "rápido, lo habrías bloqueado, recuerda, " \
                                                                          "esto evita que recibas daño, pero el " \
                                                                          "enemigo sigue recibiendo +2 a sus cargas propias."
        voz_desconocida_tutorial_escudo_especifico = voz_desconocida.nombre + ": Con esa postura habrías sido capaz " \
                                                                              "de detener un ataque especial, " \
                                                                              "aunque eso conlleva un pequeño coste " \
                                                                              "de salud, " \
                                                                              "sigue siendo mejor que recibir el " \
                                                                              "golpe entero. "
        voz_desconocida_aquellus_vacio = voz_desconocida.nombre + ": No te quedan Aquellus, son un objeto limitado, " \
                                                                  "aprovéchalos en los momentos oportunos. "
        voz_desconocida_aquellus_uso = voz_desconocida.nombre + ": Usaste un Aquellus, esa extraña poción que solo " \
                                                                "funciona en nativos de Pandora... en resumen, " \
                                                                "aumenta parcialmente tu salud. | Solo son de 1 uso. "
        voz_desconocida_despedida = voz_desconocida.nombre + ": Bien, hoy ha sido un buen entrenamiento... mañana " \
                                                             "volvere " + jugador.nombre + "..."

        print(guiones_separacion)
        print(voz_desconocida_intro)
        print(guiones_separacion)

        # BLUCLE GAMEPLAY
        fin_partida: bool = False
        print("""\n--- Características Usurpador ---
-Salud Actual: """ + str(jugador.salud) + "\n-Aquellus en posesión: " + str(
            jugador.aquellus) + "\n-Cargas Usurpador: " + str(jugador.carga_arma) + "\n-Daño Base: " + str(
            jugador.damage))
        print(guiones_separacion)
        print("\nEnemigo: " + voz_desconocida.nombre)
        print("""\n --- Análisis del enemigo --- 
-Salud Actual: """ + str(voz_desconocida.salud) + "\n-Aquellus en poder: " + str(
            voz_desconocida.aquellus) + "\n-Cargas enemigo: " + str(
            voz_desconocida.carga_arma) + "\n-Daño Base: " + str(
            voz_desconocida.damage))
        print("\n" + voz_desconocida_tutorial)
        while not fin_partida:
            enfrentamiento = 1
            while enfrentamiento == 1 and voz_desconocida.salud > 0:
                print(guiones_separacion)
                movimiento_jugador = int(input(menu_jugador))
                print(guiones_sep_jugador)
                print("- Salud Usurpador: " + str(jugador.salud))
                print("- Cargas Usurpador: " + str(jugador.carga_arma))
                print("- Aquellus Restantes: " + str(jugador.aquellus))
                print("- Daño Usurpador: " + str(jugador.damage))
                print(guiones_sep_jug_accion)
                if movimiento_jugador == 0:
                    print(voz_desconocida_despedida)
                    enfrentamiento = 0
                    fin_partida = True
                elif movimiento_jugador == 1:
                    voz_desconocida.salud = Op.resta_salud_carga_jugador(voz_desconocida.salud, jugador.damage)
                    print(golpe_rapido_acierto)
                    print("Salud Rival: " + str(voz_desconocida.salud))
                    jugador.carga_arma = Op.suma_carga(jugador.carga_arma)
                elif movimiento_jugador == 2:
                    if jugador.carga_arma < 10:
                        print(voz_desconocida_tutorial_ataque_especial_fallido)
                    else:
                        voz_desconocida.salud = Op.resta_salud(voz_desconocida.salud, jugador.carga_arma)
                        print(voz_desconocida_tutorial_ataque_especial_acierto)
                        print("Salud Rival: " + str(voz_desconocida.salud))
                        jugador.carga_arma = 5
                elif movimiento_jugador == 3:
                    print(voz_desconocida_tutorial_escudo_basico)
                elif movimiento_jugador == 4:
                    print(voz_desconocida_tutorial_escudo_especifico)
                elif movimiento_jugador == 5:
                    if jugador.aquellus == 0:
                        print(voz_desconocida_aquellus_vacio)
                    else:
                        jugador.salud = Op.suma_salud_jugador(jugador.salud)
                        jugador.aquellus = Op.resta_aquellus(jugador.aquellus)
                        print(voz_desconocida_aquellus_uso)
                else:
                    print("Escoge una opción válida.")
                    continue
                if voz_desconocida.salud <= 0:
                    print(voz_desconocida_despedida)
                    enfrentamiento = 0
                    fin_partida = True
