# JogoPro — novela visual (demo)

Novela visual sobre las contradicciones entre los valores que defendemos y las decisiones que tomamos. Tres decisiones (`D01`–`D03`), tres variables narrativas (Resentimiento, Confianza, Lucidez) y cinco finales.

- Diseño narrativo: [`Historia.md`](Historia.md) y [`ArbolDecisiones.md`](ArbolDecisiones.md) (árbol técnico con la matriz de 27 rutas).
- Guion: [`Dialogos.md`](Dialogos.md) — todos los diálogos por escena con sus condiciones.
- Arte: [`PromptsArte.md`](PromptsArte.md) — los 25 prompts completos para generar las imágenes.
- Motor: Ren'Py 8.5.x, 1920×1080.

## Estructura

```
game/
├── script.rpy          # inicio + S00 (prólogo)
├── definitions.rpy     # personajes, transforms e imágenes (placeholders de color)
├── variables.rpy       # res / conf / luc, banderas, helpers
├── escenas/            # S01–S04 con las decisiones
├── finales/            # F01a, F01b, F02, F03, F03b
├── pantallas/          # galería de finales y HUD de debug (tecla K)
├── testcases.rpy       # pruebas automatizadas de rutas
└── images/             # arte: bg/, char/, cg/, fx/ (ver ArbolDecisiones.md §9)
```

## Cómo ejecutar

```bash
# SDK instalado en ~/renpy-sdk
~/renpy-sdk/renpy.sh /home/morfeo/Documentos/Interfaces/JogoPro
```

O abrir la carpeta del proyecto desde el launcher de Ren'Py.

## Validación

```bash
~/renpy-sdk/renpy.sh /home/morfeo/Documentos/Interfaces/JogoPro lint    # análisis estático
~/renpy-sdk/renpy.sh /home/morfeo/Documentos/Interfaces/JogoPro compile # precompilar .rpyc
~/renpy-sdk/renpy.sh /home/morfeo/Documentos/Interfaces/JogoPro test    # pruebas de rutas (6 casos)
```

## Estado actual

- [x] Fases 0–5 y 7 del plan: flujo completo jugable, variables, 5 finales, galería con persistencia, tests.
- [ ] Fase 6: arte real — reemplazar los placeholders de color en `definitions.rpy` por los PNG listados en `ArbolDecisiones.md` §9 (las rutas destino ya están creadas).
- [ ] Audio opcional: los `play music`/`play sound` están comentados en las escenas.

## Depuración

- Tecla `K` en partida (solo con `config.developer`): muestra `res/conf/luc`, las decisiones tomadas y las banderas.
- Consola: `Shift+O`.
