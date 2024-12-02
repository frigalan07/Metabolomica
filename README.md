# Metabolomica
Repositorio creado para trabajar datos metabolómicos de *E.coli* como proyecto del curso de BioPython de la Licenciatura en Ciencias Genómicas. 

El proyecto busca identificar y cuantificar las variaciones en los perfiles metabolómicos de *E. coli* bajo distintas condiciones experimentales. Utilizando espectrometría de masas, se ha medido la intensidad relativa de diversos metabolitos intracelulares. Se plantea la necesidad de establecer si estas variaciones son significativas, así como asociar los cambios observados con rutas metabólicas reconocidas, mientras se controlan las diferencias entre réplicas técnicas y biológicas para asegurar una robustez de los resultados.

# Autores 

Frida Galan Hernandez, estudiante de tercer semestre de la Licenciatura en Ciencias Genómicas.

email:<fridagalan@lcg.unam.mx>

Carlos Garcia Gonzalez, estudiante de tercer semestre de la Licenciatura en Ciencias Genómicas.

email:<carlosgg@lcg.unam.mx>

# Uso

Este script se utiliza para analizar datos metabolómicos obtenidos de E. coli bajo diferentes condiciones experimentales. Puede identificar variaciones significativas en la concentración de metabolitos y asociarlas con rutas metabólicas reconocidas.

El script permite especificar las condiciones experimentales a comparar mediante argumentos en la línea de comandos.

Requisitos:

Python 3.11.9 o superior.
Instalación de las dependencias:

``` bash
pip install pandas matplotlib scipy scikit_posthocs requests
```

Ejecución:
``` bash
python script_metabolomica.py -c1 <CONDICION1> -c2 <CONDICION2>
```

<CONDICION1>: Condición experimental para el grupo 1 (por defecto, "asp").

<CONDICION2>: Condición experimental para el grupo 2 (por defecto, "glu").


# Salida

1. **Pruebas de Normalidad**: 
        Resultados de la prueba Shapiro-Wilk para evaluar la distribución de los datos.

2. **Pruebas Estadísticas**:
        Kruskal-Wallis para detectar diferencias significativas.
        Prueba post-hoc de Dunn para identificar los pares de condiciones con diferencias significativas.

3. **Análisis de Rutas Metabólicas**:
        Asociación de metabolitos con rutas metabólicas basadas en identificadores KEGG.
        Visualización de frecuencias de rutas metabólicas.


# Control de Errores

El script incluye manejo de errores para:

- Falta de archivos de datos.
- Fallos en pruebas estadísticas debido a datos insuficientes o mal formateados.
- Conexiones fallidas a bases de datos para recuperación de nombres o rutas metabólicas.


# Pruebas

1. Validación con datos simulados para condiciones conocidas.
2. Revisión de resultados estadísticos con software externo.
3. Análisis cruzado con datos reales y rutas metabólicas esperadas.


# Datos 

- **Formato esperado**: 
    Archivo Excel (.xlsx) con columnas representando condiciones experimentales y filas correspondientes a metabolitos.

- **Columnas clave**:
    "KEGG ids" para identificar metabolitos.
    Columnas experimentales etiquetadas con sufijos específicos para cada condición.

# Metadatos y Documentacion

El script utiliza identificadores KEGG para asociar metabolitos con rutas metabólicas conocidas. Esto se complementa con funciones personalizadas 
para limpieza y recuperación de datos

# Codigo Fuente

El código está organizado en módulos para una mayor claridad:

- **operations/pruebas_estadisticas.py**: Contiene funciones para realizar pruebas estadísticas.
- **utils/file_io.py**: Incluye utilidades para manejo de archivos y consultas de datos KEGG.
- **scripts/analisis_metabolomicos_E_coli.py**: Contiene el código principal

# Terminos de Uso

El uso de este código está permitido para fines académicos y no comerciales. Se agradece citar a los autores en cualquier 
trabajo derivado.

# Como Citar

Frida Galán Hernández y Carlos García González. 
"Análisis Metabolómico de E. coli usando BioPython". 
Proyecto de la Licenciatura en Ciencias Genómicas, UNAM, 2024.

# Cotactenos 

email:<fridagalan@lcg.unam.mx>

email:<carlosgg@lcg.unam.mx>
-