################################################################################
## Definiciones: personajes, transforms, imágenes y audio
################################################################################

## Personajes ###################################################################

define g = Character(_("Gabriel"), color="#d8b26a")
define p = Character(_("Pedro"), color="#8fa8bd")
define a = Character(_("Alexandre"), color="#d98c5f")

## Narración en primera persona / pensamiento de Gabriel.
define n = Character(None, what_italic=True)


## Transforms ###################################################################

transform izq:
    xalign 0.24
    yalign 1.0

transform der:
    xalign 0.76
    yalign 1.0

transform solo:
    xalign 0.50
    yalign 1.0

## Respiración sutil para sprites en pantalla.
transform respirar:
    subpixel True
    ease 3.2 yoffset -6
    ease 3.2 yoffset 0
    repeat

## Sacudida para el final trágico. Se detiene al re-mostrar el sprite sin ella.
transform temblor:
    linear 0.06 xoffset 6
    linear 0.06 xoffset -6
    repeat


## Arte #########################################################################
##
## PLACEHOLDERS: cada imagen es un color plano para poder probar el flujo
## completo sin arte. Cuando lleguen los PNG, sustituir la línea por la ruta
## real, por ejemplo:
##
##     image bg mesa = "images/bg/bg_bar_mesa.png"
##     image pedro neutro = "images/char/pedro_neutro.png"
##     image cg f01a = "images/cg/cg_f01a.png"
##
## Los colores siguen la escala de luz de ArbolDecisiones.md (biblia visual).

image bg ceremonia = Solid("#4a3218")
image bg bano = Solid("#223026")
image bg calle = Solid("#10192a")
image bg entrada = Solid("#3a2a16")
image bg barra = Solid("#33251a")
image bg mesa = Solid("#1b2a41")
image bg mesa tardia = Solid("#16222f")

image pedro neutro = Solid("#6e1f2acc", xsize=1000, ysize=1080)
image pedro ironico = Solid("#7a2430cc", xsize=1000, ysize=1080)
image pedro resentido = Solid("#862a36cc", xsize=1000, ysize=1080)
image pedro vulnerable = Solid("#5e3140cc", xsize=1000, ysize=1080)
image pedro furia = Solid("#932f3ccc", xsize=1000, ysize=1080)

image alex neutro = Solid("#2f4538cc", xsize=1000, ysize=1080)
image alex admiracion = Solid("#3a5344cc", xsize=1000, ysize=1080)
image alex incomodo = Solid("#26382ecc", xsize=1000, ysize=1080)

image cg espejo = Solid("#223026")
image cg f01a = Solid("#5a4322")
image cg f01b = Solid("#101c2c")
image cg f02 = Solid("#3d1220")
image cg f03 = Solid("#1c2f26")
image cg f03b = Solid("#2b2b33")

## Overlays de atmósfera. No se muestran aún; descomentar en las escenas cuando
## existan los archivos PNG (fx_vineta, fx_grano, fx_humo, fx_lluvia).
# image fx vineta = "images/fx/fx_vineta.png"
# image fx grano = "images/fx/fx_grano.png"
# image fx humo = "images/fx/fx_humo.png"
# image fx lluvia = "images/fx/fx_lluvia.png"


## Audio ########################################################################
##
## Activar cada línea cuando exista el archivo correspondiente:
##
## play music "audio/music/mus_bar.ogg" fadein 2.0
## play sound "audio/sfx/amb_bar.ogg" loop volume 0.4
