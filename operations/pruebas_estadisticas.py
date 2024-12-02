'''
MODULO DE PRUEBAS ESTADISTICAS 

Este módulo contiene funciones para realizar análisis estadísticos comunes en experimentos científicos, incluyendo pruebas de normalidad, 
pruebas de comparación de grupos y análisis post hoc. Es ideal para estudios que implican datos experimentales divididos en grupos independientes.


Funciones:
        1. prueba_shapiro
                Descripción:
                Realiza la prueba de Shapiro-Wilk para evaluar la normalidad de los datos en cada columna de un DataFrame.

                Parámetros:
                df (pd.DataFrame):
                Un DataFrame donde cada columna representa un conjunto de datos que será evaluado para determinar si sigue una distribución normal.
                
                Retorna:
                pd.DataFrame:
                Un DataFrame con las siguientes columnas:
                    Columna: Nombre de la columna analizada.
                    W-Estadistica: Estadístico W de la prueba de Shapiro-Wilk.
                    P-Value: Valor p asociado al estadístico W.
                    Normalidad: Indicador textual ("Normal" o "No Normal") según el valor p (> 0.05 se considera normal).
        
        2. prueba_kruskal
                Descripción:
                Realiza la prueba de Kruskal-Wallis para comparar medianas entre varios grupos independientes. Es una alternativa no paramétrica a ANOVA,
                útil cuando los datos no cumplen con los supuestos de normalidad.

                Parámetros:
                *grupos (list, array):
                Uno o más grupos de datos independientes, proporcionados como listas o arrays.
                
                Retorna:
                pd.DataFrame:
                Un DataFrame con los siguientes resultados:
                    H-Statistic: Estadístico H de Kruskal-Wallis.
                    P-Value: Valor p asociado al estadístico H.
                    Interpretación: Texto que indica si las diferencias son significativas ("Significativa" si p < 0.05, "No significativa" de lo 
                    contrario).

        3. prueba_posthoc_dunn
                Descripción:
                Realiza la prueba post hoc de Dunn para identificar qué grupos específicos difieren significativamente después de una prueba de 
                Kruskal-Wallis. Ajusta los valores p utilizando la corrección de Bonferroni.

                Parámetros:
                grupos (list):
                Lista de listas, donde cada sublista contiene los datos de un grupo.
                nombres_grupos (list):
                Lista con los nombres de los grupos correspondientes a los datos en grupos.
                
                Retorna:
                pd.DataFrame:
                Un DataFrame con las siguientes columnas:
                    Grupo 1: Nombre del primer grupo en la comparación.
                    Grupo 2: Nombre del segundo grupo en la comparación.
                    P-Value: Valor p ajustado para la comparación.
                    Interpretación: Texto que indica si las diferencias son significativas ("Significativa" si p < 0.05, "No significativa" de lo 
                    contrario).

REQUISITOS:
Este módulo requiere las siguientes bibliotecas instaladas:
    - pandas: Para manipulación de datos.
    - scipy: Para realizar pruebas estadísticas como Shapiro-Wilk y Kruskal-Wallis.
    - scikit_posthocs: Para realizar pruebas post hoc como la de Dunn.
'''


import pandas as pd
import scipy.stats as stats
import scikit_posthocs as sp

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