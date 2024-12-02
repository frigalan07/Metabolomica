# Metabolómica

Frida Galán Hernández: <fridagalangh@lcg.unam.mx> 
Carlos García González: <carlosgg@lcg.unam.mx>

Fecha:  29/09/2024


## Introducción

Las estructuras centrales de los metabolitos celulares, que van desde los componentes de la glucólisis y el ciclo del ácido cítrico hasta 
los intermediarios en la biosíntesis de nucleótidos, son idénticas en todos los organismos conocidos. La organización de estos metabolitos en 
vías de reacciones covalentes también es impresionantemente similar entre las especies. La secuenciación de los genomas completos de organismos 
que van desde *E. coli* hasta humanos ha llevado a la asignación a cada reacción metabólica de las secuencias de enzimas responsables de su 
catálisis. Esta información ha abierto la puerta a la metabolómica celular: el estudio cuantitativo de la red completa del metabolismo celular, 
en este sentido, la metabolómica se refiere a la medición del contenido total de moléculas pequeñas de los sistemas biológicos y el intento de 
relacionar el resultado sobre los fenómenos biológicos subyacentes. Su nacimiento y crecimiento como campo de estudio ha sido catalizado por 
los éxitos de la genómica, así como por avances en espectrometría de masas (MS) que facilitan la medición altamente paralela de moléculas 
pequeñas.(1)

Ahora bien, ¿y por qué elegir *E. coli* para su estudio?

*Escherichia coli* es una bacteria Gram negativa típica de la familia Enterobacteriaceae. El análisis de 16S rRNA muestra que pertenece a 
la subclase de proteobacterias γ, misma que se encuentra muy relacionada a las otras proteobacterias (α, a las cianobacterias). 
La subclase de proteobacterias γ incluye además a organismos patógenos de humanos, como son Shigella, Salmonella, Vibrio y Haemophilus. 
Las bacterias de la familia Enterobacteriaceae se caracterizan por ser capaces de respirar facultativamente: anaeróbicamente en el interior 
del intestino y aeróbicamente en el ambiente exterior. Gracias a esta capacidad muchos de los miembros de esta familia son de vida libre, 
mientras que otros tantos son principalmente comensales de animales invertebrados y vertebrados o son patógenos de plantas (2).

Las bacterias entéricas son varillas Gram-negativas no fotosintéticas capaces de generar ATP tanto aeróbicamente como anaeróbicamente. 
Por lo general, son competentes para vivir en medios mínimos simples que contienen solo sal, azúcar, amoníaco, fosfato y sulfato. 
Sus vías de metabolismo central y biosíntesis son notablemente similares a las de la levadura (3) y también, en cierta medida, de los 
mamíferos, a pesar de la compartimentación intracelular radicalmente diferente.(2)

*E. coli* es una de las bacterias más conocidas en la comunidad científica y la más estudiada debido a que es un buen organismo modelo, 
debido a que es fácilmente cultivable, es de crecimiento rápido y te permite obtener densidades poblacionales grandes, por tanto el estudio 
de su metabolómica, nos da una excelente ventana para el estudio de su metabolismo y su interacción con diversos medios. Dicho conocimiento 
es de importancia porque se puede extrapolar para estudios posteriores, ya que esta bacteria es ampliamente utilizada en la industria de la 
biotecnología, sobre todo en la producción de proteínas recombinantes. Su capacidad de poder modificarla genéticamente la convierte en un 
sistema ideal para estudios de expresión génica y producción de metabolitos de interés. A través de la ingeniería metabólica, se exploran 
nuevas vías para mejorar la producción de compuestos bioquímicos útiles y desarrollar nuevas estrategias de tratamiento contra las infecciones 
causadas por cepas patógenas.
Las vías metabólicas de un amplio espectro de organismos están bien capturadas en varias bases de datos accesibles a la web, por ejemplo, 
la Enciclopedia de Genes y Genomas de Kioto (KEGG)(1), la cual es una de las que utilizaremos en este proyecto.


"Lo que es cierto de *Escherichia coli* también debe ser cierto de los elefantes", opinó el premio Nobel Jacques Monod en 1954(4).


## Planteamiento del problema

El proyecto busca identificar y cuantificar las variaciones en los perfiles metabolómicos de E. coli bajo distintas condiciones 
experimentales. Utilizando espectrometría de masas, se ha medido la intensidad relativa de diversos metabolitos intracelulares. Se 
plantea la necesidad de establecer si estas variaciones son significativas, así como asociar los cambios observados con rutas 
metabólicas reconocidas, mientras se controlan las diferencias entre réplicas técnicas y biológicas para asegurar una robustez de los resultados. 


## Metodología

Nuestros datos de entrada son datos metabolómicos, los cuales fueron elaborados por la Dra. Daniela Ledezma del Centro de Ciencias Genómicas.

Estos datos al principio se encotraban en forma de un archivo EXCEL (.xlsx), pero los modificamos
para que sean ".csv", que nos serviran de mejor manera.

Los datos son intensidades de metabolitos intracelulares de **E. coli** crecida en medio mínimo (M9) con distintas adiciones al medio.

Las descripciones de las primeras 5 columnas son las siguientes:

* ionIdx. Indices del metabolito	
* ionMz. Coeficiente masa/Carga del metabolito. Es lo que arroja de forma cruda el espectrómetro de masas.
* Top annotation name. Nombre del metabolito
* Formula. Fórmula química.
* KEGG ids. Id del metabolito en la base de datos KEGG (https://www.genome.jp/kegg/)

Las demás columnas son las mediciones de los metabolitos, cada columna tiene un nombre específico, que en general se representan como:

* Indice consecutivo por condición 
* punto 
* id de la condición 
* guión bajo 
* número de la réplica biológica 
* id de la réplica técnica

```
2.h20_s1
```

Con estos datos planeamos resolver distintas preguntas biológicas, siguiendo un flujo claro
y específico, la logica que usaremos es la siguiente:

1. Definir los datos a trabajar, en este caso son los datos descritos previamente.

2. Revisar los datos detalladamente y entender su nomenclatura y anotación.

3. Filtrar los datos eliminando las columnas que tengan "sc", ya que son datos extra que meteran ruido.

4. Analizar la variación de las columnas de H2O, para ver que tano se ensucio el espectrómetro, con la finalidad de saber si las lecturas se contaminaron.


5. Definir cual va a ser nuestro punto de corte, es decir, cuál sería una medida "normal" en la intensidad de los metabolitos, lo cual se hará con el promedio de las lecturas de "H2O", esto es 
de suma importancia, ya que de esta medida va a depender lo siguiente que hagamos.

6. Obtener las columnas donde haya una gran concentración de matbolito y en las que haya menos, generando con estos dos subset de datos, uno para definir datos con una media significativamente menor a la media de H2O y el otro, para definir datos con una media significativamente mayor al control.

7. Una vez que tengamos estos subsets, conseguiriamos  sus ID's de la base de datos de KEEG y guardarlos en un archivo.

8. Ya que tengamos ese archivo, buscar las vías metabólicas en las que estan envueltos esos metabolitos, esta busqueda la haremos en la base de datos de KEEG.

9. Una vez que sepamos sus rutas metabólicas, vamos a interpretar los resultados y explicarlos para poder contestar nuestra pregunta biológica.


### A. Servidor y software

**Servidor**:
    Servidor local con capacidad para ejecutar scripts en Python y manejar análisis de datos.

**Usuario**:
    Frida Galán Hernández y Carlos García González

**Software**:
        - **Python 3.7 o superior**: Para el análisis y manejo de datos metabolómicos.
        - **Librerías necesarias**: pandas, matplotlib, requests, scipy, sciki_posthocs y módulos personalizados para pruebas estadísticas y
        manejo de datos KEGG.
        - **Microsoft Excel o similar**: Para trabajar con los archivos .xlsx utilizados como entrada. 

### B. Datos de Entrada 

Los datos de entrada fueron proporcionados por la Dra. Daniela Ledezma Tejada a la Dra. Heladia Salgado Osorio. 
Estos representan mediciones de intensidades relativas de metabolitos en Escherichia coli bajo diferentes condiciones experimentales.
Se descargaron los datos desde el *Moodle para el curso de Biopython* y estan localizados en la carpeta:
"docs"



#### Metadatos de la carpeta de datos

Fecha de descarga: 09/18/2024

>| Archivo | Descripción  | Tipo |
|:--      |:--           |:--  |
| datos_metabolomica.xlsx  | Intensidades relativas de metabolitos bajo distintas condiciones.  | Formato Excel |

#### Formato de los archivos

**Descripción de columnas principales del archivo datos_metabolomica.xlsx**:
    El archivo de Excel incluye:

        - **Columna ionMz**: Identificación basada en la relación masa/carga (m/z) del metabolito.
        - **Columna formula**: Fórmula molecular del metabolito identificado.
        - **Columna KEGG ids**: Identificadores únicos del metabolito en la base de datos KEGG.
        - **Columnas de datos experimentales (e.g., h2o_s1, ace_2_sb)**: Intensidades relativas de metabolitos bajo diferentes condiciones 
        experimentales.

### Preguntas de investigación

1. **¿Cómo cambia la intensidad de cada metabolito en respuesta a los diferentes medios?**
Comparar promedios de intensidades y realizar pruebas estadísticas entre condiciones experimentales (H2O, asp, glu).

2. **¿Qué vías metabólicas se ven afectadas por dicho cambio en el medio?**
Asociar los metabolitos identificados con rutas metabólicas conocidas utilizando KEGG.

3. **¿Qué mecanismos podrían estar regulando dichas vías metabólicas?**
Realizar una revisión funcional de las rutas afectadas, integrando datos biológicos y metabólicos.


## Resultados
 
Los resultados del análisis se presentarán organizados en las siguientes secciones:

    - **Pruebas de Normalidad y Estadísticas**:
        Incluye resultados de Shapiro-Wilk, Kruskal-Wallis y Dunn para determinar significancia entre las condiciones experimentales.

    - **Análisis de Vías Metabólicas**:
        Identificación de rutas metabólicas relevantes y su frecuencia de aparición.

    - **Visualización**:
        Gráficos que representa la frecuencias de las rutas.



## Análisis y Conclusiones

**Análisis**:
    - Los cambios en la intensidad de los metabolitos sugieren una respuesta adaptativa significativa de E. coli a diferentes medios experimentales.
    - La combinación de pruebas estadísticas robustas y asociaciones con KEGG valida la reproducibilidad de los resultados.

**Conclusiones**:
    - Las condiciones del medio pueden influir significativamente en las rutas metabólicas centrales de E. coli.
    - Los mecanismos reguladores probablemente involucran respuestas transcripcionales y ajustes enzimáticos rápidos.
    - Este análisis proporciona un marco útil para explorar más a fondo cómo factores externos afectan el metabolismo microbiano.


## Referencias

 [1]Rabinowitz, J. D. (2007). Cellular metabolomics of Escherchia coli. Expert Review of Proteomics, 4(2), 187–198. https://    doi.org/10.1586/14789450.4.2.187 
 [2] Logan, N. A. 1994. Bacterial systematics. Blackwell scientific publications, Oxford, 263pp.
 [3]Forster J, Famili I, Fu P, Palsson BO,
Nielsen J. Genome-scale reconstruction of the Saccharomyces cerevisiae metabolic network. Genome Res. 13(2), 244–253 (2003).
 [4] Friedmann HC. From “butyribacterium” to “E. coli”: an essay on unity in biochemistry. Perspect. Biol. Med. 47(1), 47–66 (2004).
 

 
 -->
