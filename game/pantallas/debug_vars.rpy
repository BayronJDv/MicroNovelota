################################################################################
## Pantalla de depuración (solo visible con config.developer activo)
##
## Tecla K: muestra/oculta el estado de variables y banderas.
################################################################################

default mostrar_debug = False


screen debug_vars():

    zorder 250

    key "K" action ToggleVariable("mostrar_debug")

    if mostrar_debug and config.developer:

        frame:
            xalign 0.02
            yalign 0.02
            padding (24, 18)
            background "#0d141ce6"

            vbox:
                spacing 4

                text "res [res] · conf [conf] · luc [luc]" size 24 color "#efe6d6"
                text "D01=[respuesta_d01] D02=[respuesta_d02] D03=[eleccion_d03]" size 24 color "#efe6d6"
                text "desprecio [flag_desprecio] · evasion [flag_evasion]" size 24 color "#8c8579"
                text "imprevisible [flag_imprevisible] · alcohol [flag_alcohol]" size 24 color "#8c8579"
                text "finales: [persistent.finales]" size 24 color "#8c8579"
                text "K para ocultar · Shift+O consola" size 20 color "#5a5a55"


init python:
    config.overlay_screens.append("debug_vars")
