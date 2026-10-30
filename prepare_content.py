"""Extract participant statements only; never publish the source document or solutions."""
from pathlib import Path
import re, json, zipfile, xml.etree.ElementTree as ET

root = Path(__file__).parent
with zipfile.ZipFile(root.parent.parent / 'HACKTOBERFEST_ORDENADO.docx') as z:
    xml = ET.fromstring(z.read('word/document.xml'))
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
lines = [''.join(t.text or '' for t in p.findall('.//w:t', ns)).strip() for p in xml.findall('.//w:p', ns)]
lines = lines[:next(i for i, s in enumerate(lines) if s.startswith('Actividad 2.'))]
starts = [i for i, s in enumerate(lines) if re.match(r'Reto \d+:', s)]
examples = [
 ('Jugador 1: piedra\nJugador 2: tijera', 'Jugador 1 gana'),
 ('Altura: 4', '   *\n  ***\n *****\n*******'),
 ('votos = ["Rojo", "Azul", "Rojo",\n         "Verde", "Rojo", "Azul"]', 'Expulsado: Rojo (3 votos)'),
 ('Código recibido: H1O1L1A3', 'Mensaje recuperado: HOLAAA\nTotal de caracteres: 6'),
 ('inventario = {"madera": 12, "piedra": 7, "hierro": 4}\nrecetas = {\n  "pico": {"madera": 2, "piedra": 3},\n  "espada": {"madera": 1, "hierro": 2}\n}\npedido = {"pico": 2, "espada": 1}', 'Pedido fabricado\nInventario final:\n{\'madera\': 7, \'piedra\': 1, \'hierro\': 2}'),
 ('Vuelta 1: 45.5\nVuelta 2: 42.1\nVuelta 3: 43.0', 'Tiempo total: 130.6\nVuelta más rápida: 42.1'),
 ('Mensaje: Hola Equipo', 'Mensaje secreto: h0l@ 3q#1p0'),
 ('Ataque: Agua\nDefensor: Fuego\nDaño base: 40', '¡Súper efectivo!\nDaño final: 80'),
 ('Límite: 15\nPesos: [5, 3, 4, 6, 2]', 'Objetos recogidos: 3\nPeso total en alforja: 12'),
 ('tablero = [\n  [0, 1, 0, 0],\n  [1, 1, 1, 1],\n  [0, 1, 1, 0],\n  [1, 1, 1, 1]\n]', 'Tablero actualizado:\n[0, 0, 0, 0]\n[0, 0, 0, 0]\n[0, 1, 0, 0]\n[0, 1, 1, 0]')
]
summaries = ['Decide quién gana la partida.', 'Dibuja una pirámide centrada.', 'Cuenta votos y detecta empates.', 'Descomprime el mensaje interceptado.', 'Comprueba recursos y fabrica el pedido.', 'Calcula el total y la vuelta más rápida.', 'Cambia las vocales por símbolos.', 'Calcula la efectividad y el daño.', 'Recoge objetos sin superar el límite.', 'Elimina las filas completas del tablero.']
items = []
for idx, start in enumerate(starts):
    block = lines[start:starts[idx+1] if idx+1 < len(starts) else len(lines)]
    match = re.match(r'Reto (\d+): (.+) \(Dificultad (.+)\)', block[0])
    def section(a, b):
        return [re.sub(r'^•\s*', '', s).strip() for s in block[block.index(a)+1:block.index(b)] if s]
    summary = ' '.join(section('Resumen', 'Condiciones'))
    conditions = section('Condiciones', 'Ejemplo de entradas y salidas')
    # Paragraph continuations in the document are joined into a single condition.
    if idx == 3:
        conditions = ['El código se recibe mediante input() y contiene pares consecutivos de una letra mayúscula seguida de un dígito entre 1 y 9.', 'Recorrer cada par y repetir la letra tantas veces como indique su número, conservando el orden original.', 'Mostrar el mensaje reconstruido y la cantidad total de caracteres obtenidos. Se garantiza que la entrada es válida.']
    items.append(dict(id=f'CR-{idx+1:02}', title=match[2], level={'fácil':'easy','intermedia':'medium','difícil':'hard'}[match[3]], summary=summary, short=summaries[idx], conditions=conditions, skills=section('Conocimientos necesarios','Solución propuesta en Python'), input=examples[idx][0], output=examples[idx][1]))
assert len(items) == 10
(root/'public'/'challenges.json').write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding='utf-8')
print('10 participant statements extracted. Solutions excluded.')
