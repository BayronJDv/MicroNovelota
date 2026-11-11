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
## Los fondos y CGs se escalan a 1920×1080 con fit="cover" para llenar la
## pantalla sin deformarse. Los sprites ya están recortados con transparencia
## y normalizados a 1080 px de alto; los transforms izq/der/solo los posician.

image bg ceremonia = Transform("images/bg/bg_ceremonia.png", xysize=(1920, 1080), fit="cover")
image bg bano = Transform("images/bg/bg_bano.png", xysize=(1920, 1080), fit="cover")
image bg calle = Transform("images/bg/bg_calle.png", xysize=(1920, 1080), fit="cover")
image bg entrada = Transform("images/bg/bg_bar_entrada.png", xysize=(1920, 1080), fit="cover")
image bg barra = Transform("images/bg/bg_bar_barra.png", xysize=(1920, 1080), fit="cover")
image bg mesa = Transform("images/bg/bg_bar_mesa.png", xysize=(1920, 1080), fit="cover")
image bg mesa tardia = Transform("images/bg/bg_bar_mesa_tardia.png", xysize=(1920, 1080), fit="cover")

image pedro neutro = "images/char/pedro_neutro.png"
image pedro ironico = "images/char/pedro_ironico.png"
image pedro resentido = "images/char/pedro_resentido.png"
image pedro vulnerable = "images/char/pedro_vulnerable.png"
image pedro furia = "images/char/pedro_furia.png"

image alex neutro = "images/char/alex_neutro.png"
image alex admiracion = "images/char/alex_admiracion.png"
image alex incomodo = "images/char/alex_incomodo.png"

image cg espejo = Transform("images/cg/cg_espejo.png", xysize=(1920, 1080), fit="cover")
image cg f01a = Transform("images/cg/cg_f01a.png", xysize=(1920, 1080), fit="cover")
image cg f01b = Transform("images/cg/cg_f01b.png", xysize=(1920, 1080), fit="cover")
image cg f02 = Transform("images/cg/cg_f02.png", xysize=(1920, 1080), fit="cover")
image cg f03 = Transform("images/cg/cg_f03.png", xysize=(1920, 1080), fit="cover")
image cg f03b = Transform("images/cg/cg_f03b.png", xysize=(1920, 1080), fit="cover")

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
