################################################################################
## Variables narrativas
##
## ArbolDecisiones.md, sección 2:
##   res  = Resentimiento de Pedro (0-6, inicial 1)
##   conf = Confianza de Pedro     (0-2, inicial 0)
##   luc  = Lucidez de Gabriel     (0-2, inicial 0)
##
## Los valores nunca se muestran al jugador; solo la pantalla de debug (tecla K,
## solo en desarrollo) los expone.

default res = 1
default conf = 0
default luc = 0

## Banderas narrativas: alteran texto, no aritmética.
default flag_desprecio = False
default flag_evasion = False
default flag_imprevisible = False
default flag_alcohol = False

## Registro de decisiones para las variantes de diálogo.
default respuesta_d01 = ""
default respuesta_d02 = ""
default eleccion_d03 = ""

## Finales desbloqueados para la galería (persisten entre partidas).
default persistent.finales = []


init python:

    def ajustar(res_d=0, conf_d=0, luc_d=0):
        """Aplica deltas con saturación según los límites del árbol."""
        store.res = max(0, min(6, store.res + res_d))
        store.conf = max(0, min(2, store.conf + conf_d))
        store.luc = max(0, min(2, store.luc + luc_d))

    def desbloquear_final(fid):
        """Registra un final en la galería si aún no está descubierto."""
        if fid not in persistent.finales:
            persistent.finales.append(fid)
