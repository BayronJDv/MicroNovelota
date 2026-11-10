################################################################################
## S04 · La verdad tiene un precio + D03 (punto de no retorno) + resolución
################################################################################

label s04_verdad:

    n "Alexandre se levanta con su vaso a medio terminar y una excusa que nadie le cree."

    hide alex with dissolve
    scene bg mesa tardia with fade
    show pedro neutro at izq with dissolve

    ## play music "audio/music/mus_tension.ogg" fadein 3.0

    if flag_evasion:
        p "Se te da bien esto, ¿sabes? Empezar conversaciones nuevas cuando las viejas se ponen incómodas."

    if flag_imprevisible:
        p "¿Te acuerdas de la despedida de Marta? Tú también sabías reírte entonces. Casi parecía otra persona."

    if flag_alcohol:
        p "Y esa copa nueva que ni has tocado. Dime, ¿bebes por elegancia o por costumbre?"

    show pedro vulnerable

    p "Me quedé sin ahorros en el segundo año. Sabía que había una lista negra, pero hice las cuentas: si no encontraba nada en seis meses, la hipoteca ganaba."

    p "Ningún despacho de la ciudad me contrató. Ninguno de la siguiente, tampoco. ¿Sabes lo que es hacer números en un supermercado para ver si te llega para la cena? Yo cenaba con jueces, Gabriel."

    p "Mi mujer aguantó lo que pudo. Mi hija aprendió a decir que su padre estaba entre proyectos. Los niños lo aprenden rápido."

    show pedro resentido

    p "Y tú dando discursos. Causas sociales. Becas. Hasta saliste en el periódico defendiendo a un tipo al que despidieron con un expediente trucado. Me lo enseñó mi sobrina. Me reí. No sé si me reí."

    n "Pedro se inclina hacia mí. El bar está casi vacío; la lámpara sobre la mesa suelta un círculo de luz que ya no alcanza para los dos."

    p "Gabriel, tú siempre has sabido defenderte con palabras. Dime algo... ¿alguna vez te has preguntado qué habría pasado si hubieras dicho la verdad?"

    n "Ahí lo entendí. Pedro sabía. No sospechaba: sabía. Y esta noche, por algún motivo que quizá tampoco él entiende, ha decidido jugársela."


label d03:

    menu:

        "Admitir la culpa.":
            $ eleccion_d03 = "A"

        "Negar los hechos.":
            $ eleccion_d03 = "B"

        "Ofrecer dinero.":
            $ eleccion_d03 = "C"

    jump resolver_final


label resolver_final:

    if eleccion_d03 == "A" and conf >= 1 and luc >= 1:
        jump f01a
    elif eleccion_d03 == "A":
        jump f01b
    elif eleccion_d03 == "B" and res >= 4:
        jump f02
    elif eleccion_d03 == "C" and res >= 5:
        jump f03b
    else:
        jump f03
