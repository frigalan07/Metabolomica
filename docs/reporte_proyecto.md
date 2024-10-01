# Metabolómica

Frida Galán Hernández: <fridagalangh@lcg.unam.mx> 
Carlos García González: <carlosgg@lcg.unam.mx>

Fecha:  29/09/2024


## Introducción

*Escherichia coli* es un bacteria Gram negativa típica de la familia Enterobacteriaceae. El análisis de 16rRNA muestra que 
pertenece a la subclase de proteobacterias γ, misma que se encuentra muy relacionada a las otras proteobacteria (α, a las 
cianobacterias. La subclase de proteobacterias g, incluye además a organismos patógenos de humanos, como son Shigella, Samonella, Vibrio y Haemophilus. Las bacterias de la familia Enterobacteriaceae se caracterizan por ser capaces de 
respirar facultativamente: anaérobicamente en el interior del intestino y aerobicamente en el ambiente exterior. Gracias a esta 
capacidad muchos de los miembros de esta familia son de vida libre, mientras que otros tantos son principalmente comensales de  animales invertebrados y vertebrados o son patógenos de plantas (1). *Escherichia coli* es la flora facultativa no patógena predominante del intestino humano. Sin embargo, algunas cepas de E. coli han desarrollado la capacidad de causar enfermedades del sistema gastrointestinal, urinario o nervioso central incluso en los huéspedes humanos más robustos. (2) Estas cepas patógenas como lo son *E. coli* enterotoxigénica (ETEC) y *E. coli* enterohemorrágica (EHEC) , son un gran desafío para la salud pública mundial. 
*E.coli* es una de las bacterias más conocidas en la comunidad científica y la más estudiada debido a que es un buen organismo modelo, debido a que es fácilmente cultivable, es de crecimiento rápido y te permite obtener densidades poblacionales grandes, por tanto el estudio de su metabolómica, que se define como -una disciplina compleja que se centra en el estudio de metabolitos presentes en células, tejidos u organismos en un tiempo determinado o bajo un estímulo-(3) nos da una excelente ventana para el estudio de su metabolismo y su interacción con diversos medios. Dicho conocimiento es de importancia porque se puede extrapolar para estudios posteriores, ya que esta bacteria es ampliamente utilizada en la industria de la biotecnología, sobretodo en la producción de proteínas recombinantes. Su capacidad de poder modificarla genéticamente la convierte en un sistema ideal para estudios de expresión génica y producción de metabolitos de interés. A través de la ingeniería metabólica, se exploran nuevas vías para mejorar la producción de compuestos bioquímicos útiles y desarrollar nuevas estrategias de tratamiento contra las infecciones causadas por cepas patógenas.


## Planteamiento del problema

El proyecto busca identificar y cuantificar las variaciones en los perfiles metabolómicos de E. coli bajo distintas condiciones 
experimentales. Utilizando espectrometría de masas, se ha medido la intensidad relativa de diversos metabolitos intracelulares. Se 
plantea la necesidad de establecer si estas variaciones son significativas, así como asociar los cambios observados con rutas 
metabólicas reconocidas, mientras se controlan las diferencias entre réplicas técnicas y biológicas para asegurar una robustez de los resultados. 


## Metodología

Nuestros datos de entrada son datos de metabolómicos, los cuales fueron elaborados por la Dra. Daniela Ledezma del Centro de Ciencias Genómicas.

Estos datos al principio se encotraban en forma de un archivo EXCEL (.xlsx), pero los modificamos
para que sean ".csv", que nos serviran de mejor manera.

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

Con estos datos planeamos resolver distintas preguntas biológicas, siguiendo un flujo claro
y específico, la logica que usaremos es la siguiente:

1. Definir los datos a trabajar, en este caso son los datos descritos previamente.

2. Revisar los datos detalladamente y entender su nomenclatura y anotación.

3. Definir un subset de datos con los cuales trabajan, ya que son demasiados datos.

4. Definir cual va a ser nuestro punto de corte, es decir, cuál sería una medida "normal" en la intensidad de los metabolitos, esto es de suma importancia, ya que de esta medida va a depender lo siguiente que hagamos.

5. Obtener las columnas donde haya una gran concentración de matbolito y en las que haya menos, generando con estos un segundo subset de datos, para determinar que es una concentración mayor o menor, ocuparemos el dato anterior.

6. Una vez que tengamos ese subset, conseguir sus ID de la base de datos de KEEG y guardarlos en un archivo.

7. Ya que tengamos ese archivo, buscar las vías metabólicas en las que estan envueltos esos metabolitos, esta busqueda la haremos en la base de datos de KEEG.

8. Una vez que sepamos sus rutas metabólicas, vamos a interpretar los resultados y explicarlos para poder contestar nuestra pregunta biológica.


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
> ¿Pregunta X?
Respuesta: Describir el trabajo que implica o pasos a seguir para resolver esta pregunta.



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
 
 [1] Logan, N. A. 1994. Bacterial systematics. Blackwell scientific publications, Oxford, 263pp.
 [2] Nataro JP, Kaper JB.1998.Diarrheagenic Escherichia coli. Clin Microbiol Rev 11:.https://doi.org/10.1128/cmr.11.1.142
 [3] Diccionario del Instituto Nacional del Cáncer. Instituto Nacionales de la Salud, Gobierno de Estados Unidos, https://www.cancer.gov/espanol/publicaciones/diccionarios/diccionario-cancer/def/metabolomica.

 
 -->
