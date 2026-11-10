################################################################################
## JogoPro — novela visual (demo)
##
## Punto de entrada y S00 · Prólogo: el reconocimiento.
################################################################################


label start:
    jump s00_prologo


label s00_prologo:

    scene bg ceremonia with fade

    n "La felicitación llegó por correo interno a las once de la mañana: «Por su trayectoria en la defensa del interés público, el bufete nombra a Gabriel Ferrán socio del año»."

    n "Por la noche, en la cena del bufete, mi tío levantó la copa y dijo la frase que ya era tradición: tercera generación de abogados en esta familia. Tercera generación."

    n "La sala aplaudió. Debería haberme sentido satisfecho."

    n "Pero pensé en Pedro."

    scene bg bano with fade

    n "Me encerré en el baño de la sala de eventos. Veinte años haciendo justicia con el apellido de otros detrás."

    scene cg espejo with dissolve

    n "El espejo me devolvió un hombre impecable: traje azul marino, reloj de oro, ninguna mancha visible."

    n "Pedro firmó un informe que nunca escribió. Los registros de aquella prueba antidrogas llevaban mi letra debajo de la suya."

    n "Él perdió el empleo, los ahorros y el nombre. Yo gané esta corbata que ahora me aprieta."

    scene bg calle with fade

    n "Salí sin despedirme. Caminé sin rumbo hasta que reconocí el letrero: el bar de la calle Cerrada, el de los años de universidad, cuando ser abogado era una idea y no una cuenta de resultados."

    n "Quería un trago, ruido que no me hiciera preguntas y una noche sin responsabilidades."

    n "No llegaba buscando redención. Llegaba buscando olvidar."

    jump s01_bar
