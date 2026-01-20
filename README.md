# Procesadores-de-Lenguajes
---
## ¿Cómo ejecutar el Procesador?
(Se presupone la carpeta "EntregaGrupoPERL" como raíz del repositorio)
El procesador se ejecuta automáticamente con cada commit realizado al repositorio. Este toma las "órdenes" de cómo tiene que hacer las cosas del archivo "argumentos.txt", situado en la raíz de éste repositorio.
El archivo se compone de 3 líneas:
  - Qué analizador se quiere utilizar
    - "ANTLR" (Analizador descendente implementado con ANTLR4)
    - "CUP" (Analizador ascendente implementado con JFlex y Cup)
  - Qué archivo .cv queremos que convierta en html
    - Se debe de colocar dicho archivo en la carpeta de "entradas"
  - Qué plantilla .html se quiere utilizar
    - Se debe de colocar dicha plantilla en la carpeta de "templates"
---
## ¿Cómo escribo un Currículum en un archivo .cv?
La especificación del lenguaje se encuentra en el archivo "EBNF", dentro de la carpeta "gramatica".
También se encuentra descrito en el archivo "Procesadores_de_Lenguaje.pdf"
