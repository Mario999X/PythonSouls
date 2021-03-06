import pythonSouls.Personaje as Per
import pythonSouls.Operaciones as Op
import random


class Palacio:
    def preparar_palacio(self):
        # PREPARACION JUGADOR
        jugador = Per.Personaje()
        jugador.nombre = input("Introduce el nombre del Usurpador: ")
        jugador.salud = 130
        jugador.aquellus = 4
        jugador.carga_arma = 7
        jugador.damage = 10

        # PREPARACION ENEMIGOS
        # NOMBRE, SALUD BASE, AQUELLUS, CARGA INICIAL, DAÑO BASE
        enemigo_uno = Per.Personaje("Ansgot, El devoto", 150, 2, 5, 7)
        boss = Per.Personaje("Alysys, Reina de Pandora", 200, 3, 7, 17)

        # PREPARACION DIALOGOS
        # DIALOGOS ACCIONES
        guiones_separacion = "-------------------------"
        guiones_sep_jugador = "------------ DETALLES USURPADOR -------------"
        guiones_sep_jug_accion = "------------ ACCIÓN USURPADOR -------------"
        guiones_sep_enemigo = "------------ DETALLES ENEMIGO -------------"
        guiones_sep_ene_accion = "------------ ACCIÓN ENEMIGO -------------"
        golpe_rapido_acierto = "¡GOLPE DIRECTO!"
        minimo_cargas_jugador = "Necesitás el mínimo de cargas para lanzar un ataque especial. | Perdiste un turno"
        minimo_cargas_enemigo = "El rival no tiene las cargas mínimas para lanzar un ataque especial: "
        menu_jugador = """
        --- TURNO JUGADOR ---
        0.Rendirse
        1.Espada - Ataque rápido (+ 2 cargas)
        2.Espada - Ataque Especial (Mínimo 10 cargas + 10 daño adicional)
        3.Escudo - Defensa básica (Frente ataques rápidos)
        4.Escudo - Defensa específica (Frente ataques especiales, en caso de detener uno, -3 de salud)
        5.Aquellus - Curación (+ 50 salud)
        Opción: """
        frase_huida_jugador = "El Usurpador huye del combate"
        frase_derrota_jugador = "--- NO HAS CUMPLIDO TÚ OBJETIVO ---"
        voz_desconocida = "...siempre puedes volver a intentarlo, Usurpador..."
        frase_win = "--- ENHORABUENA, TE HICISTE CON EL PODER... ---"
        # DIALOGOS ENEMIGOS
        enemigo_uno_intro = enemigo_uno.nombre + ": Asi que TÚ eres el intruso... me decepcionas " + jugador.nombre + ", tendre que poner fin a tu miserable existencia."
        enemigo_uno_sorpresa = enemigo_uno.nombre + ": ¿Qué? ¡Imposible!"
        enemigo_uno_muerte = enemigo_uno.nombre + ": Toda una vida en tinieblas, nunca más..."
        boss_intro = boss.nombre + ": Al final has aparecido para ver a tu querida hermana... siento decepcionarte pero estos últimos 5 años me he estado preparando para este momento, ¡en guardia! "
        boss_sorpresa = boss.nombre + ": Vaya... nunca imagine que fueras tan fuerte... ¡Da igual, no pienso dejar que ganes esta batalla!"
        boss_muerte = boss.nombre + ": Nunca debiste perturbar la paz de Pandora " + jugador.nombre + "... solo eres una marioneta... "

        print(guiones_separacion)
        print("--- ¡ATENCIÓN, SE HA DETECTADO A UN INTRUSO EN EL PALACIO! ---")
        print(guiones_separacion)

        # BUCLE GAMEPLAY
        fin_partida: bool = False
        print("""--- Características Usurpador ---
-Salud Actual: """ + str(jugador.salud) + "\n-Aquellus en posesión: " + str(
            jugador.aquellus) + "\n-Cargas Usurpador: " + str(jugador.carga_arma) + "\n-Daño Base: " + str(
            jugador.damage))
        print(guiones_separacion)
        print("Primer obstáculo: " + enemigo_uno.nombre)
        print("\n" + enemigo_uno_intro)
        print(guiones_separacion)
        print("""--- Análisis del enemigo --- 
-Salud Actual: """ + str(enemigo_uno.salud) + "\n-Aquellus en poder: " + str(
            enemigo_uno.aquellus) + "\n-Cargas enemigo: " + str(enemigo_uno.carga_arma) + "\n-Daño Base: " + str(
            enemigo_uno.damage))
        while not fin_partida:

            enfrentamiento = 1
            # ENFRENTAMIENTO 1
            while enfrentamiento == 1 and jugador.salud > 0:
                # TURNO DEL JUGADOR
                print(guiones_separacion)
                movimiento_jugador = int(input(menu_jugador))
                print(guiones_sep_jugador)
                print("- Salud Usurpador: " + str(jugador.salud))
                print("- Cargas Usurpador: " + str(jugador.carga_arma))
                print("- Aquellus Restantes: " + str(jugador.aquellus))
                print("- Daño Usurpador: " + str(jugador.damage))
                print(guiones_sep_jug_accion)
                if movimiento_jugador == 0:
                    print(frase_huida_jugador)
                    enfrentamiento = 0
                elif movimiento_jugador == 1:
                    enemigo_uno.salud = Op.resta_salud(enemigo_uno.salud, jugador.damage)
                    print(golpe_rapido_acierto)
                    print("Salud Rival: " + str(enemigo_uno.salud))
                    jugador.carga_arma = Op.suma_carga(jugador.carga_arma)
                elif movimiento_jugador == 2:
                    if jugador.carga_arma < 10:
                        print(minimo_cargas_jugador)
                    else:
                        enemigo_uno.salud = Op.resta_salud_carga_jugador(enemigo_uno.salud, jugador.carga_arma)
                        print(
                            "¡Lanzaste un ataque especial de carga: " + str(
                                jugador.carga_arma) + "!")
                        print("Salud Rival: " + str(enemigo_uno.salud))
                        print("Tú carga se reinició a 5")
                        jugador.carga_arma = 5
                elif movimiento_jugador == 3:
                    print("¡Preparas tu defensa frente ataques rápidos!")
                elif movimiento_jugador == 4:
                    print("¡Preparas tu defensa frente ataques especiales!")
                elif movimiento_jugador == 5:
                    if jugador.aquellus == 0:
                        print("No te quedan Aquellus | Perdiste un turno")
                    else:
                        jugador.salud = Op.suma_salud_jugador(jugador.salud)
                        jugador.aquellus = Op.resta_aquellus(jugador.aquellus)
                        print("Recuperaste salud | Aquellus restantes: " + str(jugador.aquellus))
                        print("Salud Actual: " + str(jugador.salud))
                else:
                    print("Escoge una opción válida")
                    continue
                    # COMPROBACION DEL ESTADO DE LA BATALLA
                if enemigo_uno.salud <= 0:
                    print(guiones_separacion)
                    print(enemigo_uno_muerte)
                    print("¡Derrotaste a: " + enemigo_uno.nombre + "!")
                    jugador.damage = jugador.damage + 5
                    print("¡Ganas 5 de daño!: " + str(jugador.damage) + " Daño total.")
                    jugador.salud = jugador.salud + 40
                    print("¡Ganas 40 de salud!: " + str(jugador.salud) + " Salud Actual.")
                    jugador.carga_arma = Op.resta_carga(jugador.carga_arma)
                    print(guiones_separacion)
                    print("Obstáculo Final: " + boss.nombre)
                    print(boss_intro)
                    print(guiones_separacion)
                    print("--- Análisis del enemigo ---")
                    print("-Salud Actual: " + str(boss.salud) + "\n-Aquellus en poder: " + str(
                        boss.aquellus) + "\n-Cargas enemigo: " + str(boss.carga_arma) + "\n-Daño Base: " + str(
                        boss.damage))
                    enfrentamiento = enfrentamiento + 1
                    break
                    # TURNO DEL RIVAL IA
                if movimiento_jugador >= 1:
                    print(guiones_sep_enemigo)
                    print("- Salud Rival: " + str(enemigo_uno.salud))
                    print("- Cargas Rival: " + str(enemigo_uno.carga_arma))
                    print("- Aquellus Restantes: " + str(enemigo_uno.aquellus))
                    print("- Daño Rival: " + str(enemigo_uno.damage))
                    print(guiones_sep_ene_accion)
                    movimiento_ia = random.randint(1, 3)
                    if movimiento_ia == 1:
                        if movimiento_jugador == 3:
                            print("¡El usurpador se cubrió el golpe!")
                            enemigo_uno.carga_arma = Op.suma_carga(enemigo_uno.carga_arma)
                        else:
                            jugador.salud = Op.resta_salud(jugador.salud, enemigo_uno.damage)
                            print(golpe_rapido_acierto + "\nSalud del Usurpador: " + str(jugador.salud))
                            enemigo_uno.carga_arma = Op.suma_carga(enemigo_uno.carga_arma)
                    elif movimiento_ia == 2:
                        if enemigo_uno.carga_arma < 9:
                            enemigo_uno.carga_arma = Op.suma_carga(enemigo_uno.carga_arma)
                            print(minimo_cargas_enemigo + str(
                                enemigo_uno.carga_arma))
                            print("El Usurpador observa.")
                        else:
                            if movimiento_jugador == 4:
                                print("¡El Usurpador usó todas sus fuerzas para bloquear el golpe!")
                                jugador.salud = Op.proteccion_especial(jugador.salud)
                                print("La carga del enemigo se reinició a 5")
                                print(enemigo_uno_sorpresa)
                                enemigo_uno.carga_arma = 5
                            else:
                                jugador.salud = Op.resta_salud_carga_enemigo(jugador.salud, enemigo_uno.carga_arma)
                                print("¡El rival lanzó un ataque especial!")
                                print("Salud del usurpador: " + str(jugador.salud))
                                print("La carga del enemigo se reinició a 5")
                                enemigo_uno.carga_arma = 5
                    elif movimiento_ia == 3:
                        if enemigo_uno.aquellus == 0:
                            print("¡Al rival no le quedan Aquellus! | Perdió un turno")
                            print("El Usurpador observa.")
                        else:
                            enemigo_uno.salud = Op.suma_salud_enemigo(enemigo_uno.salud)
                            enemigo_uno.aquellus = Op.resta_aquellus(enemigo_uno.aquellus)
                            print("¡El rival recuperó salud!\nSalud actual: " + str(enemigo_uno.salud))
                            print("Aquellus restantes: " + str(enemigo_uno.aquellus))
            # ENFRENTAMIENTO FINAL
            while enfrentamiento == 2 and jugador.salud > 0:
                # TURNO DEL JUGADOR
                movimiento_jugador = int(input(menu_jugador))
                print(guiones_sep_jugador)
                print("- Salud Usurpador: " + str(jugador.salud))
                print("- Cargas Usurpador: " + str(jugador.carga_arma))
                print("- Aquellus Restantes: " + str(jugador.aquellus))
                print("- Daño Usurpador: " + str(jugador.damage))
                print(guiones_sep_jug_accion)
                if movimiento_jugador == 0:
                    print(frase_huida_jugador)
                    enfrentamiento = 0
                elif movimiento_jugador == 1:
                    boss.salud = Op.resta_salud(boss.salud, jugador.damage)
                    print(golpe_rapido_acierto)
                    print("Salud Rival: " + str(boss.salud))
                    jugador.carga_arma = Op.suma_carga(jugador.carga_arma)
                elif movimiento_jugador == 2:
                    if jugador.carga_arma < 10:
                        print(minimo_cargas_jugador)
                    else:
                        boss.salud = Op.resta_salud_carga_jugador(boss.salud, jugador.carga_arma)
                        print(
                            "¡Lanzaste un ataque especial de carga: " + str(jugador.carga_arma) + "!")
                        print("Salud Rival: " + str(boss.salud))
                        print("Tú carga se reinició a 5")
                        jugador.carga_arma = 5
                elif movimiento_jugador == 3:
                    print("¡Preparas tu defensa frente ataques rápidos!")
                elif movimiento_jugador == 4:
                    print("¡Preparas tu defensa frente ataques especiales!")
                elif movimiento_jugador == 5:
                    if jugador.aquellus == 0:
                        print("No te quedan Aquellus | Perdiste un turno")
                    else:
                        jugador.salud = Op.suma_salud_jugador(jugador.salud)
                        jugador.aquellus = Op.resta_aquellus(jugador.aquellus)
                        print("Recuperaste salud | Aquellus restantes: " + str(jugador.aquellus))
                        print("Salud Actual: " + str(jugador.salud))
                else:
                    print("Escoge una opción válida")
                    continue
                    # COMPROBACION DE LA BATALLA
                if boss.salud <= 0:
                    print(guiones_separacion)
                    print(boss_muerte)
                    print("Derrotaste a: " + boss.nombre)
                    print("¿Qué será de la paz en la región Pandora?...")
                    print(guiones_separacion)
                    print(frase_win)
                    fin_partida = True
                    break
                    # TURNO DEL RIVAL IA
                if movimiento_jugador >= 1:
                    print(guiones_sep_enemigo)
                    print("- Salud Rival: " + str(boss.salud))
                    print("- Cargas Rival: " + str(boss.carga_arma))
                    print("- Aquellus Restantes: " + str(boss.aquellus))
                    print("- Daño Rival: " + str(boss.damage))
                    print(guiones_sep_ene_accion)
                    movimiento_ia = random.randint(1, 3)
                    if movimiento_ia == 1:
                        if movimiento_jugador == 3:
                            print("¡El usurpador se cubrió el golpe!")
                            boss.carga_arma = Op.suma_carga(boss.carga_arma)
                        else:
                            jugador.salud = Op.resta_salud(jugador.salud, boss.damage)
                            print(golpe_rapido_acierto + "\nSalud del usurpador: " + str(jugador.salud))
                            boss.carga_arma = Op.suma_carga(boss.carga_arma)
                    elif movimiento_ia == 2:
                        if boss.carga_arma < 9:
                            boss.carga_arma = Op.suma_carga(boss.carga_arma)
                            print(minimo_cargas_enemigo + str(boss.carga_arma))
                            print("El Usurpador observa.")
                        else:
                            if movimiento_jugador == 4:
                                print("¡El Usurpador usó todas sus fuerzas para bloquear el golpe!")
                                jugador.salud = Op.proteccion_especial(jugador.salud)
                                print("La carga del enemigo se reinició a 5")
                                print(boss_sorpresa)
                                boss.carga_arma = 5
                            else:
                                jugador.salud = Op.resta_salud_carga_enemigo(jugador.salud, boss.carga_arma)
                                print("¡El rival lanzó un ataque especial!")
                                print("Salud del Usurpador: " + str(jugador.salud))
                                print("La carga del enemigo se reinició a 5")
                                boss.carga_arma = 5
                    elif movimiento_ia == 3:
                        if boss.aquellus == 0:
                            print("¡Al rival no le quedan Aquellus! | Perdió un turno")
                            print("El Usurpador observa.")
                        else:
                            boss.salud = Op.suma_salud_enemigo(boss.salud)
                            boss.aquellus = Op.resta_aquellus(boss.aquellus)
                            print("¡El rival recuperó salud!\nSalud actual: " + str(boss.salud))
                            print("\nAquellus restantes: " + str(boss.aquellus))
            else:
                print(frase_derrota_jugador + "\n" + voz_desconocida)
                fin_partida = True
