################################################################################
## Casos de prueba automatizados (Ren'Py 8.5 Automated Testing)
##
## Ejecutar:  ~/renpy-sdk/renpy.sh <proyecto> test
##
## Recorren las rutas críticas de la matriz de ArbolDecisiones.md. Cada caso
## termina verificando el título del final correspondiente en pantalla.

testsuite global:

    before testcase:
        $ _test.transition_timeout = 0.05
        $ _test.timeout = 5.0

        if not screen "main_menu":
            run MainMenu(confirm=False)

    teardown:
        exit


## D01=A (justicia), D02=B (dejar de beber) -> D03.A debe dar F01a.
testcase ruta_f01a:
    click "start"
    advance until screen "choice"
    click "La justicia."
    advance until screen "choice"
    click "Dejar de beber."
    advance until screen "choice"
    click "Admitir la culpa."
    advance until "La verdad y la redención."

## D01=B (lealtad), D02=B -> D03.B debe dar F03 (res=3 < 4).
testcase ruta_f03_negacion:
    click "start"
    advance until screen "choice"
    click "La lealtad."
    advance until screen "choice"
    click "Dejar de beber."
    advance until screen "choice"
    click "Negar los hechos."
    advance until "Una mentira más."

## D01=C (resultados), D02=A (otra bebida) -> D03.B debe dar F02 (res=5).
testcase ruta_f02:
    click "start"
    advance until screen "choice"
    click "Conseguir resultados."
    advance until screen "choice"
    click "Pedir otra bebida."
    advance until screen "choice"
    click "Negar los hechos."
    advance until "El último argumento."

## D01=C, D02=A -> D03.C debe dar F03b (res=5).
testcase ruta_f03b:
    click "start"
    advance until screen "choice"
    click "Conseguir resultados."
    advance until screen "choice"
    click "Pedir otra bebida."
    advance until screen "choice"
    click "Ofrecer dinero."
    advance until "El precio del silencio."

## D01=A, D02=C (invitar) -> D03.A debe dar F01b (luc=0).
testcase ruta_f01b:
    click "start"
    advance until screen "choice"
    click "La justicia."
    advance until screen "choice"
    click "Invitar a Pedro a beber."
    advance until screen "choice"
    click "Admitir la culpa."
    advance until "La verdad a destiempo."

## La galería abre desde el menú y vuelve.
testcase galeria_abre:
    click "finales"
    advance until screen "galeria_finales"
    click "return"
