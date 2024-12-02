``` bash

# Casos de prueba para el análisis de metabolitos de E. coli

## Caso de prueba 1: Lectura correcta del archivo de datos

# Comando:
python script.py

# Descripción:
El archivo de datos 'datos_metabolomica.xlsx' está presente y es accesible.

# Resultado esperado:
- El archivo se lee correctamente.
- No debe generar ningún error relacionado con la falta de archivo o problema de lectura.

---

## Caso de prueba 2: El archivo de datos no está presente

# Comando:
python script.py

# Descripción:
El archivo 'datos_metabolomica.xlsx' no está presente en la ruta esperada.

# Resultado esperado:
- El script debería mostrar un mensaje de error que indique que el archivo no se encuentra.
- La ejecución del script debe finalizar correctamente sin continuar con el análisis.

---

## Caso de prueba 3: Argumentos de línea de comandos con valores predeterminados

# Comando:
python script.py

# Descripción:
El script se ejecuta sin especificar las condiciones experimentales. Las condiciones predeterminadas 'asp' y 'glu' deben ser usadas.

# Resultado esperado:
- Las condiciones experimentales se establecen como 'asp' y 'glu' de manera predeterminada.
- El análisis de metabolitos se realiza utilizando estas condiciones.

---

## Caso de prueba 4: Argumentos de línea de comandos con condiciones personalizadas

# Comando:
python script.py -c1 "glu" -c2 "gal"

# Descripción:
El script se ejecuta con condiciones experimentales personalizadas: 'glucosa' y 'galactosa'.

# Resultado esperado:
- El script filtra correctamente las columnas para las condiciones 'glucosa' y 'galactosa'.
- Los resultados del análisis de metabolitos se realizan bajo estas condiciones.

---

## Caso de prueba 5: Datos con NaN (valores faltantes) en las condiciones experimentales

# Comando:
python script.py

# Descripción:
El archivo contiene NaN (valores faltantes) en algunas columnas relacionadas con metabolitos.

# Resultado esperado:
- Las funciones de análisis deben manejar correctamente los valores faltantes (por ejemplo, usando `dropna()` para eliminar datos nulos antes del análisis).
- El script debe continuar sin errores.

---

## Caso de prueba 6: Prueba de normalidad (Shapiro-Wilk) exitosa

# Comando:
python script.py

# Descripción:
El script ejecuta la prueba de normalidad sobre las condiciones de agua, 'asp' y 'glu' y todas las distribuciones siguen una distribución normal.

# Resultado esperado:
- La salida de la prueba de Shapiro-Wilk debería mostrar "Normal" para cada grupo.
- Los valores de W-Estadística y P-Value deben ser generados correctamente.

---

## Caso de prueba 7: Prueba de normalidad (Shapiro-Wilk) no normal

# Comando:
python script.py

# Descripción:
El script ejecuta la prueba de normalidad sobre las condiciones de agua, 'asp' y 'glu', y alguna de las distribuciones no es normal.

# Resultado esperado:
- La salida de la prueba de Shapiro-Wilk debería mostrar "No Normal" para al menos un grupo.
- Los valores de W-Estadística y P-Value deben ser generados correctamente.

---

## Caso de prueba 8: Prueba de Kruskal-Wallis exitosa

# Comando:
python script.py

# Descripción:
El script realiza una prueba de Kruskal-Wallis entre los promedios de las condiciones experimentales.

# Resultado esperado:
- La salida debe contener la estadística H y el valor P de la prueba de Kruskal-Wallis.
- El script debería interpretar si la diferencia entre los grupos es significativa o no.

---

## Caso de prueba 9: Prueba de Dunn post-hoc con diferencias significativas

# Comando:
python script.py

# Descripción:
El script realiza una prueba de Dunn post-hoc cuando la prueba de Kruskal-Wallis muestra diferencias significativas entre los grupos.

# Resultado esperado:
- El resultado de la prueba de Dunn debe contener pares de grupos con diferencias significativas (con un valor p < 0.05).
- El script debe interpretar correctamente los resultados de la prueba post-hoc.

---

## Caso de prueba 10: Análisis de rutas metabólicas exitoso

# Comando:
python script.py

# Descripción:
El script realiza correctamente el análisis de rutas metabólicas para los metabolitos presentes en el archivo de datos, extrayendo y contando las frecuencias de las rutas asociadas.

# Resultado esperado:
- El script debe mostrar los metabolitos, sus rutas asociadas y las rutas más frecuentes.
- El gráfico de barras debe mostrar las rutas metabólicas y sus frecuencias.

---

## Caso de prueba 11: Error al procesar los IDs de KEGG

# Comando:
python script.py

# Descripción:
El archivo contiene errores en los IDs de KEGG (por ejemplo, IDs mal formateados o desconocidos).

# Resultado esperado:
- El script debería manejar el error y continuar, mostrando un mensaje de error para cada metabolito con problemas de ID.
- El análisis debe proceder con los metabolitos válidos.

---

## Caso de prueba 12: Error al obtener las rutas metabólicas

# Comando:
python script.py

# Descripción:
Algunos metabolitos no tienen rutas metabólicas asociadas o la función de obtención de rutas falla.

# Resultado esperado:
- El script debe manejar el error sin detenerse completamente y seguir procesando los metabolitos restantes.
- Los metabolitos sin rutas metabólicas pueden ser indicados con un mensaje de advertencia.

---

## Caso de prueba 13: Visualización de las frecuencias de rutas metabólicas

# Comando:
python script.py

# Descripción:
El script debe generar un gráfico de barras horizontal mostrando las frecuencias de las rutas metabólicas.

# Resultado esperado:
- El gráfico debe mostrar las rutas metabólicas en el eje y y sus frecuencias en el eje x.
- El gráfico debe tener una visualización clara con etiquetas legibles y debe estar invertido en el eje y.

---

## Caso de prueba 14: Sin datos de rutas metabólicas

# Comando:
python script.py

# Descripción:
El archivo no contiene datos de rutas metabólicas válidos o todos los metabolitos están asociados a rutas no válidas.

# Resultado esperado:
- El script debe mostrar un mensaje indicando que no se encontraron rutas metabólicas y no generar el gráfico de barras.

---

```