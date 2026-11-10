################################################################################
## F03 · Una mentira más
## Evasión: Pedro se marcha; Gabriel conserva su reputación y su soledad.
################################################################################

label f03:

    $ desbloquear_final("F03")

    scene bg mesa tardia
    show pedro resentido at izq

    g "Puedo ayudarte, Pedro. No tienes que seguir viviendo así. Escribe una cifra, la que necesites para empezar de nuevo. Podemos dejar todo esto atrás."

    n "Alcancé la cartera antes de terminar la frase. Un cheque en blanco es la forma más elegante de decir «cállate»."

    p "..."

    p "¿Eso soy para ti? ¿Una deuda pendiente que puedes pagar?"

    p "Ni una disculpa, Gabriel. Ni un lo siento. Dinero. Como en el bufete: todo se puede poner precio."

    n "Pedro empujó el cheque de vuelta con dos dedos, sin tocarlo siquiera."

    p "Guárdatelo. Con esto te has comprado veinte años de silencio, ¿no? Pregúntate cuánto te queda."

    hide pedro with dissolve
    scene cg f03 with fade

    n "La puerta del bar se cerró con suavidad, lo cual fue peor que un portazo."

    n "El barman recogió los vasos. Alexandre ya se había ido. El cheque volvió a mi cartera con la dificultad de un papel que no quiere doblarse."

    n "Al día siguiente mi vida siguió exactamente igual. Las causas, los discursos, la beca con mi nombre. Todo funcionó."

    n "Todo, menos la costumbre nueva de mirar la puerta de los bares y pensar que un hombre delgado, con abrigo, está sentado en alguna parte, sin tocar un vaso."

    scene black with fade

    n "Una mentira más."

    return
