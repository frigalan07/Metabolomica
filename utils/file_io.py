'''
MÓDULO DE CONSULTAS Y PROCESAMIENTO DE DATOS KEGG
Este módulo contiene funciones útiles para interactuar con la base de datos KEGG, que es ampliamente utilizada en investigaciones genómicas, bioquímicas y biomédicas. Permite obtener información sobre metabolitos y rutas metabólicas relacionadas, procesando datos de forma eficiente para integrar conocimiento metabólico.

Funciones Incluidas:
1. limpiar_ids_kegg
Descripción: Preprocesa una lista de IDs de KEGG para asegurar que estén en el formato correcto al realizar consultas en la API KEGG.
Parámetros:
ids (list): Lista de IDs KEGG (como C00031 para compuestos o hsa00010 para rutas).
Retorna:
Una lista de IDs formateados (espacios eliminados y codificados para URLs).
2. obtener_nombre_metabolito
Descripción: Recupera el nombre de un metabolito dado su ID en la base de datos KEGG.
Parámetros:
compound_id (str): ID del compuesto (ejemplo: C00031).
Retorna:
El nombre del compuesto como cadena de texto, o "Nombre desconocido" si no se encuentra o hay un error.
3. obtener_rutas
Descripción: Consulta las rutas metabólicas asociadas a un metabolito específico.
Parámetros:
compound_id (str): ID del compuesto (ejemplo: C00031).
Retorna:
Lista única de IDs de rutas metabólicas asociadas al compuesto.
4. obtener_nombre_rutas
Descripción: Obtiene el nombre de una ruta metabólica dada su ID en KEGG.
Parámetros:
pathway_id (str): ID de la ruta (ejemplo: hsa00010).
Retorna:
El nombre de la ruta como cadena de texto, o "Nombre desconocido" si no se encuentra o hay un error.
Requisitos:
Este módulo requiere las siguientes bibliotecas:

requests: Para realizar solicitudes HTTP a la API de KEGG.

'''

import requests

def limpiar_ids_kegg(ids):
    """
    Limpia y prepara una lista de identificadores KEGG para ser utilizados en consultas.

    Args:
    - ids (list): Lista de cadenas con identificadores KEGG.

    Returns:
    - list: Lista con identificadores formateados para consultas KEGG (espacios reemplazados por '%20').
    """
    return [id.strip().replace(" ", "%20") for id in ids]


def obtener_nombre_metabolito(compound_id):
    """
    Recupera el nombre de un metabolito a partir de su identificador KEGG.

    Args:
    - compound_id (str): Identificador KEGG del compuesto (por ejemplo, "C00031").

    Returns:
    - str: Nombre del metabolito si está disponible; de lo contrario, "Nombre desconocido".
    """
    url = f"http://rest.kegg.jp/get/{compound_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text
        # El nombre del compuesto aparece en la línea que comienza con "NAME"
        for line in data.split("\n"):
            if line.startswith("NAME"):
                return line.split("NAME")[1].strip()
    return "Nombre desconocido"


def obtener_rutas(compound_id):
    """
    Consulta las rutas metabólicas asociadas con un metabolito específico en KEGG.

    Args:
    - compound_id (str): Identificador KEGG del compuesto.

    Returns:
    - list: Lista con los identificadores de las rutas metabólicas asociadas; devuelve una lista vacía si no se encuentran rutas.
    """
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


def obtener_nombre_rutas(pathway_id):
    """
    Obtiene el nombre de una ruta metabólica a partir de su identificador KEGG.

    Args:
    - pathway_id (str): Identificador de la ruta metabólica (por ejemplo, "path:map00010").

    Returns:
    - str: Nombre de la ruta metabólica si está disponible; de lo contrario, "Nombre desconocido".
    """
    url = f"http://rest.kegg.jp/get/{pathway_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text
        # El nombre de la ruta aparece en la línea que comienza con "NAME"
        for line in data.split("\n"):
            if line.startswith("NAME"):
                return line.split("NAME")[1].strip()
        # Alternativamente, el nombre podría estar en la primera línea
        return data.split("\n")[1].strip()
    return "Nombre desconocido"
