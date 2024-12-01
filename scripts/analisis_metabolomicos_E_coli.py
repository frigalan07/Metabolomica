'''
Nombre:
    Análisis metabolómicos de E. Coli

Version:
    

Autor:
    Galán Hernández Frida
    García González Carlos

Descripcion:
    Este script esta hecho en Python  y tienen la funcionalidad de analizar datos de metabolitos de Escherichia coli en diferentes condiciones experimentales. 
    Utiliza bibliotecas estándar de Python, así como herramientas especializadas como Biopython, pandas y SciPy, para realizar análisis estadísticos y 
    explorar rutas metabólicas. Inicialmente, se procesan argumentos de línea de comandos para seleccionar dos condiciones de interés. Luego, se cargan 
    y filtran los datos provenientes de un archivo Excel, eliminando columnas irrelevantes. El script evalúa la normalidad de las distribuciones 
    mediante la prueba de Shapiro-Wilk y compara los grupos utilizando la prueba de Kruskal-Wallis y un análisis post hoc de Dunn.

    Además, el código incluye funciones para interactuar con la base de datos KEGG, permitiendo obtener nombres de metabolitos y rutas metabólicas asociadas. 
    Posteriormente, los resultados se visualizan en un gráfico de barras horizontal que muestran la frecuencia de las rutas metabólicas identificadas. 
    El programa también cuenta con manejo de errores para garantizar que se puedan identificar problemas durante el análisis, como fallos en las consultas 
    a KEGG o datos faltantes. Esta herramienta es ideal para investigadores interesados en el análisis comparativo de metabolitos y sus implicaciones 
    metabólicas.

Argumentos:
    - c1: Primera condición en la que se encuentran los metabolitos, por defecto es 'asp'
    - c2: Segunda condición en la que se encuentran los metabolitos, por defecto es 'glu'

Usage:
    python scripts/analisis_metabolomicos_E_coli.py -c1 CONDICION1 -c2 CONDICION2
    python3 scripts/analisis_metabolomicos_E_coli.py -c1  -c2 

'''
# Importaciones estándar de Python
import argparse
import sys
from collections import Counter

# Librerías de terceros (instaladas vía pip)
import pandas as pd
import matplotlib.pyplot as plt
import requests
import scipy.stats as stats
import scikit_posthocs as sp

# Importaciones específicas de Biopython
from Bio.KEGG import REST


# Se parsean los argumentos usando la libreria de argparse
parser = argparse.ArgumentParser(
    description="El siguiente script analiza datos de metabolitos de E. coli"
)

parser.add_argument("-c1", "--CONDICION1",
                    help="Especifica la primera condición experimental para el análisis de los metabolitos, por defecto 'asp'",
                    type=str,
                    default="asp",
                    required=False)

parser.add_argument("-c2", "--CONDICION2",
                    help="Especifica la segunda condición experimental para el análisis de los metabolitos, por defecto 'glu'",
                    type=str,
                    default="glu",
                    required=False)

args = parser.parse_args()


def prueba_shapiro(df):
    """
    Realiza la prueba de Shapiro-Wilk para cada columna de un DataFrame.

    Args:
    - df (pd.DataFrame): DataFrame cuyas columnas serán analizadas.

    Returns:
    - pd.DataFrame: Resultados de normalidad para cada columna.
    """
    shapiro_results = {col: stats.shapiro(df[col].dropna()) for col in df.columns}

    shapiro_df = pd.DataFrame(
        {
            "Columna": shapiro_results.keys(),
            "W-Estadistica": [result[0] for result in shapiro_results.values()],
            "P-Value": [result[1] for result in shapiro_results.values()],
            "Normalidad": [
                "Normal" if result[1] > 0.05 else "No Normal"
                for result in shapiro_results.values()
            ]
        }
    )
    return shapiro_df


def prueba_kruskal(*grupos):
    """
    Realiza la prueba de Kruskal-Wallis para determinar diferencias entre varios grupos independientes.

    Args:
    - *grupos: Listas o arrays representando los grupos independientes.

    Returns:
    - pd.DataFrame: Resultados de la prueba.
    """
    stat, p_value = stats.kruskal(*grupos)
    return pd.DataFrame({
        "H-Statistic": [stat],
        "P-Value": [p_value],
        "Interpretación": ["Significativa" if p_value < 0.05 else "No significativa"]
    })


def prueba_posthoc_dunn(grupos, nombres_grupos):
    """
    Realiza la prueba post hoc de Dunn.

    Args:
    - grupos: Lista de listas con datos de cada grupo.
    - nombres_grupos: Nombres de los grupos.

    Returns:
    - pd.DataFrame: Resultados de la prueba post hoc.
    """
    datos = [dato for grupo in grupos for dato in grupo]
    etiquetas = [nombre for nombre, grupo in zip(nombres_grupos, grupos) for _ in grupo]

    dunn_results = sp.posthoc_dunn(
        pd.DataFrame({"Datos": datos, "Grupos": etiquetas}),
        val_col="Datos",
        group_col="Grupos",
        p_adjust="bonferroni"
    )

    dunn_long = dunn_results.reset_index().melt(
        id_vars="index", var_name="Grupo 2", value_name="P-Value")
    dunn_long.rename(columns={"index": "Grupo 1"}, inplace=True)
    dunn_long["Interpretación"] = dunn_long["P-Value"].apply(
        lambda p: "Significativa" if p < 0.05 else "No significativa"
    )
    return dunn_long


def limpiar_ids_kegg(ids):
    return [id.strip().replace(" ", "%20") for id in ids]


def obtener_rutas_metabolicas(id_kegg):
    try:
        # Hacer la consulta a la base de datos KEGG para obtener la información
        pathway = REST.kegg_get(f"pathway:{id_kegg}")
        
        # Parsear la respuesta y extraer las rutas metabólicas
        pathways = pathway.read().splitlines()
        
        # Filtrar y mostrar las rutas
        rutas = [line for line in pathways if "PATHWAY" in line]
        
        return rutas
    except Exception as e:
        print(f"Error al consultar KEGG para {id_kegg}: {e}")
        return []

# Función para obtener el nombre de un metabolito
def get_compound_name(compound_id):
    url = f"http://rest.kegg.jp/get/{compound_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text
        # El nombre del compuesto aparece en la línea que comienza con "NAME"
        for line in data.split("\n"):
            if line.startswith("NAME"):
                return line.split("NAME")[1].strip()
    return "Nombre desconocido"

# Función para consultar rutas metabólicas para un metabolito
def get_metabolic_pathways(compound_id):
    url = f"http://rest.kegg.jp/link/pathway/{compound_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text.strip()
        pathways = []
        for line in data.split("\n"):
            if "\t" in line:
                parts = line.split("\t")
                if len(parts) > 1:
                    pathways.append(parts[1])
        return list(set(pathways))  # Elimina duplicados
    return []

# Función para obtener el nombre de una ruta metabólica
def get_pathway_name(pathway_id):
    url = f"http://rest.kegg.jp/get/{pathway_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text
        # El nombre de la ruta aparece en la primera línea después del encabezado
        for line in data.split("\n"):
            if line.startswith("NAME"):
                return line.split("NAME")[1].strip()
        # Alternativamente, el nombre podría estar en la primera línea
        return data.split("\n")[1].strip()
    return "Nombre desconocido"

if __name__ == "__main__":
    # Ruta al archivo de datos
    ruta_archivo = "../Downloads/datos_metabolomica.xlsx"
    try:
        datos_crudos = pd.read_excel(ruta_archivo)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta_archivo}")
        sys.exit(1)

    # Filtrar columnas válidas
    datos_semilimpios = datos_crudos.loc[:, ~datos_crudos.columns.str.endswith(("sc", "EXTRA"))]
    datos_filtrados = datos_semilimpios.loc[:, datos_semilimpios.columns.str.contains(r".*\.\w{3}_.*")]

    # Condición 1 y 2
    df_condicion1 = datos_filtrados.loc[:, datos_filtrados.columns.str.contains(args.CONDICION1)]
    df_condicion2 = datos_filtrados.loc[:, datos_filtrados.columns.str.contains(args.CONDICION2)]

    # Pruebas estadísticas
    promedio_aguas = datos_crudos.filter(like="h2o").mean(axis=1)
    promedio_con1 = df_condicion1.mean(axis=1)
    promedio_con2 = df_condicion2.mean(axis=1)

    df_aguas = datos_crudos.loc[:, datos_crudos.columns.str.contains("h2o")]
    df_condicion1 = datos_filtrados.loc[:, datos_filtrados.columns.str.contains(args.CONDICION1)]
    df_condicion2 = datos_filtrados.loc[:, datos_filtrados.columns.str.contains(args.CONDICION2)]

    try:
        # Pruebas de Shapiro-Wilk
        print("Resultados de las pruebas de normalidad (Shapiro-Wilk):")
        try:
            shapiro_h2o = prueba_shapiro(df_aguas)
            shapiro_con1 = prueba_shapiro(df_condicion1)
            shapiro_con2 = prueba_shapiro(df_condicion2)

            print(f"  H2O: {shapiro_h2o}")
            print(f"  {args.CONDICION1}: {shapiro_con1}")
            print(f"  {args.CONDICION2}: {shapiro_con2}")
        except Exception as e:
            print(f"Error en la prueba de Shapiro-Wilk: {e}")

        # Pruebas estadísticas
        print("\nResultados de las pruebas estadísticas:")
        try:
            print(prueba_kruskal(promedio_aguas, promedio_con1, promedio_con2))
            dunn_result = prueba_posthoc_dunn(
                [promedio_aguas, promedio_con1, promedio_con2],
                ["H2O", args.CONDICION1, args.CONDICION2]
            )
            print(dunn_result)
        except Exception as e:
            print(f"Error en las pruebas estadísticas: {e}")

        # Análisis de rutas metabólicas
        print("\nResultados del análisis de rutas metabólicas:")
        try:
            ids_kegg = datos_crudos["KEGG ids"].dropna().tolist()
            ids_kegg_limpios = limpiar_ids_kegg(ids_kegg)

            global_pathways = []
            for compound in ids_kegg_limpios:
                try:
                    compound_name = get_compound_name(compound)
                    pathways = get_metabolic_pathways(compound)
                    global_pathways.extend(pathways)
                    print(f"Metabolito: {compound} ({compound_name})")
                    for path in pathways:
                        print(f"  {path}: {get_pathway_name(path)}")
                except Exception as e:
                    print(f"Error procesando el compuesto {compound}: {e}")

            # Contar la frecuencia de cada ruta
            ruta_frecuencias = Counter(global_pathways)

            # Convertir el contador a un DataFrame
            df_frecuencias = pd.DataFrame.from_dict(ruta_frecuencias, orient='index', columns=['Frecuencia']).reset_index()

            # Renombrar la columna 'index' a 'Ruta'
            df_frecuencias.rename(columns={'index': 'Ruta'}, inplace=True)

            # Agregar nombres de rutas al DataFrame
            df_frecuencias['Nombre de la Ruta'] = df_frecuencias['Ruta'].apply(get_pathway_name)

            # Ordenar por frecuencia descendente
            df_frecuencias = df_frecuencias.sort_values(by='Frecuencia', ascending=False)

            # Graficar
            plt.figure(figsize=(10, 8))  # Ajustar tamaño de la figura
            plt.barh(df_frecuencias['Nombre de la Ruta'], df_frecuencias['Frecuencia'], color='#E0218A')
            plt.xlabel('Frecuencia', fontsize=12)
            plt.ylabel('Ruta metabólica', fontsize=12)
            plt.title('Frecuencia de Rutas Metabólicas', fontsize=14)
            plt.gca().invert_yaxis()  # Invertir el eje Y para que las barras más altas estén arriba
            plt.xticks(rotation=90)   # Rotar los nombres en el eje X (en este caso para frecuencias, si es necesario)
            plt.tight_layout()
            plt.show()

        except Exception as e:
            print(f"Error en el análisis de rutas metabólicas: {e}")

    except Exception as main_error:
        print(f"Error general: {main_error}")
