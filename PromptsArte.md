# Prompts de arte — JogoPro

Prompts completos para generar las 25 imágenes de la demo con un generador de imágenes. Cada prompt está en inglés (los modelos rinden mejor) y es autocontenido: incluye la descripción, la iluminación de la escena y el estilo.

Destino de cada archivo: la ruta indicada dentro de `game/images/`. Nombres exactos, todo en minúsculas.

## 0. Reglas de uso

### 0.1 Sufijo de estilo (añadir AL FINAL de todos los prompts)

```text
adult anime noir illustration, muted palette of deep teal #1B2A41, amber #E0A458, wine red #6E1F2A and cream #F2E8D5, hard chiaroscuro lighting, painterly shading, subtle film grain, cinematic composition, no text, no watermark, no logos
```

### 0.2 Fichas de personaje (reemplazar el marcador donde aparezca)

`{GABRIEL}`
```text
Gabriel, 45-year-old Latino lawyer, lean build, short dark hair with grey temples, tired brown eyes, clean shaven, navy blue suit with no tie, white shirt open at the collar, gold wristwatch
```

`{PEDRO}`
```text
Pedro, 48-year-old Latino former lawyer, heavier build, three-day stubble, receding dark hair, bloodshot tired eyes, wrinkled grey shirt, dark wool coat draped over his chair
```

`{ALEXANDRE}`
```text
Alexandre, 23-year-old Latino law student, slim, short curly black hair, round glasses, olive hoodie over a white t-shirt, eager expression
```

### 0.3 Prompt negativo (si el generador lo admite)

```text
text, watermark, signature, logo, photorealistic, 3d render, chibi, multiple views, extra fingers, deformed hands, frame, border, split screen, collage
```

### 0.4 Notas técnicas

- **Fondos y CG**: generar a 1920×1080 (o 16:9 y reescalar).
- **Sprites**: generar a 1000×1080 o mayor. Los generadores no producen transparencia: pedir el personaje **sobre fondo blanco liso** y recortar el fondo después (remove.bg, Photoshop, GIMP). Composición: busto desde el pecho, cabeza entre el 6% y el 45% de la altura del lienzo, hombros cerca del 83%.
- **Continuidad**: generar primero los 8 sprites; usar el PNG aprobado de cada personaje como *imagen de referencia* (image prompt / IP-adapter) para los CG y como guía de estilo para los fondos. Es lo que mantiene a Pedro idéntico entre escenas.
- Los prompts de sprite dicen "facing slightly three-quarters, looking left" o "looking right" según a quién mira el personaje en cada montaje: Pedro mira a la derecha (hacia el centro), Alexandre mira a la izquierda (hacia el centro).

---

## 1. Fondos → `game/images/bg/`

### 1.1 `bg_ceremonia.png` — S00, cena del bufete

```text
Empty luxurious law firm ballroom at golden dusk, seen from the middle of the room: long banquet table with champagne glasses, cream marble columns, leather-bound bookshelves, tall windows with low warm golden light spilling in, subtle haze in the air, no people, symmetrical composition, the lower third of the frame kept clear and empty — adult anime noir illustration, muted palette of deep teal #1B2A41, amber #E0A458, wine red #6E1F2A and cream #F2E8D5, hard chiaroscuro lighting, painterly shading, subtle film grain, cinematic composition, no text, no watermark, no logos
```

### 1.2 `bg_bano.png` — S00, baño de la sala

```text
Empty upscale office bathroom at night, view facing a large mirror above a marble sink, white and pale green tiles, cold fluorescent ceiling light with a slight flicker feel, faint steam on the mirror edges, paper towels dispenser, deep shadows in the corners, no people, the reflection in the mirror shows only the empty room — adult anime noir illustration, muted palette of deep teal #1B2A41, amber #E0A458, wine red #6E1F2A and cream #F2E8D5, hard chiaroscuro lighting, painterly shading, subtle film grain, cinematic composition, no text, no watermark, no logos
```

### 1.3 `bg_calle.png` — S00, calle nocturna

```text
Narrow city street at night after rain, wet asphalt reflecting sodium orange streetlamps, a vertical neon bar sign with unreadable letters at the far end of the alley, dumpsters and iron railings, puddles, deep teal shadows between the amber pools of light, no people — adult anime noir illustration, muted palette of deep teal #1B2A41, amber #E0A458, wine red #6E1F2A and cream #F2E8D5, hard chiaroscuro lighting, painterly shading, subtle film grain, cinematic composition, no text, no watermark, no logos
```

### 1.4 `bg_bar_entrada.png` — S01, interior desde la puerta

```text
Interior of a small old-fashioned bar seen from the entrance door: dark wooden bar counter on the right with backlit amber liquor bottles, hanging warm tungsten lamps, empty tables and worn wooden floor toward the back, faint cigarette smoke haze in the air, green bottle walls, cozy but melancholic, no people, lower half of the frame kept clear for characters — adult anime noir illustration, muted palette of deep teal #1B2A41, amber #E0A458, wine red #6E1F2A and cream #F2E8D5, hard chiaroscuro lighting, painterly shading, subtle film grain, cinematic composition, no text, no watermark, no logos
```

### 1.5 `bg_bar_barra.png` — opcional, primer plano de la barra

```text
Close-up of an old bar counter at night: two whiskey glasses, an open whiskey bottle, folded coaster, blurred backlit liquor bottles and an amber-lit mirror behind, warm tungsten reflections on the wood, no people, no faces, shallow depth of field — adult anime noir illustration, muted palette of deep teal #1B2A41, amber #E0A458, wine red #6E1F2A and cream #F2E8D5, hard chiaroscuro lighting, painterly shading, subtle film grain, cinematic composition, no text, no watermark, no logos
```

### 1.6 `bg_bar_mesa.png` — S02–S04, mesa del rincón (fondo principal)

```text
Corner table of an old bar at night against a dark green bottle-colored wall with old framed photographs: single hanging lamp low above the table creating a pool of amber light, two leather chairs facing each other, two glasses and a whiskey bottle on the round wooden table, rain-streaked window on the left, deep teal darkness in the background, faint smoke, no people, the space in front of the wall left empty for characters — adult anime noir illustration, muted palette of deep teal #1B2A41, amber #E0A458, wine red #6E1F2A and cream #F2E8D5, hard chiaroscuro lighting, painterly shading, subtle film grain, cinematic composition, no text, no watermark, no logos
```

### 1.7 `bg_bar_mesa_tardia.png` — S04, cierre del bar

Same as 1.6 but:

```text
Same corner table of an old bar at closing time, later at night: the bar almost empty in the background, chairs stacked on distant tables, all lights off except the single lamp above this table, denser smoke haze, the room sinking from amber into cold teal, rain still on the window, no people — adult anime noir illustration, muted palette of deep teal #1B2A41, amber #E0A458, wine red #6E1F2A and cream #F2E8D5, hard chiaroscuro lighting, painterly shading, subtle film grain, cinematic composition, no text, no watermark, no logos
```

---

## 2. Sprites → `game/images/char/`

Instrucción común para los 8 (añadir al final de cada uno):

```text
waist-up bust character sprite, centered, facing slightly three-quarters, plain solid white background for later cutout, clean lineart, cel shading, sharp focus, no props in hands, no cropped edges — adult anime noir illustration, muted palette of deep teal #1B2A41, amber #E0A458, wine red #6E1F2A and cream #F2E8D5, hard chiaroscuro lighting, painterly shading, no text, no watermark
```

*(Los sprites usan iluminación de la escena "mesa": clave ámbar lateral izquierda, sombras teal.)*

### 2.1 `pedro_neutro.png`

```text
Character sprite of {PEDRO}, waist-up bust facing slightly three-quarters and looking right with a neutral listening expression, tired but calm, hands not visible — [instrucción común]
```

### 2.2 `pedro_ironico.png`

```text
Character sprite of {PEDRO}, waist-up bust facing slightly three-quarters and looking right with a bitter half-smile, one raised eyebrow, ironic mocking expression — [instrucción común]
```

### 2.3 `pedro_resentido.png`

```text
Character sprite of {PEDRO}, waist-up bust facing slightly three-quarters and looking right with a resentful expression, tense jaw, narrowed eyes, speaking through his teeth — [instrucción común]
```

### 2.4 `pedro_vulnerable.png`

```text
Character sprite of {PEDRO}, waist-up bust facing slightly three-quarters and looking right, vulnerable expression, teary bloodshot eyes looking away for a moment, shoulders slightly sunken, exhausted honesty — [instrucción común]
```

### 2.5 `pedro_furia.png`

```text
Character sprite of {PEDRO}, waist-up bust facing slightly three-quarters and looking right, furious expression, wide bloodshot eyes, gritted teeth, leaning slightly forward, veins on temple — [instrucción común]
```

### 2.6 `alex_neutro.png`

```text
Character sprite of {ALEXANDRE}, waist-up bust facing slightly three-quarters and looking left, neutral curious expression — [instrucción común]
```

### 2.7 `alex_admiracion.png`

```text
Character sprite of {ALEXANDRE}, waist-up bust facing slightly three-quarters and looking left, admiring expression, bright-eyed smile of a fan meeting his idol — [instrucción común]
```

### 2.8 `alex_incomodo.png`

```text
Character sprite of {ALEXANDRE}, waist-up bust facing slightly three-quarters and looking left, uncomfortable expression, apologetic half-smile, slightly hunched shoulders, eyes glancing away — [instrucción común]
```

---

## 3. CG → `game/images/cg/`

### 3.1 `cg_espejo.png` — S00, el reflejo

```text
Cinematic illustration: {GABRIEL} seen from the chest up, facing his own sharp reflection in a large bathroom mirror, loosened tie hanging open, suit jacket slightly wrinkled, looking down at the sink instead of at his eyes, cold green fluorescent light from above, blurred white-green tiles behind, his reflection perfectly sharp while his back is in soft focus — adult anime noir illustration, muted palette of deep teal #1B2A41, amber #E0A458, wine red #6E1F2A and cream #F2E8D5, hard chiaroscuro lighting, painterly shading, subtle film grain, cinematic composition, no text, no watermark, no logos
```

### 3.2 `cg_f01a.png` — F01a, la confesión

```text
Cinematic illustration, side view of the corner table at dawn: {PEDRO} sitting on the left listening with a guarded, unreadable expression, {GABRIEL} on the right leaning forward and pushing a manila document envelope across the table toward him, first pale sunlight entering through the window mixing with the warm amber table lamp, two empty glasses, quiet and heavy atmosphere — adult anime noir illustration, muted palette of deep teal #1B2A41, amber #E0A458, wine red #6E1F2A and cream #F2E8D5, hard chiaroscuro lighting, painterly shading, subtle film grain, cinematic composition, no text, no watermark, no logos
```

### 3.3 `cg_f01b.png` — F01b, la verdad a destiempo

```text
Cinematic illustration, wide shot: {GABRIEL} sitting alone at the corner bar table in cold blue light, an untouched manila envelope in front of him, the chair across the table empty and pushed back, Pedro's unfinished glass left behind, the bar empty around him, no warm light left, only the pale street lamp through the window — adult anime noir illustration, muted palette of deep teal #1B2A41, amber #E0A458, wine red #6E1F2A and cream #F2E8D5, hard chiaroscuro lighting, painterly shading, subtle film grain, cinematic composition, no text, no watermark, no logos
```

### 3.4 `cg_f02.png` — F02, el último argumento

```text
Cinematic illustration, dramatic low angle at the corner table: {PEDRO} standing up and leaning over the flipped table with clenched fists, shouting, {GABRIEL} recoiling on his chair with raised hands, a glass shattered on the floor, the whole scene bathed in deep wine-red emergency light with pitch-black shadows, violence suggested by composition only, no blood, no weapons — adult anime noir illustration, muted palette of deep teal #1B2A41, amber #E0A458, wine red #6E1F2A and cream #F2E8D5, hard chiaroscuro lighting, painterly shading, subtle film grain, cinematic composition, no text, no watermark, no logos
```

### 3.5 `cg_f03.png` — F03, la salida

```text
Cinematic illustration: {PEDRO} seen from behind as a dark silhouette walking out through the bar's glass door, backlit by the cold green-tinted street light outside, his coat heavy on his shoulders; in the blurred foreground {GABRIEL} remains seated at the corner table in the amber lamp light, looking at the door, rain streaks on the glass — adult anime noir illustration, muted palette of deep teal #1B2A41, amber #E0A458, wine red #6E1F2A and cream #F2E8D5, hard chiaroscuro lighting, painterly shading, subtle film grain, cinematic composition, no text, no watermark, no logos
```

### 3.6 `cg_f03b.png` — F03b, el precio del silencio

```text
Cinematic illustration, tilted high-angle shot: a signed check and a phone lying on the wet wooden bar table, harsh white light blazing in from the open door like a camera flash, {GABRIEL} sitting in shadow at the edge of the frame with his face half-covered by his hand, the harsh light cutting the scene into white and black with almost no soft shadow, cold and clinical — adult anime noir illustration, muted palette of deep teal #1B2A41, amber #E0A458, wine red #6E1F2A and cream #F2E8D5, hard chiaroscuro lighting, painterly shading, subtle film grain, cinematic composition, no text, no watermark, no logos
```

---

## 4. Overlays → `game/images/fx/`

Estos cuatro son efectos gráficos; si el generador de imágenes los hace mal, se pueden crear en GIMP/Photoshop en minutos.

### 4.1 `fx_vineta.png` (1920×1080)

```text
Full-frame radial vignette effect, pure black fading from fully opaque at the edges to fully transparent in the center, smooth gradient, no objects, no texture, plain black vignette overlay
```

### 4.2 `fx_grano.png` (512×512, tileable)

```text
Seamless tileable monochrome film grain texture, fine random noise, uniform, fully neutral gray, high resolution, seamless pattern
```

*(Mostrar en el juego con `alpha 0.08`.)*

### 4.3 `fx_humo.png` (512×512, tileable)

```text
Seamless tileable wispy smoke texture, soft translucent gray smoke tendrils on fully transparent or black background, no objects, uniform density
```

### 4.4 `fx_lluvia.png` (512×512, tileable)

```text
Seamless tileable rain overlay, thin diagonal white rain streaks at 15 degrees, transparent background, uniform density, motion-blurred droplets
```

---

## 5. Orden de generación recomendado

1. **Sprites de Pedro** (2.1–2.5): son el ancla visual. Aprobar el primero antes que el resto.
2. **Sprites de Alexandre** (2.6–2.8).
3. **`bg_bar_mesa.png`** (1.6): es el fondo que más tiempo en pantalla. Ajustar la paleta con este.
4. **CG** (3.1–3.6), usando los sprites como referencia de personaje.
5. **Fondos restantes** (1.1–1.5, 1.7).
6. **Overlays** (4.1–4.4).
7. Recortar transparencia de sprites, reescalar todo, guardar con los nombres exactos y mover a las carpetas de `game/images/`.
