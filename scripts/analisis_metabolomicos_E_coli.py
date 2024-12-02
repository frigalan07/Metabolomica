'''
Nombre:
    Análisis metabolómicos de E. Coli

Version:
    4.3.2

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
import argparse  # Para el manejo de argumentos desde la línea de comandos
from collections import Counter  # Para contar elementos en listas

# Librerías de terceros (instaladas vía pip)
import pandas as pd  # Para manipulación y análisis de datos
import matplotlib.pyplot as plt  # Para crear gráficos

import sys  # Para manejar variables y funciones del intérprete de Python
import os  # Para interactuar con el sistema operativo

# Agregar dinámicamente la raíz del proyecto a sys.path usando rutas relativas
script_dir = os.path.dirname(__file__)  # Carpeta donde está el script actual
project_root = os.path.abspath(os.path.join(script_dir, ".."))  # Subir un nivel a la raíz del proyecto
sys.path.append(project_root)  # Agregar la raíz del proyecto a sys.path

# Importar funciones personalizadas de módulos locales
from operations.pruebas_estadisticas import prueba_shapiro, prueba_kruskal, prueba_posthoc_dunn
from utils.file_io import limpiar_ids_kegg, obtener_nombre_metabolito, obtener_rutas, obtener_nombre_rutas

# Configuración de los argumentos que se pueden pasar al script
parser = argparse.ArgumentParser(
    description="El siguiente script analiza datos de metabolitos de E. coli"
)

# Argumento opcional para la primera condición experimental
parser.add_argument("-c1", "--CONDICION1",
                    help="Especifica la primera condición experimental para el análisis de los metabolitos, por defecto 'asp'",
                    type=str,
                    default="asp",
                    required=False)

# Argumento opcional para la segunda condición experimental
parser.add_argument("-c2", "--CONDICION2",
                    help="Especifica la segunda condición experimental para el análisis de los metabolitos, por defecto 'glu'",
                    type=str,
                    default="glu",
                    required=False)

# Parsear los argumentos
args = parser.parse_args()

# Inicio del programa principal
if __name__ == "__main__":
    # Ruta al archivo de datos de metabolómica
    ruta_archivo = os.path.join(os.path.dirname(__file__), '..', 'docs', 'datos_metabolomica.xlsx')
    try:
        # Leer el archivo Excel con los datos crudos
        datos_crudos = pd.read_excel(ruta_archivo)
    except FileNotFoundError:
        # Manejo de error si no se encuentra el archivo
        print(f"Archivo no encontrado: {ruta_archivo}")
        sys.exit(1)

    # Filtrar columnas válidas (excluir las que terminan en "sc" o "EXTRA")
    datos_semilimpios = datos_crudos.loc[:, ~datos_crudos.columns.str.endswith(("sc", "EXTRA"))]
    # Mantener solo columnas que cumplen un patrón específico
    datos_filtrados = datos_semilimpios.loc[:, datos_semilimpios.columns.str.contains(r".*\.\w{3}_.*")]

    # Filtrar datos según las condiciones proporcionadas
    df_condicion1 = datos_filtrados.loc[:, datos_filtrados.columns.str.contains(args.CONDICION1)]
    df_condicion2 = datos_filtrados.loc[:, datos_filtrados.columns.str.contains(args.CONDICION2)]

    # Calcular promedios para distintas condiciones
    promedio_aguas = datos_crudos.filter(like="h2o").mean(axis=1)
    promedio_con1 = df_condicion1.mean(axis=1)
    promedio_con2 = df_condicion2.mean(axis=1)

    # Filtrar columnas relacionadas con agua y las condiciones
    df_aguas = datos_crudos.loc[:, datos_crudos.columns.str.contains("h2o")]

    try:
        # Realizar pruebas de normalidad (Shapiro-Wilk)
        print("Resultados de las pruebas de normalidad (Shapiro-Wilk):")
        try:
            # Probar cada grupo
            shapiro_h2o = prueba_shapiro(df_aguas)
            shapiro_con1 = prueba_shapiro(df_condicion1)
            shapiro_con2 = prueba_shapiro(df_condicion2)

            # Mostrar resultados
            print(f"  H2O: {shapiro_h2o}")
            print(f"  {args.CONDICION1}: {shapiro_con1}")
            print(f"  {args.CONDICION2}: {shapiro_con2}")
        except Exception as e:
            print(f"Error en la prueba de Shapiro-Wilk: {e}")

        # Realizar pruebas estadísticas adicionales
        print("\nResultados de las pruebas estadísticas:")
        try:
            # Prueba de Kruskal-Wallis
            print("Resultado de la prueba de Kruskal-Wallis")
            print(prueba_kruskal(promedio_aguas, promedio_con1, promedio_con2))
            # Prueba post-hoc de Dunn
            print(f"\n Resultado de la prueba posthoc de Dunn")
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
            # Obtener y limpiar los IDs de KEGG
            ids_kegg = datos_crudos["KEGG ids"].dropna().tolist()
            ids_kegg_limpios = limpiar_ids_kegg(ids_kegg)

            global_pathways = []  # Lista para almacenar todas las rutas encontradas
            for compound in ids_kegg_limpios:
                try:
                    # Obtener nombre del metabolito y sus rutas metabólicas
                    compound_name = obtener_nombre_metabolito(compound)
                    pathways = obtener_rutas(compound)
                    global_pathways.extend(pathways)

                    # Mostrar resultados para cada compuesto
                    print(f"Metabolito: {compound} ({compound_name})")
                    for path in pathways:
                        print(f"  {path}: {obtener_nombre_rutas(path)}")
                except Exception as e:
                    print(f"Error procesando el compuesto {compound}: {e}")

            # Contar frecuencia de cada ruta metabólica
            ruta_frecuencias = Counter(global_pathways)

            # Convertir el contador a un DataFrame
            df_frecuencias = pd.DataFrame.from_dict(ruta_frecuencias, orient='index', columns=['Frecuencia']).reset_index()

            # Renombrar columna para mayor claridad
            df_frecuencias.rename(columns={'index': 'Ruta'}, inplace=True)

            # Agregar nombres legibles de las rutas
            df_frecuencias['Nombre de la Ruta'] = df_frecuencias['Ruta'].apply(obtener_nombre_rutas)

            # Ordenar por frecuencia de mayor a menor
            df_frecuencias = df_frecuencias.sort_values(by='Frecuencia', ascending=False)

            # Graficar frecuencias de rutas metabólicas
            plt.figure(figsize=(10, 8))
            plt.barh(df_frecuencias['Nombre de la Ruta'], df_frecuencias['Frecuencia'], color='#E0218A')
            plt.xlabel('Frecuencia', fontsize=12)
            plt.ylabel('Ruta metabólica', fontsize=12)
            plt.title('Frecuencia de Rutas Metabólicas', fontsize=14)
            plt.gca().invert_yaxis()
            plt.xticks(rotation=90)
            plt.tight_layout()
            plt.show()

        except Exception as e:
            print(f"Error en el análisis de rutas metabólicas: {e}")

    except Exception as main_error:
        print(f"Error general: {main_error}")
