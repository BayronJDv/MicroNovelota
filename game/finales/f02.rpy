################################################################################
## F02 · El último argumento
## La negación con res >= 4 desata la violencia.
################################################################################

label f02:

    $ desbloquear_final("F02")

    scene bg mesa tardia
    show pedro furia at izq with vpunch

    g "No puedes responsabilizarme de todo lo que te ha pasado. Yo también tuve que tomar decisiones difíciles. El informe no era tuyo por casualidad, Pedro: tu firma era la más conveniente para el despacho. No me culpes de aritmética."

    p "La más conveniente."

    n "Pedro repitió mi frase en voz baja, como quien prueba un veneno."

    p "Sabía que dirías algo así. Veinte años esperando que dijeras otra cosa... y has dicho exactamente esto."

    g "Pedro, siéntate. Estás borracho."

    p "¿Y tú qué estás? ¿Sobrio? Llevo veinte años sobrio de ti."

    show pedro furia at izq, temblor

    p "Todo lo que tengo delante —la deuda, la lista negra, la casa de mi suegra— empezó en una oficina donde tú escribías y yo firmaba. Y el hombre que lo hizo da discursos sobre justicia."

    n "Pedro se levantó. La silla cayó hacia atrás y el ruido llenó el bar entero."

    hide pedro
    scene cg f02 with vpunch

    n "La mesa se volcó. El vaso explotó contra el suelo."

    n "No recuerdo cuánto duró. Recuerdo el rojo de la luz sobre la barra y una idea absurda, profesional, que me cruzó la cabeza como un último manotazo: que ninguna de mis causas había preparado a nadie para esto."

    scene black with fade

    n "El abogado que dedicó su carrera a defender la justicia murió en la mesa de un bar, a manos del hombre al que traicionó."

    n "La injusticia, esta vez, tampoco dejó testigos útiles."

    n "El último argumento."

    return
