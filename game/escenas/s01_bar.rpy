################################################################################
## S01 · El bar + D01 (¿Qué es lo más importante para un abogado?)
################################################################################

label s01_bar:

    scene bg entrada with fade

    ## play music "audio/music/mus_bar.ogg" fadein 2.0
    ## play sound "audio/sfx/amb_bar.ogg" loop volume 0.4

    show alex neutro at solo with dissolve

    a "¿Gabriel Ferrán? No... no me lo puedo creer."

    n "Un chico de veintitantos años se me planta delante con una sonrisa de fan y una servilleta arrugada en la mano."

    a "Alexandre. Estudio Derecho. He leído el caso de las viviendas de Herrera, el del hospital... básicamente todo lo que ha salido de usted."

    show alex admiracion

    a "Siempre digo que si llego a la mitad de abogado que es usted, ya me doy por satisfecho."

    n "Me da un poco de vergüenza. Y un poco de algo peor, que no sé nombrar."

    a "¿Me deja hacerle una pregunta, solo una? Es para un trabajo."

    a "Después de tantos años ejerciendo... ¿qué diría que es lo más importante para un abogado? ¿La justicia, la lealtad o conseguir resultados?"


label d01:

    menu:

        "La justicia.":
            $ respuesta_d01 = "A"
            $ ajustar(res_d=1)
            g "La justicia. La técnica, los contactos, los resultados... son medios. La justicia es lo único que convierte esto en un oficio y no en un trámite."

        "La lealtad.":
            $ respuesta_d01 = "B"
            $ ajustar(res_d=2)
            g "La lealtad. A los tuyos, a los que confiaron en ti antes de que tuvieras un despacho. Sin eso, la abogacía es un oficio de mercenarios."

        "Conseguir resultados.":
            $ respuesta_d01 = "C"
            $ ajustar(res_d=2)
            $ flag_desprecio = True
            g "Resultados. La justicia y la lealtad están bien en los discursos, pero un abogado se mide por lo que consigue. Todo lo demás es decorado."

    jump s02_reencuentro
