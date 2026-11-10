################################################################################
## Galería de finales
##
## Accesible desde el menú principal (botón "Finales"). Muestra una tarjeta por
## final; los no descubiertos aparecen como "???".
################################################################################

define FINALES_INFO = [
    ("F01a", _("La verdad y la redención"), _("Gabriel confiesa y asume las consecuencias. Pedro escucha, aunque no perdona."), "cg f01a"),
    ("F01b", _("La verdad a destiempo"), _("Gabriel confiesa sin haber sabido escuchar. Pedro no le cree."), "cg f01b"),
    ("F02", _("El último argumento"), _("La negación colma el resentimiento. La conversación termina en violencia."), "cg f02"),
    ("F03", _("Una mentira más"), _("Pedro se marcha. Gabriel conserva su reputación y su soledad."), "cg f03"),
    ("F03b", _("El precio del silencio"), _("La oferta de dinero se vuelve humillación, y la humillación, titular."), "cg f03b"),
]


screen galeria_finales():

    tag menu

    use game_menu(_("Finales"), scroll="viewport"):

        style_prefix "galeria"

        vbox:
            spacing 18

            text _("Descubiertos: [len(persistent.finales)]/[len(FINALES_INFO)]"):
                style "galeria_contador"

            null height 12

            for fid, titulo, desc, cg_id in FINALES_INFO:

                if fid in persistent.finales:
                    textbutton titulo:
                        style "galeria_button"
                        action Show("visor_cg", cg_id=cg_id, titulo=titulo)

                    text desc:
                        style "galeria_desc"

                else:
                    text "???":
                        style "galeria_bloqueado"

                null height 6


screen visor_cg(cg_id, titulo):

    modal True
    zorder 100

    add cg_id

    text titulo:
        style "visor_titulo"

    textbutton _("Cerrar"):
        action Hide("visor_cg")
        xalign 0.98
        yalign 0.02

    key "dismiss" action Hide("visor_cg")
    key "game_menu" action Hide("visor_cg")


style galeria_contador is gui_text
style galeria_button is gui_button
style galeria_button_text is gui_button_text
style galeria_desc is gui_text
style galeria_bloqueado is gui_text
style visor_titulo is gui_text

style galeria_contador:
    color gui.accent_color
    size gui.label_text_size

style galeria_button:
    xminimum 640

style galeria_button_text:
    size gui.interface_text_size
    color gui.hover_color

style galeria_desc:
    size 26
    left_padding 30
    color gui.idle_small_color

style galeria_bloqueado:
    size gui.interface_text_size
    color "#5a5a55"

style visor_titulo:
    xalign 0.02
    yalign 0.02
    size gui.label_text_size
    color gui.accent_color
    outlines [(2, "#000000", 0, 0)]
