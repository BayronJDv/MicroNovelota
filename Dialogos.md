# Diálogos completos por escena — JogoPro

Transcripción de todos los textos del juego tal como están en `game/` (fuente de verdad: los archivos `.rpy`).

**Leyenda:**
- **NARRACIÓN** — pensamiento de Gabriel (`n`, se muestra en cursiva sin nombre).
- **GABRIEL / PEDRO / ALEXANDRE** — diálogo hablado.
- *(si …)* — línea condicional: solo aparece si se cumple la condición indicada.
- Las frases entre « » son opciones de menú (elección del jugador).

---

## S00 · Prólogo: el reconocimiento (`script.rpy`)

**NARRACIÓN:** La felicitación llegó por correo interno a las once de la mañana: «Por su trayectoria en la defensa del interés público, el bufete nombra a Gabriel Ferrán socio del año».

**NARRACIÓN:** Por la noche, en la cena del bufete, mi tío levantó la copa y dijo la frase que ya era tradición: tercera generación de abogados en esta familia. Tercera generación.

**NARRACIÓN:** La sala aplaudió. Debería haberme sentido satisfecho.

**NARRACIÓN:** Pero pensé en Pedro.

*(Fondo: baño)*

**NARRACIÓN:** Me encerré en el baño de la sala de eventos. Veinte años haciendo justicia con el apellido de otros detrás.

*(Fondo: CG espejo)*

**NARRACIÓN:** El espejo me devolvió un hombre impecable: traje azul marino, reloj de oro, ninguna mancha visible.
Dialogos.md y el árbol q
**NARRACIÓN:** Pedro firmó un informe que nunca escribió. Los registros de aquella prueba antidrogas llevaban mi letra debajo de la suya.

**NARRACIÓN:** Él perdió el empleo, los ahorros y el nombre. Yo gané esta corbata que ahora me aprieta.

*(Fondo: calle)*

**NARRACIÓN:** Salí sin despedirme. Caminé sin rumbo hasta que reconocí el letrero: el bar de la calle Cerrada, el de los años de universidad, cuando ser abogado era una idea y no una cuenta de resultados.

**NARRACIÓN:** Quería un trago, ruido que no me hiciera preguntas y una noche sin responsabilidades.

**NARRACIÓN:** No llegaba buscando redención. Llegaba buscando olvidar.

---

## S01 · El bar (`escenas/s01_bar.rpy`)

**ALEXANDRE:** ¿Gabriel Ferrán? No... no me lo puedo creer.

**NARRACIÓN:** Un chico de veintitantos años se me planta delante con una sonrisa de fan y una servilleta arrugada en la mano.

**ALEXANDRE:** Alexandre. Estudio Derecho. He leído el caso de las viviendas de Herrera, el del hospital... básicamente todo lo que ha salido de usted.

**ALEXANDRE:** Siempre digo que si llego a la mitad de abogado que es usted, ya me doy por satisfecho.

**NARRACIÓN:** Me da un poco de vergüenza. Y un poco de algo peor, que no sé nombrar.

**ALEXANDRE:** ¿Me deja hacerle una pregunta, solo una? Es para un trabajo.

**ALEXANDRE:** Después de tantos años ejerciendo... ¿qué diría que es lo más importante para un abogado? ¿La justicia, la lealtad o conseguir resultados?

### D01 · Decisión

| Opción | Respuesta de Gabriel |
| --- | --- |
| «La justicia.» | La justicia. La técnica, los contactos, los resultados... son medios. La justicia es lo único que convierte esto en un oficio y no en un trámite. |
| «La lealtad.» | La lealtad. A los tuyos, a los que confiaron en ti antes de que tuvieras un despacho. Sin eso, la abogacía es un oficio de mercenarios. |
| «Conseguir resultados.» | Resultados. La justicia y la lealtad están bien en los discursos, pero un abogado se mide por lo que consigue. Todo lo demás es decorado. |

---

## S02 · El reencuentro (`escenas/s02_reencuentro.rpy`)

**PEDRO** *(si D01 = A)*: Qué curioso escuchar eso de ti.

**PEDRO** *(si D01 = B)*: Supongo que algunos compañeros no cuentan dentro de esa lealtad.

**PEDRO** *(si D01 = C)*: Entonces supongo que lo mío fue un resultado necesario.

**NARRACIÓN:** La voz llega desde la mesa del rincón. Amarga, pausada, sin prisa por herir. Con prisa, en cambio, por clavar.

**GABRIEL:** ¿... Pedro?

**PEDRO:** Cuánto tiempo, Gabriel. O debería decir... consejero Ferrán.

**ALEXANDRE:** ¿Se conocen?

**GABRIEL:** Trabajamos juntos. Hace años.

**PEDRO:** Juntos. Sí. La palabra se nos queda corta, ¿no?

**NARRACIÓN:** Pedro gira la copa sobre la mesa sin beber. Alexandre mira la mesa, a mí y otra vez la mesa.

**GABRIEL:** Quédate, Alexandre. Es una conversación que le debo a alguien.

**NARRACIÓN:** Pedro sonríe con la mitad de la cara.

---

## S03 · Los recuerdos (`escenas/s03_recuerdos.rpy`)

**PEDRO:** ¿Te acuerdas de las tardes en el bufete? Los dos con becas de miseria, soñando con juicios que no existían. Yo ordenaba tus carpetas, Gabriel. Llegué a saber dónde estabas antes que tu secretaria.

**NARRACIÓN:** Pedro habla del bufete como quien habla de un país que ya no existe.

**PEDRO:** Tú tenías un don. Lo digo en serio. Cuando hablabas del interés público, hasta yo te creía.

**PEDRO** *(si D01 = C — flag `desprecio`)*: Qué ironía, ¿eh? A mí ya no me impresiona tu currículum. Yo sé exactamente lo que costó.

**NARRACIÓN:** Alexandre, que ha entendido todo menos lo que importa, intenta romper el hielo.

**ALEXANDRE:** ¿Otra ronda? Yo invito la siguiente.

### D02 · Decisión

| Opción | Texto siguiente |
| --- | --- |
| «Pedir otra bebida.» | **GABRIEL:** Sí. Otra. La que sea. — **NARRACIÓN:** Levanté la mano hacia la barra antes de que Pedro terminara de mirarme. La conversación podía esperar otra media hora. Llevaba veinte años esperando; ¿qué más daba? |
| «Dejar de beber.» | **GABRIEL:** No. Gracias, Alexandre. Creo que... quiero escuchar esto. — **NARRACIÓN:** Dejé el vaso sobre la mesa, vacío ya, y me quedé donde estaba. Pedro entrecerró los ojos, buscando la trampa. |
| «Invitar a Pedro a beber.» | **GABRIEL:** Tráele una a Pedro. De las de antes. Las que tomábamos cuando el bufete era una oficina con dos mesas. — **NARRACIÓN:** Pedro la aceptó, pero bebió como quien firma un documento: sin gustárselo. |

### Reacción de Pedro (según D02)

**PEDRO** *(si D02 = A)*: Siempre fuiste bueno para mirar hacia otro lado cuando las cosas se complicaban.

**PEDRO** *(si D02 = B)*: Mira nada más... parece que todavía puedes escuchar a alguien sin tener que convencerlo de algo.

**PEDRO** *(si D02 = C)*: ¿Ahora quieres invitarme algo? Antes también tenías formas bastante curiosas de conseguir lo que querías.

---

## S04 · La verdad tiene un precio (`escenas/s04_verdad.rpy`)

**NARRACIÓN:** Alexandre se levanta con su vaso a medio terminar y una excusa que nadie le cree.

*(Cambio de fondo: mesa tardía; Alexandre sale de escena)*

**PEDRO** *(si D02 = A — flag `evasion`)*: Se te da bien esto, ¿sabes? Empezar conversaciones nuevas cuando las viejas se ponen incómodas.

**PEDRO** *(si D02 = C — flag `imprevisible`)*: ¿Te acuerdas de la despedida de Marta? Tú también sabías reírte entonces. Casi parecía otra persona.

**PEDRO** *(si D02 = A o C — flag `alcohol`)*: Y esa copa nueva que ni has tocado. Dime, ¿bebes por elegancia o por costumbre?

**PEDRO:** Me quedé sin ahorros en el segundo año. Sabía que había una lista negra, pero hice las cuentas: si no encontraba nada en seis meses, la hipoteca ganaba.

**PEDRO:** Ningún despacho de la ciudad me contrató. Ninguno de la siguiente, tampoco. ¿Sabes lo que es hacer números en un supermercado para ver si te llega para la cena? Yo cenaba con jueces, Gabriel.

**PEDRO:** Mi mujer aguantó lo que pudo. Mi hija aprendió a decir que su padre estaba entre proyectos. Los niños lo aprenden rápido.

**PEDRO:** Y tú dando discursos. Causas sociales. Becas. Hasta saliste en el periódico defendiendo a un tipo al que despidieron con un expediente trucado. Me lo enseñó mi sobrina. Me reí. No sé si me reí.

**NARRACIÓN:** Pedro se inclina hacia mí. El bar está casi vacío; la lámpara sobre la mesa suelta un círculo de luz que ya no alcanza para los dos.

**PEDRO:** Gabriel, tú siempre has sabido defenderte con palabras. Dime algo... ¿alguna vez te has preguntado qué habría pasado si hubieras dicho la verdad?

**NARRACIÓN:** Ahí lo entendí. Pedro sabía. No sospechaba: sabía. Y esta noche, por algún motivo que quizá tampoco él entiende, ha decidido jugársela.

### D03 · Decisión

Opciones visibles: «Admitir la culpa.» · «Negar los hechos.» · «Ofrecer dinero.»

---

## F01a · La verdad y la redención (`finales/f01a.rpy`)

**GABRIEL:** Sí. Todas las noches. Pedro... los registros de aquella prueba los alteré yo. El informe que firmaste lo escribí yo.

**GABRIEL:** No tengo ninguna excusa. Sé que no puedo devolverte lo que perdiste, pero puedo dejar de esconder lo que hice.

**NARRACIÓN:** Dije lo que llevaba veinte años ensayando frente al espejo de un baño. Sin la presión familiar, sin las ambiciones de un chico de veintiséis años con miedo a ser nadie. Nada de eso era un argumento. Era solo la explicación de un cobarde.

**PEDRO:** ¿Y ahora qué? ¿Se supone que tengo que decirte que todo está bien?

**GABRIEL:** No. Se supone que dejo de mentirte. Lo demás no te corresponde a ti arreglarlo.

**NARRACIÓN:** Le dije que el bufete conserva copias de los registros originales, que mañana mismo lo comunicaría al colegio y a la fiscalía. Con mi firma y sin abogados de por medio.

**PEDRO:** Veinte años, Gabriel. Vas a destrozar veinte años de tu vida por una noche de bar.

**GABRIEL:** Vosotros destruisteis veinte años de la vuestra por mi miedo. Al menos esta parte es mía.

**NARRACIÓN:** No nos abrazamos. Pedro pagó su ronda, la mía también, y se marchó a casa, que aún existe.

**NARRACIÓN:** Yo me quedé hasta el amanecer, escribiendo la carta que empezaría a devolverme a mí mismo.

**NARRACIÓN:** La verdad no compró su perdón. Compró algo más pequeño y más difícil: dejar de ser dos personas.

*(Fade a negro)*

**NARRACIÓN:** La verdad y la redención.

---

## F01b · La verdad a destiempo (`finales/f01b.rpy`)

**GABRIEL:** Sí. Lo he preguntado. Todas las noches. Aquella prueba la alteré yo, Pedro. El informe lo escribí yo. Perdóname.

**NARRACIÓN:** Lo solté de golpe, torpe, medio de un tirón. Las palabras salieron como salen las náuseas: aliviando y avergonzando a la vez.

**NARRACIÓN:** Pedro me miró durante mucho tiempo. Más que sorpresa, había cálculo.

**PEDRO:** ¿Ahora? ¿Después de veinte años, en un bar, con esa copa sin tocar, me dices esto a mí?

**PEDRO:** No te creo, Gabriel. Y lo peor no es eso. Lo peor es que aunque sea verdad, no me importa. Si lo dijiste para aliviarte, es solo otra cosa que te haces a ti mismo. Si lo dijiste por otra cosa, no quiero saber cuál.

**GABRIEL:** Voy a denunciarlo. Mañana mismo, con los registros originales.

**PEDRO:** Claro. Y cuando salga en los periódicos, el protagonista volverás a ser tú: el abogado caído que confiesa. Hasta para hundirte, sales en la primera página.

**NARRACIÓN:** Pedro se fue sin terminar la copa.

**NARRACIÓN:** Presenté la denuncia al día siguiente. El bufete cayó, el apellido también, y en algún artículo mediocre alguien escribió que actué por remordimiento.

**NARRACIÓN:** Pedro nunca me llamó.

**NARRACIÓN:** Hice lo correcto en el peor orden posible: primero me escuché a mí, y después, demasiado tarde, intenté escucharlo a él. La verdad llegó, pero sin nadie al otro lado para recibirla.

*(Fade a negro)*

**NARRACIÓN:** La verdad a destiempo.

---

## F02 · El último argumento (`finales/f02.rpy`)

**GABRIEL:** No puedes responsabilizarme de todo lo que te ha pasado. Yo también tuve que tomar decisiones difíciles. El informe no era tuyo por casualidad, Pedro: tu firma era la más conveniente para el despacho. No me culpes de aritmética.

**PEDRO:** La más conveniente.

**NARRACIÓN:** Pedro repitió mi frase en voz baja, como quien prueba un veneno.

**PEDRO:** Sabía que dirías algo así. Veinte años esperando que dijeras otra cosa... y has dicho exactamente esto.

**GABRIEL:** Pedro, siéntate. Estás borracho.

**PEDRO:** ¿Y tú qué estás? ¿Sobrio? Llevo veinte años sobrio de ti.

**PEDRO:** Todo lo que tengo delante —la deuda, la lista negra, la casa de mi suegra— empezó en una oficina donde tú escribías y yo firmaba. Y el hombre que lo hizo da discursos sobre justicia.

**NARRACIÓN:** Pedro se levantó. La silla cayó hacia atrás y el ruido llenó el bar entero.

*(CG: confrontación)*

**NARRACIÓN:** La mesa se volcó. El vaso explotó contra el suelo.

**NARRACIÓN:** No recuerdo cuánto duró. Recuerdo el rojo de la luz sobre la barra y una idea absurda, profesional, que me cruzó la cabeza como un último manotazo: que ninguna de mis causas había preparado a nadie para esto.

*(Fade a negro)*

**NARRACIÓN:** El abogado que dedicó su carrera a defender la justicia murió en la mesa de un bar, a manos del hombre al que traicionó.

**NARRACIÓN:** La injusticia, esta vez, tampoco dejó testigos útiles.

**NARRACIÓN:** El último argumento.

---

## F03 · Una mentira más (`finales/f03.rpy`)

**GABRIEL:** Puedo ayudarte, Pedro. No tienes que seguir viviendo así. Escribe una cifra, la que necesites para empezar de nuevo. Podemos dejar todo esto atrás.

**NARRACIÓN:** Alcancé la cartera antes de terminar la frase. Un cheque en blanco es la forma más elegante de decir «cállate».

**PEDRO:** ...

**PEDRO:** ¿Eso soy para ti? ¿Una deuda pendiente que puedes pagar?

**PEDRO:** Ni una disculpa, Gabriel. Ni un lo siento. Dinero. Como en el bufete: todo se puede poner precio.

**NARRACIÓN:** Pedro empujó el cheque de vuelta con dos dedos, sin tocarlo siquiera.

**PEDRO:** Guárdatelo. Con esto te has comprado veinte años de silencio, ¿no? Pregúntate cuánto te queda.

*(Pedro sale; CG: la puerta del bar)*

**NARRACIÓN:** La puerta del bar se cerró con suavidad, lo cual fue peor que un portazo.

**NARRACIÓN:** El barman recogió los vasos. Alexandre ya se había ido. El cheque volvió a mi cartera con la dificultad de un papel que no quiere doblarse.

**NARRACIÓN:** Al día siguiente mi vida siguió exactamente igual. Las causas, los discursos, la beca con mi nombre. Todo funcionó.

**NARRACIÓN:** Todo, menos la costumbre nueva de mirar la puerta de los bares y pensar que un hombre delgado, con abrigo, está sentado en alguna parte, sin tocar un vaso.

*(Fade a negro)*

**NARRACIÓN:** Una mentira más.

---

## F03b · El precio del silencio (`finales/f03b.rpy`)

**GABRIEL:** Puedo ayudarte, Pedro. No tienes que seguir viviendo así. Dime una cifra, cualquiera, y esto queda atrás. Por los viejos tiempos.

**PEDRO:** Por los viejos tiempos.

**NARRACIÓN:** Pedro sonrió. Fue la primera sonrisa completa de toda la noche, y me gustó menos que todas las anteriores.

**PEDRO:** ¿Sabes cuántas veces me he imaginado esta conversación? En el paro, en las colas, en casa de mi suegra. Y siempre terminaba igual: tú sacando un papel y yo golpeándote. Nunca me acordé de la otra opción.

**PEDRO:** Acepto. Dame el cheque.

**NARRACIÓN:** No me lo esperaba. Escribí la cifra más grande que había escrito nunca, y Pedro la guardó en el bolsillo con dos dedos, como quien guarda una servilleta.

**PEDRO:** Gracias, Gabriel. De verdad. Mira lo fácil que es todo cuando hay voluntad.

**NARRACIÓN:** Pedro pagó su ronda, se puso el abrigo y se detuvo en la puerta. Y entonces lo comprendí, por la manera en que no se despidió: el cheque no era un final.

*(Pedro sale; CG: el cheque y el teléfono sobre la mesa)*

**NARRACIÓN:** Dos semanas después, la cifra apareció en una noticia junto a mi nombre, una foto mía saliendo del bufete y tres líneas de texto: «El socio del año y el precio del silencio».

**NARRACIÓN:** El cheque nunca se cobró. Se enmarcó. El colegio de abogados abrió expediente, el bufete me pidió un «reposo temporal» y mi tío dejó de decir tercera generación.

**NARRACIÓN:** Conservé el cargo. Perdí el nombre. Y aprendí que hay mentiras que no se compran: se financian.

*(Fade a negro)*

**NARRACIÓN:** El precio del silencio.
