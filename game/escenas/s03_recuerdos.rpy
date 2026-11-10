################################################################################
## S03 · Los recuerdos + D02 (la bebida)
################################################################################

label s03_recuerdos:

    show pedro resentido

    p "¿Te acuerdas de las tardes en el bufete? Los dos con becas de miseria, soñando con juicios que no existían. Yo ordenaba tus carpetas, Gabriel. Llegué a saber dónde estabas antes que tu secretaria."

    n "Pedro habla del bufete como quien habla de un país que ya no existe."

    p "Tú tenías un don. Lo digo en serio. Cuando hablabas del interés público, hasta yo te creía."

    if flag_desprecio:
        p "Qué ironía, ¿eh? A mí ya no me impresiona tu currículum. Yo sé exactamente lo que costó."

    show alex incomodo

    n "Alexandre, que ha entendido todo menos lo que importa, intenta romper el hielo."

    a "¿Otra ronda? Yo invito la siguiente."


label d02:

    menu:

        "Pedir otra bebida.":
            $ respuesta_d02 = "A"
            $ ajustar(res_d=2, luc_d=-1)
            $ flag_evasion = True
            $ flag_alcohol = True
            g "Sí. Otra. La que sea."
            n "Levanté la mano hacia la barra antes de que Pedro terminara de mirarme. La conversación podía esperar otra media hora. Llevaba veinte años esperando; ¿qué más daba?"

        "Dejar de beber.":
            $ respuesta_d02 = "B"
            $ ajustar(conf_d=1, luc_d=1)
            g "No. Gracias, Alexandre. Creo que... quiero escuchar esto."
            n "Dejé el vaso sobre la mesa, vacío ya, y me quedé donde estaba. Pedro entrecerró los ojos, buscando la trampa."

        "Invitar a Pedro a beber.":
            $ respuesta_d02 = "C"
            $ ajustar(res_d=1, conf_d=1)
            $ flag_imprevisible = True
            $ flag_alcohol = True
            g "Tráele una a Pedro. De las de antes. Las que tomábamos cuando el bufete era una oficina con dos mesas."
            n "Pedro la aceptó, pero bebió como quien firma un documento: sin gustárselo."

    if respuesta_d02 == "A":
        p "Siempre fuiste bueno para mirar hacia otro lado cuando las cosas se complicaban."
    elif respuesta_d02 == "B":
        p "Mira nada más... parece que todavía puedes escuchar a alguien sin tener que convencerlo de algo."
    else:
        p "¿Ahora quieres invitarme algo? Antes también tenías formas bastante curiosas de conseguir lo que querías."

    jump s04_verdad
