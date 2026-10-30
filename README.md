# Code Relay · Hacktoberfest

Página de proyección para participantes de IEEE HKN Nu Zeta, ESPOL. Contiene los 10 retos de la actividad Code Relay, organizados por dificultad: 4 fáciles, 4 intermedios y 2 difíciles.

El tablero se abre directamente. Seleccionar un reto muestra su enunciado, condiciones, datos de ejemplo y salida esperada. No hay registro, envío de respuestas, ejecución de código ni soluciones publicadas.

## Proyectar

- `F`: pantalla completa. También se puede usar F11 del navegador.
- `←` / `→`: reto anterior y siguiente, ordenados por dificultad.
- `Esc`: volver al tablero.
- Altavoz: volumen y silencio. Por las políticas del navegador, la música puede requerir una primera interacción.

La página reutiliza MedievalSharp, Georgia, la paleta medieval, logotipos y música de las páginas de Human vs AI y Código Secreto del mismo evento. Las pistas de bienvenida y de torneo se reproducen en secuencia; la pista de torneo se repite.

## Vista local

Desde este directorio: `python -m http.server 8080 --directory public`. Abrir http://localhost:8080.

## Render

Crear un **Static Site** desde la rama `main`, con comando de compilación `echo "Static site ready"` y directorio de publicación `public`. No requiere dependencias ni servidor. Se usan fragmentos `#CR-01` para enlaces directos, sin reglas de reescritura.

## Contenido

Los enunciados proceden de la sección Actividad 1 del documento HACKTOBERFEST_ORDENADO.docx. `public/challenges.json` incluye únicamente información para participantes. Se reconstruyó el espaciado del ejemplo de pirámide y se incluyó el tablero inicial de Tetris indicado en la guía para que el reto sea autosuficiente. El documento original y las soluciones no forman parte del sitio.

`prepare_content.py` regenera los enunciados si el documento original sigue en la carpeta Downloads, dos niveles por encima de este repositorio. No se ejecuta durante el despliegue.
