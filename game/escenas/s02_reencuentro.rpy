################################################################################
## S02 · El reencuentro: Pedro respondió a la respuesta de Gabriel.
################################################################################

label s02_reencuentro:

    scene bg mesa with fade
    show pedro ironico at izq with dissolve
    show alex incomodo at der with dissolve

    if respuesta_d01 == "A":
        p "Qué curioso escuchar eso de ti."
    elif respuesta_d01 == "B":
        p "Supongo que algunos compañeros no cuentan dentro de esa lealtad."
    else:
        p "Entonces supongo que lo mío fue un resultado necesario."

    n "La voz llega desde la mesa del rincón. Amarga, pausada, sin prisa por herir. Con prisa, en cambio, por clavar."

    g "¿... Pedro?"

    p "Cuánto tiempo, Gabriel. O debería decir... consejero Ferrán."

    a "¿Se conocen?"

    g "Trabajamos juntos. Hace años."

    p "Juntos. Sí. La palabra se nos queda corta, ¿no?"

    n "Pedro gira la copa sobre la mesa sin beber. Alexandre mira la mesa, a mí y otra vez la mesa."

    g "Quédate, Alexandre. Es una conversación que le debo a alguien."

    n "Pedro sonríe con la mitad de la cara."

    jump s03_recuerdos
