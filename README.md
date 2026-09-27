# c0ffeebabe

Experimento en **Python** que busca cadenas cuyo **hash MD5** "coincide" con la propia entrada, usando una lista de **números mágicos** hex (`0xDEADBEEF`, `0xCAFEBABE`, `0xC0FFEEBABE`, …).

## Cómo funciona

1. Lee `wordlist.txt` (una palabra/hex por línea) y, para cada una, guarda dos variantes: **sin** el prefijo `0x` y en **minúsculas**.
2. Para cada palabra base, genera `n` cadenas aleatorias concatenando la palabra con números al azar (en tres formas: `palabra+rand`, `rand+palabra+rand`, `rand+palabra`).
3. Calcula el **MD5** de cada cadena (`hexdigest`).
4. Mide cuánto del **digest MD5** coincide, **como prefijo**, con la cadena de entrada (`find_collisions`), y lo expresa en **porcentaje**.
5. Si el porcentaje es **> 50%**, guarda `{ input_str, output_str, collision }` agrupado por palabra base.
6. Escribe los aciertos en un **JSON** (nombre por defecto: *timestamp*) y **repite en bucle** con un `sleep` de 1 segundo.

> **Nota:** no es una "colisión MD5" en el sentido criptográfico (dos entradas con el mismo hash). Es un **heurístico de coincidencia de prefijo** entre la entrada y su digest; las colisiones MD5 reales no se buscan así.

## `wordlist.txt`

Números mágicos clásicos:

```
0xC0FFEEBABE  0x8BADF00D  0xABADBABE  0x1BADB002  0xBAADF00D  0xBADCAB1E
0xBEADFACE    0xCAFEBABE  0xCAFED00D  0xDEADBABE  0xDEADBEEF  0xDEADDEAD
0xDEADFA11    0xDEFEC8ED  0xFEE1DEAD  0xFEEDCAFE  0xFEEDFACE  0xC0FFEE
0xE011CFD0    0xFACE8D    0xFEEE      0xCCCCCCC
```

## Requisitos

- **Python 3** (solo biblioteca estándar: `argparse`, `hashlib`, `json`, `logging`, `random`, `re`, `time`, `calendar`).

## Uso

```bash
python c0ffeebabe.py
# con opciones:
python c0ffeebabe.py -i wordlist.txt -n 10000 -d 1000000000 -o salida.json
```

| Argumento | Por defecto | Descripción |
|---|---|---|
| `-i`, `--input` | `wordlist.txt` | Archivo de lista de palabras. |
| `-n`, `--iterations` | `10000` | Iteraciones por palabra. |
| `-d`, `--dispersion` | `1000000000` | Rango de los números aleatorios. |
| `-o`, `--output` | *(timestamp)* | Archivo JSON de salida. |

## Salida

Un **JSON** (por defecto `<timestamp>.json`) con las cadenas que superaron el 50% de coincidencia:

```json
{
  "0xDEADBEEF": [
    { "input_str": "...", "output_str": "...", "collision": 62.5 }
  ]
}
```

## Estado

⚠️ **El archivo `c0ffeebabe.py` de este repo no ejecuta tal cual.** Está **desformateado** (perdió la indentación por completo) y además la línea de `hashlib.md5(...)` quedó **con dos sentencias pegadas**, más `if name == 'main'` (debería ser `if __name__ == "__main__":`). Hay que **corregir el formato/sintaxis** antes de usarlo.

## Licencia

Sin licencia definida. Experimento; úsalo bajo tu responsabilidad.
