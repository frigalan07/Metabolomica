import requests


def limpiar_ids_kegg(ids):
    return [id.strip().replace(" ", "%20") for id in ids]


# Función para obtener el nombre de un metabolito
def obtener_nombre_metabolito(compound_id):
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
def obtener_rutas(compound_id):
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
def obtener_nombre_rutas(pathway_id):
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