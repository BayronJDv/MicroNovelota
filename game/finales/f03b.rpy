################################################################################
## F03b · El precio del silencio
## La oferta de dinero con res >= 5: humillación y exposición pública.
################################################################################

label f03b:

    $ desbloquear_final("F03b")

    scene bg mesa tardia
    show pedro resentido at izq

    g "Puedo ayudarte, Pedro. No tienes que seguir viviendo así. Dime una cifra, cualquiera, y esto queda atrás. Por los viejos tiempos."

    p "Por los viejos tiempos."

    n "Pedro sonrió. Fue la primera sonrisa completa de toda la noche, y me gustó menos que todas las anteriores."

    p "¿Sabes cuántas veces me he imaginado esta conversación? En el paro, en las colas, en casa de mi suegra. Y siempre terminaba igual: tú sacando un papel y yo golpeándote. Nunca me acordé de la otra opción."

    p "Acepto. Dame el cheque."

    n "No me lo esperaba. Escribí la cifra más grande que había escrito nunca, y Pedro la guardó en el bolsillo con dos dedos, como quien guarda una servilleta."

    p "Gracias, Gabriel. De verdad. Mira lo fácil que es todo cuando hay voluntad."

    n "Pedro pagó su ronda, se puso el abrigo y se detuvo en la puerta. Y entonces lo comprendí, por la manera en que no se despidió: el cheque no era un final."

    hide pedro with dissolve
    scene cg f03b with fade

    n "Dos semanas después, la cifra apareció en una noticia junto a mi nombre, una foto mía saliendo del bufete y tres líneas de texto: «El socio del año y el precio del silencio»."

    n "El cheque nunca se cobró. Se enmarcó. El colegio de abogados abrió expediente, el bufete me pidió un «reposo temporal» y mi tío dejó de decir tercera generación."

    n "Conservé el cargo. Perdí el nombre. Y aprendí que hay mentiras que no se compran: se financian."

    scene black with fade

    n "El precio del silencio."

    return
