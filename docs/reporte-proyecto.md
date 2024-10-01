# Metabolómica

Frida Galán Hernández: <fridagalangh@lcg.unam.mx> 
Carlos García González: <carlosgg@lcg.unam.mx>

Fecha:  29/09/2024


## Introducción

Las estructuras centrales de los metabolitos celulares, que van desde los componentes de la glucólisis y el ciclo del ácido cítrico hasta los intermediarios en la biosíntesis de nucleótidos, son idénticas en todos los organismos conocidos. La organización de estos metabolitos en vías de reacciones covalentes también es impresionantemente similar entre las especies. La secuenciación de los genomas completos de organismos que van desde *E. coli* hasta humanos ha llevado a la asignación a cada reacción metabólica de las secuencias de enzimas responsables de su catálisis. Esta información ha abierto la puerta a la metabolómica celular: el estudio cuantitativo de la red completa del metabolismo celular, en este sentido, la metabolómica se refiere a la medición del contenido total de moléculas pequeñas de los sistemas biológicos y el intento de relacionar el resultado sobre los fenómenos biológicos subyacentes. Su nacimiento y crecimiento como campo de estudio ha sido catalizado por los éxitos de la genómica, así como por avances en espectrometría de masas (MS) que facilitan la medición altamente paralela de moléculas pequeñas.(1)

Ahora bien, ¿y por qué elegir *E. coli* para su estudio?

*Escherichia coli* es una bacteria Gram negativa típica de la familia Enterobacteriaceae. El análisis de 16S rRNA muestra que pertenece a la subclase de proteobacterias γ, misma que se encuentra muy relacionada a las otras proteobacterias (α, a las cianobacterias). La subclase de proteobacterias γ incluye además a organismos patógenos de humanos, como son Shigella, Salmonella, Vibrio y Haemophilus. Las bacterias de la familia Enterobacteriaceae se caracterizan por ser capaces de respirar facultativamente: anaeróbicamente en el interior del intestino y aeróbicamente en el ambiente exterior. Gracias a esta capacidad muchos de los miembros de esta familia son de vida libre, mientras que otros tantos son principalmente comensales de animales invertebrados y vertebrados o son patógenos de plantas (2).

Las bacterias entéricas son varillas Gram-negativas no fotosintéticas capaces de generar ATP tanto aeróbicamente como anaeróbicamente. Por lo general, son competentes para vivir en medios mínimos simples que contienen solo sal, azúcar, amoníaco, fosfato y sulfato. Sus vías de metabolismo central y biosíntesis son notablemente similares a las de la levadura (3) y también, en cierta medida, de los mamíferos, a pesar de la compartimentación intracelular radicalmente diferente.(2)

*E. coli* es una de las bacterias más conocidas en la comunidad científica y la más estudiada debido a que es un buen organismo modelo, debido a que es fácilmente cultivable, es de crecimiento rápido y te permite obtener densidades poblacionales grandes, por tanto el estudio de su metabolómica, nos da una excelente ventana para el estudio de su metabolismo y su interacción con diversos medios. Dicho conocimiento es de importancia porque se puede extrapolar para estudios posteriores, ya que esta bacteria es ampliamente utilizada en la industria de la biotecnología, sobre todo en la producción de proteínas recombinantes. Su capacidad de poder modificarla genéticamente la convierte en un sistema ideal para estudios de expresión génica y producción de metabolitos de interés. A través de la ingeniería metabólica, se exploran nuevas vías para mejorar la producción de compuestos bioquímicos útiles y desarrollar nuevas estrategias de tratamiento contra las infecciones causadas por cepas patógenas.
Las vías metabólicas de un amplio espectro de organismos están bien capturadas en varias bases de datos accesibles a la web, por ejemplo, la Enciclopedia de Genes y Genomas de Kioto (KEGG)(1), la cual es una de las que utilizaremos en este proyecto.


"Lo que es cierto de *Escherichia coli* también debe ser cierto de los elefantes", opinó el premio Nobel Jacques Monod en 1954(4).


## Planteamiento del problema

El proyecto busca identificar y cuantificar las variaciones en los perfiles metabolómicos de E. coli bajo distintas condiciones 
experimentales. Utilizando espectrometría de masas, se ha medido la intensidad relativa de diversos metabolitos intracelulares. Se 
plantea la necesidad de establecer si estas variaciones son significativas, así como asociar los cambios observados con rutas 
metabólicas reconocidas, mientras se controlan las diferencias entre réplicas técnicas y biológicas para asegurar una robustez de los resultados. 


## Metodología

Nuestros datos de entrada son datos de metabolomicos, los cuales fueron elaborados por la Dra. Daniela Ledezma del Centro de Ciencias
Genómicas.
Dichos datos se encuentran en un archivo EXCEL (.xlsx).

Los datos son intensidades de metabolitos intracelulares de **E. coli** crecida en medio mínimo (M9) con distintas adiciones al medio.

Las descripciones de las primeras 5 columnas son las siguientes:

- ionIdx. Indices del metabolito	
- ionMz. Coeficiente masa/Carga del metabolito. Es lo que arroja de forma cruda el espectrómetro de masas.
- Top annotation name. Nombre del metabolito
- Formula. Fórmula química.
- KEGG ids. Id del metabolito en la base de datos KEGG (https://www.genome.jp/kegg/)

Las demás columnas son las mediciones de los metabolitos, cada columna tiene un nombre específico, que en general se representan como:

- Indice consecutivo por condición 
- punto 
- id de la condición 
- guión bajo 
- número de la réplica biológica 
- id de la réplica técnica

```
2.h20_s1
```



### A. Servidor y software

> Servidor: 

> Usuario: 

> Software: 

### B. Datos de Entrada 

Entendiendo los archivos de datos 

Los datos de entrada fueron descargados desde NCBI y se encuentran en RUTA DE LA CARPETA.

```
|-- data
|   |-- coli_genomic.fna
|   |-- coli.gff
|   |-- coli_protein.fna
|   |-- directorio.txt
|   `-- flagella_genes.txt
```
-->

#### Metadatos de la carpeta de datos

<!-- 
> Versión/Identificador del genoma:  NC_000913.3

> Fecha de descarga: dd/mm/aaaa

>| Archivo | Descripción  | Tipo |
|:--      |:--           |:--  |
| coli_genomic.fna  | Secuencia de nucleotidos de E. coli  | Formato FastA |
| coli.gff.   | Anotación del genoma de E. coli  | Formato gff |
| coli_protein.faa | Secuencia de aminoacidos de las proteinas de E. coli | formato FastA|
| flagella_genes.txt | Genes con función relacionada al flagello en E. coli | lista |
| directorio.txt. | Archivo con nombres de personas | lista |

-->

#### Formato de los archivos

<!-- 

- `coli_genomic.fna` : formato FastA


```
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGCTTCTGAACTG
GTTACCTGCCGTGAGTAAATTAAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGAC
AGATAAAAATTACAGAGTACACAACATCCATGAAACGCATTAGCACCACCATTACCACCACCATCACCATTACCACAGGT
```

Formato: 

> a. La primera línea es información de la secuencia. Primero viene el identificador del genoma.

> b. Después vienen varias líneas con la secuencia de nuclótidos del genoma completo.



- `coli.gff`: anotación de features en el genoma


El contenido del archivo es:

```
##gff-version 3
#!gff-spec-version 1.21
#!processor NCBI annotwriter
#!genome-build ASM584v2
#!genome-build-accession NCBI_Assembly:GCF_000005845.2
##sequence-region NC_000913.3 1 4641652
##species https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=511145

NC_000913.3     RefSeq  region  1       4641652 .       +       .       ID=NC_000913.3:1.>
NC_000913.3     RefSeq  gene    190     255     .       +       .       ID=gene-b0001;Dbx>
NC_000913.3     RefSeq  CDS     190     255     .       +       0       ID=cds-NP_414542.>
NC_000913.3     RefSeq  gene    337     2799    .       +       .       ID=gene-b0002;Dbx>
NC_000913.3     RefSeq  CDS     337     2799    .       +       0       ID=cds-NP_414543.>

```

Formato: 

> a. Es un formato gff tabular, es decir, cada dato es separado por tabulador.
> 
> b. Cada renglón en el formato gff es una elemento genético anotado en el genoma, que se le denomina `feature`, éstos features pueden ser genes, secuencias de inserción, promotores, sitios de regulación, todo aquello que este codificado en el DNA y ocupe una región en el genoma de  E. coli.

> c. Los atributos de cada columna par cada elemento genético son

>```
1. seqname. Nombre del cromosoma
2. source. Nombre del programa que generó ese elemento
3. feature. Tipo de elemento
4. start. Posición de inicio
5. end. Posición de final
6. score. Un valor de punto flotante
7. strand. La cadena (+ , - )
8. frame. Marco de lectura
9.  attribute. Pares tag-value, separados por coma, que proveen información adicional
```


#### Preguntas de investigación

1)¿Cómo cambia la intensidad de cada metabolito en respuesta a los  diferentes medios?
2)¿Qué vías metabólicas se ven afectadas por dicho cambio en el medio?
3)Proponer mediante que mecanismos se ven afectadas dichas vías metabólicas 



-->


## Resultados
 

<!-- ### X. Pregunta 

Archivo(s):     

Algoritmo: 

1. 

Solución: Describir paso a paso la solución, incluyendo los comandos correspondientes

```bash

```

-->




## Análisis y Conclusiones

 <!-- Describir todo lo que descubriste en este análisis -->


## Referencias
<!-- Registrar todas las referencias consultadas. Se sugiere formato APA. Ejemplo:

 [1]Rabinowitz, J. D. (2007). Cellular metabolomics of Escherchia coli. Expert Review of Proteomics, 4(2), 187–198. https://    doi.org/10.1586/14789450.4.2.187 
 [2] Logan, N. A. 1994. Bacterial systematics. Blackwell scientific publications, Oxford, 263pp.
 [3]Forster J, Famili I, Fu P, Palsson BO,
Nielsen J. Genome-scale reconstruction of the Saccharomyces cerevisiae metabolic network. Genome Res. 13(2), 244–253 (2003).
 [4] Friedmann HC. From “butyribacterium” to “E. coli”: an essay on unity in biochemistry. Perspect. Biol. Med. 47(1), 47–66 (2004).
 

 
 -->