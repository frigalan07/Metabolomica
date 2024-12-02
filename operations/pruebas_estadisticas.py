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