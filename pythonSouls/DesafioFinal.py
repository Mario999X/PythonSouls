import pythonSouls.Personaje as Per
import pythonSouls.Operaciones as Op
import random


class Desafio_Final:
    def preparar_desafio_final(self):
        num_turno = 1
        # PREPARACION JUGADOR
        jugador = Per.Personaje()
        jugador.nombre = input("Introduce el nombre del Usurpador: ")
        jugador.salud = 400
        jugador.aquellus = 5
        jugador.carga_arma = 15
        jugador.damage = 21

        # PREPARACION ENEMIGO
        # NOMBRE, SALUD BASE, AQUELLUS, CARGA INICIAL, DAÑO BASE
        boss_definitivo = Per.Personaje("Lar'guug, el hijo bastardo", 1000, 7, 20, 23)

        # PREPARACION DIALOGOS
        guiones_separacion = "-------------------------"
        guiones_sep_jugador = "------------ DETALLES USURPADOR -------------"
        guiones_sep_jug_accion = "------------ ACCIÓN USURPADOR -------------"
        guiones_sep_enemigo = "------------ DETALLES ENEMIGO -------------"
        guiones_sep_ene_accion = "------------ ACCIÓN ENEMIGO -------------"
        guiones_sep_evento_batalla = "---------- EVENTO BATALLA ----------"
        golpe_rapido_acierto = "¡GOLPE DIRECTO!"
        minimo_cargas_jugador = "Necesitás el mínimo de cargas para lanzar un ataque especial. | Perdiste un turno"
        minimo_cargas_enemigo = "El rival no tiene las cargas mínimas para lanzar un ataque especial (30): "
        menu_jugador = """
        --- TURNO JUGADOR ---
        0.Rendirse
        1.Espada - Ataque rápido (+ 2 cargas)
        2.Espada Familiar - Ataque Especial (Mínimo 25 cargas + 20 daño adicional)
        3.Escudo - Defensa básica (Frente ataques rápidos)
        4.Escudo - Defensa específica (Frente ataques especiales, en caso de detener uno, -3 de salud)
        5.Aquellus - Curación (+ 50 salud)
        Opción: """
        mostrar_turno = "TURNO: "
        frase_intro_boss = boss_definitivo.nombre + ": Mi cuerpo aún debe acostumbrarse a la realidad, pero cuando lo haga, ¡morirás!"
        turno_5_jugador = "¡Recogiste el anillo de tú hermana! | Ganas: "
        turno_10_boss = boss_definitivo.nombre + ": ¡Estoy entrando en forma! | Gana: "
        turno_15_boss = boss_definitivo.nombre + ": ¡No tienes ninguna oportunidad! | Gana: "
        turno_20_jugador = "¡Notas cierto poder emanar desde el anillo! | Ganas: "
        turno_25_boss = boss_definitivo.nombre + ": ¡AHHHHHHHH! | Gana: "
        turno_30_jugador = "¡Notas el fragor de la batalla! | Ganas: "
        turno_40_jugador = "¡Preparas un golpe definitivo! | Carga Actual: "
        frase_jugador = jugador.nombre + ": Alguien como tú... ¡no debería regresar del vacio!"
        frase_muerte_boss = boss_definitivo.nombre + ": Te he subestimado... encontrare la forma de regresar... y entonces... "
        frase_muerte_boss_secreto = boss_definitivo.nombre + ": Como... he acabado... ¿qué estás haciendo?... ¡no!..."
        turno_49_boss = boss_definitivo.nombre + ": ¡Demasiado tarde, preparate a morir!"
        frase_win = "El Usurpador logró terminar con una amenaza inminente, pero su hermana sigue muerta y la paz en Pandora no esta garantizada..."
        frase_win_secreto = "El Usurpador, con el poder de la espada familiar, usó rápidamente el alma maldita del hijo bastardo para revivir a su hermana y así evitar cualquier tipo de resurreción.\n" \
                    "La paz de Pandora podrá ser mantenida, pero... ¿qué ocurrirá con el Usurpador?"
        frase_derrota = boss_definitivo.nombre + ": Antes de morir, quiero que sepas que fuiste un gran peón, pero...¡Pandora es mia!"
        boss_definitivo_sorpresa = boss_definitivo.nombre + ": ¡¿Has sido capaz de detener ese golpe?!...¡NO PIENSO PERDER!"

        print(guiones_separacion)
        print("El Usurpador, tras escuchar los últimos lamentos de su moribunda hermana, supo el grave error que "
              "había cometido.\nHabía sido engañado por su hermano bastardo, creído muerto desde hace 5 años, "
              "y que usando el poder de la corona, ha sido capaz de revivir.\nLos recuerdos regresan al Usurpador, "
              "y recogiendo la espada de su hermana, se dispone a eliminar a su enemigo de una vez por todas.  ")
        print(guiones_separacion)
        print(mostrar_turno + str(num_turno))
        print(guiones_separacion)
        fin_partida: bool = False
        print("""--- Características Usurpador ---
-Salud Actual: """ + str(jugador.salud) + "\n-Aquellus en posesión: " + str(
            jugador.aquellus) + "\n-Cargas Usurpador: " + str(jugador.carga_arma) + "\n-Daño Base: " + str(
            jugador.damage))
        print(guiones_separacion)
        print("Enemigo: " + boss_definitivo.nombre)
        print("\n" + frase_intro_boss)
        print(guiones_separacion)
        print("""--- Análisis del enemigo --- 
-Salud Actual: """ + str(boss_definitivo.salud) + "\n-Aquellus en poder: " + str(
            boss_definitivo.aquellus) + "\n-Cargas enemigo: " + str(
            boss_definitivo.carga_arma) + "\n-Daño Base: " + str(
            boss_definitivo.damage))
        while not fin_partida:
            while num_turno >= 1 and jugador.salud > 0:
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
                    num_turno = 0
                elif movimiento_jugador == 1:
                    boss_definitivo.salud = Op.resta_salud(boss_definitivo.salud, jugador.damage)
                    print(golpe_rapido_acierto)
                    print("Salud Rival: " + str(boss_definitivo.salud))
                    jugador.carga_arma = Op.suma_carga(jugador.carga_arma)
                elif movimiento_jugador == 2:
                    if jugador.carga_arma < 25:
                        print(minimo_cargas_jugador)
                    else:
                        boss_definitivo.salud = Op.resta_salud_especial_desafio_jugador(boss_definitivo.salud, jugador.carga_arma)
                        print(
                            "¡Lanzaste un ataque especial de carga: " + str(jugador.carga_arma) + "!")
                        print("Salud Rival: " + str(boss_definitivo.salud))
                        print("Tú carga vuelve a 15")
                        jugador.carga_arma = 15
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
                if boss_definitivo.salud <= -35:
                    print("\n---------- FINAL SECRETO ----------")
                    print(frase_jugador)
                    print(frase_muerte_boss_secreto)
                    print("¡Derrotaste a: " + boss_definitivo.nombre + "!")
                    print(frase_win_secreto)
                    print(guiones_separacion)
                    fin_partida = True
                    break
                elif boss_definitivo.salud <= 0:
                    print("\n---------- FINAL ----------")
                    print(frase_muerte_boss)
                    print("¡Derrotaste a: " + boss_definitivo.nombre + "!")
                    print(frase_win)
                    print(guiones_separacion)
                    fin_partida = True
                    break
                if num_turno == 5:
                    jugador.damage = jugador.damage + 10
                    print(guiones_sep_evento_batalla)
                    print(turno_5_jugador + "\n-Daño Actual: " + str(jugador.damage))
                elif num_turno == 10:
                    boss_definitivo.damage = boss_definitivo.damage + 5
                    print(guiones_sep_evento_batalla)
                    print(turno_10_boss + "\n-Daño Actual: " + str(boss_definitivo.damage))
                elif num_turno == 15:
                    boss_definitivo.damage = boss_definitivo.damage + 10
                    boss_definitivo.salud = boss_definitivo.salud + 50
                    print(guiones_sep_evento_batalla)
                    print(turno_15_boss + "\n-Salud Actual: " + str(boss_definitivo.salud) +
                          "\n-Daño Actual: " + str(boss_definitivo.damage))
                elif num_turno == 20:
                    jugador.damage = jugador.damage + 10
                    jugador.salud = jugador.salud + 40
                    print(guiones_sep_evento_batalla)
                    print(turno_20_jugador + "\n-Salud Actual: " + str(jugador.salud) + "\n-Daño Actual: " + str(jugador.damage))
                elif num_turno == 25:
                    boss_definitivo.damage = boss_definitivo.damage + 5
                    boss_definitivo.salud = boss_definitivo.salud + 25
                    print(guiones_sep_evento_batalla)
                    print(turno_25_boss + "\n-Salud Actual: " + str(boss_definitivo.salud) + "\n-Daño Atual: " + str(boss_definitivo.damage))
                elif num_turno == 30:
                    jugador.damage = jugador.damage + 5
                    jugador.salud = jugador.salud + 30
                    print(guiones_sep_evento_batalla)
                    print(turno_30_jugador + "\n-Salud Actual: " + str(jugador.salud) +
                          "\n-Daño Actual: " + str(jugador.damage))
                elif num_turno == 40:
                    jugador.carga_arma = jugador.carga_arma + 30
                    print(guiones_sep_evento_batalla)
                    print(turno_40_jugador + str(jugador.carga_arma))
                elif num_turno == 49:
                    print(guiones_sep_evento_batalla)
                    print(turno_49_boss)
                elif num_turno == 50:
                    num_turno = 0
                    fin_partida = True
                    break
                # TURNO DEL RIVAL IA
                if movimiento_jugador >= 1:
                    print(guiones_sep_enemigo)
                    print("- Salud Rival: " + str(boss_definitivo.salud))
                    print("- Cargas Rival: " + str(boss_definitivo.carga_arma))
                    print("- Aquellus Restantes: " + str(boss_definitivo.aquellus))
                    print("- Daño Rival: " + str(boss_definitivo.damage))
                    print(guiones_sep_ene_accion)
                    movimiento_ia = random.randint(1, 3)
                    if movimiento_ia == 1:
                        if movimiento_jugador == 3:
                            print("¡El Usurpador se cubrió el golpe!")
                            boss_definitivo.carga_arma = Op.suma_carga(boss_definitivo.carga_arma)
                            num_turno = Op.siguiente_turno(num_turno)
                            print(guiones_separacion)
                            print(mostrar_turno + str(num_turno))
                        else:
                            jugador.salud = Op.resta_salud(jugador.salud, boss_definitivo.damage)
                            print(golpe_rapido_acierto + "\nSalud del Usurpador: " + str(jugador.salud))
                            boss_definitivo.carga_arma = Op.suma_carga(boss_definitivo.carga_arma)
                            num_turno = Op.siguiente_turno(num_turno)
                            print(guiones_separacion)
                            print(mostrar_turno + str(num_turno))
                    elif movimiento_ia == 2:
                        if boss_definitivo.carga_arma < 30:
                            print(minimo_cargas_enemigo + str(boss_definitivo.carga_arma))
                            boss_definitivo.carga_arma = Op.suma_carga(boss_definitivo.carga_arma)
                            print("El Usurpador observa.")
                            num_turno = Op.siguiente_turno(num_turno)
                            print(guiones_separacion)
                            print(mostrar_turno + str(num_turno))
                        else:
                            if movimiento_jugador == 4:
                                print("¡El Usurpador usó todas sus fuerzas para bloquear el golpe!")
                                jugador.salud = Op.proteccion_especial(jugador.salud)
                                print(boss_definitivo_sorpresa)
                                print("La carga del enemigo se reinició a 20")
                                boss_definitivo.carga_arma = 20
                                num_turno = Op.siguiente_turno(num_turno)
                                print(guiones_separacion)
                                print(mostrar_turno + str(num_turno))
                            else:
                                jugador.salud = Op.resta_salud_carga_enemigo(jugador.salud, boss_definitivo.carga_arma)
                                print("¡El rival lanzó un ataque especial!")
                                print("Salud del usurpador: " + str(jugador.salud))
                                boss_definitivo.carga_arma = 20
                                num_turno = Op.siguiente_turno(num_turno)
                                print(guiones_separacion)
                                print(mostrar_turno + str(num_turno))
                    elif movimiento_ia == 3:
                        if boss_definitivo.aquellus == 0:
                            print("¡Al rival no le quedan Aquellus! | Perdió un turno")
                            print("El Usurpador observa.")
                            num_turno = Op.siguiente_turno(num_turno)
                            print(guiones_separacion)
                            print(mostrar_turno + str(num_turno))
                        else:
                            boss_definitivo.salud = Op.suma_salud_enemigo(boss_definitivo.salud)
                            boss_definitivo.aquellus = Op.resta_aquellus(boss_definitivo.aquellus)
                            print("¡El rival recuperó salud!\nSalud actual: " + str(boss_definitivo.salud))
                            print("Aquellus restantes: " + str(boss_definitivo.aquellus))
                            num_turno = Op.siguiente_turno(num_turno)
                            print(guiones_separacion)
                            print(mostrar_turno + str(num_turno))
                            continue
            else:
                print(guiones_separacion)
                print(frase_derrota)
                print("--- HAS MUERTO ---")
                print(guiones_separacion)
                fin_partida = True
