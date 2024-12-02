``` bash
# Casos de prueba para el análisis de KEGG y funciones asociadas

## Caso de prueba 1: Función limpiar_ids_kegg con lista de IDs válidos

# Comando:
python script.py

# Descripción:
La función `limpiar_ids_kegg` recibe una lista de identificadores KEGG con espacios adicionales.

# Resultado esperado:
- La salida debe ser una lista de identificadores KEGG sin espacios adicionales, con los espacios reemplazados por '%20'.
- Ejemplo de entrada: ["C00031 ", " C00032"]
- Ejemplo de salida esperada: ["C00031", "C00032"]

---

## Caso de prueba 2: Función obtener_nombre_metabolito con un ID válido

# Comando:
python script.py

# Descripción:
La función `obtener_nombre_metabolito` consulta el nombre de un metabolito usando un ID válido de KEGG.

# Resultado esperado:
- La función debe devolver el nombre del metabolito asociado con el ID proporcionado.
- Ejemplo de entrada: "C00031"
- Ejemplo de salida esperada: "Glucosa"

---

## Caso de prueba 3: Función obtener_nombre_metabolito con un ID no válido

# Comando:
python script.py

# Descripción:
La función `obtener_nombre_metabolito` consulta un ID de metabolito no válido.

# Resultado esperado:
- La función debe devolver "Nombre desconocido" cuando el ID no sea válido o no exista.

---

## Caso de prueba 4: Función obtener_rutas con un ID de metabolito válido

# Comando:
python script.py

# Descripción:
La función `obtener_rutas` consulta las rutas metabólicas asociadas con un ID de metabolito válido.

# Resultado esperado:
- La función debe devolver una lista de identificadores de las rutas metabólicas asociadas.
- Ejemplo de entrada: "C00031"
- Ejemplo de salida esperada: ["path:map00010", "path:map00020"]

---

## Caso de prueba 5: Función obtener_rutas con un ID de metabolito sin rutas asociadas

# Comando:
python script.py

# Descripción:
La función `obtener_rutas` consulta un ID de metabolito que no tiene rutas metabólicas asociadas.

# Resultado esperado:
- La función debe devolver una lista vacía `[]` si no se encuentran rutas metabólicas asociadas.

---

## Caso de prueba 6: Función obtener_nombre_rutas con una ruta válida

# Comando:
python script.py

# Descripción:
La función `obtener_nombre_rutas` consulta el nombre de una ruta metabólica usando un ID de ruta válido.

# Resultado esperado:
- La función debe devolver el nombre de la ruta metabólica asociada.
- Ejemplo de entrada: "path:map00010"
- Ejemplo de salida esperada: "Glycolysis / Gluconeogenesis"

---

## Caso de prueba 7: Función obtener_nombre_rutas con un ID de ruta no válido

# Comando:
python script.py

# Descripción:
La función `obtener_nombre_rutas` consulta un ID de ruta metabólica no válido.

# Resultado esperado:
- La función debe devolver "Nombre desconocido" cuando el ID de la ruta no sea válido o no exista.

---

## Caso de prueba 8: Manejo de errores en obtener_nombre_metabolito con conexión fallida

# Comando:
python script.py

# Descripción:
La función `obtener_nombre_metabolito` intenta consultar un metabolito cuando la conexión a KEGG falla.

# Resultado esperado:
- El script debe manejar la excepción de error de conexión y continuar sin interrumpir el proceso.
- La función debe devolver "Nombre desconocido" en caso de error.

---

## Caso de prueba 9: Manejo de errores en obtener_rutas con conexión fallida

# Comando:
python script.py

# Descripción:
La función `obtener_rutas` intenta obtener rutas metabólicas para un metabolito cuando la conexión a KEGG falla.

# Resultado esperado:
- El script debe manejar la excepción de error de conexión y continuar sin interrumpir el proceso.
- La función debe devolver una lista vacía `[]` en caso de error.

---

## Caso de prueba 10: Limpieza de IDs KEGG con espacios y caracteres especiales

# Comando:
python script.py

# Descripción:
La función `limpiar_ids_kegg` recibe una lista de identificadores con espacios y caracteres especiales.

# Resultado esperado:
- La salida debe ser una lista de identificadores KEGG formateados correctamente, donde los espacios sean reemplazados por '%20'.
- Ejemplo de entrada: ["C00031 ", "C00032 ", " C00033", "C#00034"]
- Ejemplo de salida esperada: ["C00031", "C00032", "C00033", "C%2300034"]

---

## Caso de prueba 11: Obtener rutas metabólicas para metabolitos con rutas duplicadas

# Comando:
python script.py

# Descripción:
La función `obtener_rutas` recibe un metabolito con varias rutas metabólicas asociadas, algunas de ellas duplicadas.

# Resultado esperado:
- La salida debe ser una lista de rutas únicas, eliminando cualquier ruta duplicada.
- Ejemplo de entrada: "C00031"
- Ejemplo de salida esperada: ["path:map00010", "path:map00020"]

---

## Caso de prueba 12: Varias consultas a KEGG con IDs distintos

# Comando:
python script.py

# Descripción:
El script consulta varios metabolitos para obtener sus nombres y rutas metabólicas, realizando múltiples peticiones a KEGG.

# Resultado esperado:
- El script debe manejar múltiples consultas sin errores y mostrar correctamente los nombres y rutas para cada metabolito.
- Ejemplo de entrada: ["C00031", "C00032"]
- Ejemplo de salida esperada: Nombre de metabolito y rutas para cada ID.

---

```