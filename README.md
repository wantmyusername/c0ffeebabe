# c0ffeebabe

Este código es un programa de Python que busca colisiones de hash MD5 para palabras de una lista de palabras. Funciona de la siguiente manera:

1. Lee una lista de palabras desde un archivo de texto.

2. Genera un número de palabras aleatorias para cada palabra en la lista y concatena las palabras aleatorias con la palabra original.

3. Genera el hash MD5 para cada palabra concatenada y busca colisiones de hash entre ellas.

4. Si una colisión se encuentra y la tasa de colisión es mayor del 50%, se registra en una lista de salida.

5. La lista de salida se escribe en un archivo JSON con un nombre de archivo que contiene la marca de tiempo.

6. El proceso se repite indefinidamente en un ciclo infinito.

El programa acepta argumentos de línea de comandos para personalizar los valores predeterminados, como el archivo de lista de palabras, el número de iteraciones y la dispersión de las palabras aleatorias. El programa también registra mensajes de información en la consola para el seguimiento del proceso.
