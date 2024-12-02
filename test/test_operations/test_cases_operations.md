
``` bash
# Casos de prueba para prueba_shapiro

## Caso de prueba 1: DataFrame con valores numéricos válidos
df = pd.DataFrame({
    "Grupo1": [1.2, 2.3, 3.1, 4.5],
    "Grupo2": [5.0, 6.2, 7.1, 8.3]
})
prueba_shapiro(df)
# Resultado esperado:
# Columna        W-Estadistica    P-Value    Normalidad
# Grupo1         <valor>          <valor>    Normal/No Normal
# Grupo2         <valor>          <valor>    Normal/No Normal

## Caso de prueba 2: DataFrame con valores faltantes (NaN)
df = pd.DataFrame({
    "Grupo1": [1.2, np.nan, 3.1, 4.5],
    "Grupo2": [np.nan, 6.2, 7.1, np.nan]
})
prueba_shapiro(df)
# Resultado esperado:
# Los NaN son excluidos. Las columnas con todos los NaN podrían ser omitidas o retornar un error.

## Caso de prueba 3: DataFrame con una sola columna
df = pd.DataFrame({"Grupo1": [1.2, 2.3, 3.1, 4.5]})
prueba_shapiro(df)
# Resultado esperado:
# Resultados válidos para la única columna.

## Caso de prueba 4: DataFrame con datos no numéricos
df = pd.DataFrame({"Grupo1": ["a", "b", "c"], "Grupo2": [1, 2, 3]})
prueba_shapiro(df)
# Resultado esperado:
# La función debería ignorar las columnas no numéricas o manejar con un mensaje de error.

# Casos de prueba para prueba_kruskal

## Caso de prueba 1: Dos grupos independientes con diferencias significativas
grupo1 = [1.2, 2.3, 3.1]
grupo2 = [4.5, 5.6, 6.7]
prueba_kruskal(grupo1, grupo2)
# Resultado esperado:
# H-Statistic    P-Value    Interpretación
# <valor>        <valor>    Significativa/No significativa

## Caso de prueba 2: Tres grupos con diferencias no significativas
grupo1 = [1, 1, 1]
grupo2 = [2, 2, 2]
grupo3 = [3, 3, 3]
prueba_kruskal(grupo1, grupo2, grupo3)
# Resultado esperado:
# H-Statistic    P-Value    Interpretación
# <valor>        <valor>    No significativa

## Caso de prueba 3: Grupos con tamaños desiguales
grupo1 = [1, 2, 3]
grupo2 = [4, 5, 6, 7, 8]
prueba_kruskal(grupo1, grupo2)
# Resultado esperado:
# La función debe manejar correctamente tamaños desiguales.

# Casos de prueba para prueba_posthoc_dunn

## Caso de prueba 1: Tres grupos independientes con diferencias significativas
grupos = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
nombres_grupos = ["Grupo1", "Grupo2", "Grupo3"]
prueba_posthoc_dunn(grupos, nombres_grupos)
# Resultado esperado:
# Grupo 1    Grupo 2    P-Value    Interpretación
# <nombre>   <nombre>   <valor>    Significativa/No significativa

## Caso de prueba 2: Grupos con un solo valor
grupos = [[1], [2], [3]]
nombres_grupos = ["Grupo1", "Grupo2", "Grupo3"]
prueba_posthoc_dunn(grupos, nombres_grupos)
# Resultado esperado:
# La función debería manejar este caso con un mensaje de error o un DataFrame vacío.

## Caso de prueba 3: Grupos con tamaños desiguales
grupos = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
nombres_grupos = ["Grupo1", "Grupo2", "Grupo3"]
prueba_posthoc_dunn(grupos, nombres_grupos)
# Resultado esperado:
# Resultados válidos, manejando tamaños desiguales correctamente.
```