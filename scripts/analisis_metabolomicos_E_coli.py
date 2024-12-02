'''
Nombre:
    Análisis metabolómicos de E. Coli

Version:
    3.12.2

Autor:
    Galán Hernández Frida
    García González Carlos

Descripcion:
    Este programa hecho en Python tienen la funcionalidad de calcular la frecuencia de nucleótidos, 
    la frecuencia de codones, además de que transcribe una secuencia de DNA a RNA y la traduce a una cadena de aminoácidos
Argumentos:
    - nombre archivo (path)
    - n (T,A,G,C) para establecer el nucleótido de interesa 
    - m (0,1,2) para establecer el marco de lectura, solo forward 
Usage:
    python scripts/analisis_DNA.py PATH DE LA ARCHIVO CON LA SECUENCIA -n NUCLEÓTIDO -m MARCO DE LECTURA
    python3 scripts/analisis_DNA.py /Users/frida_galan/Desktop/PythonSEM2/Notas_Biopython/seq.nt.fa -n T -m 0 
'''
# Importaciones estándar de Python
import argparse

from collections import Counter

# Librerías de terceros (instaladas vía pip)
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Importaciones específicas de Biopython
from Bio.KEGG import REST

import sys
import os

# Agregar dinámicamente la raíz del proyecto a sys.path usando rutas relativas
script_dir = os.path.dirname(__file__)  # Carpeta donde está el script actual
project_root = os.path.abspath(os.path.join(script_dir, ".."))  # Subir un nivel a la raíz
sys.path.append(project_root)  # Agregar la raíz del proyecto a sys.path


from operations.pruebas_estadisticas import prueba_shapiro
from operations.pruebas_estadisticas import prueba_kruskal
from operations.pruebas_estadisticas import prueba_posthoc_dunn


# Se parsean los argumentos usando la libreria de argparse
parser = argparse.ArgumentParser(
    description="El siguiente script analiza datos de metabolitos de E. coli"
)

parser.add_argument("-c1", "--CONDICION1",
                    help="Primera condición para expresión diferencial, por defecto 'asp'",
                    type=str,
                    default="asp",
                    required=False)

parser.add_argument("-c2", "--CONDICION2",
                    help="Segunda condición para expresión diferencial, por defecto 'glu'",
                    type=str,
                    default="glu",
                    required=False)

args = parser.parse_args()



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
    ruta_archivo = "..\..\..\..\..\Downloads\datos_metabolomica.xlsx"
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
