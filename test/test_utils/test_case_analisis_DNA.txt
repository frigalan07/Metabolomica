**Analisis_DNA** 

Este documento describe los casos de prueba para un script de Python el cual hace uso de diversos módulos, 
a modo que las funciones que realiza son las siguientes: 
- Cuenta la apariencia de cada de cada nucleóotidos
- Cuenta la frecuencia de los codones 
- Obtiene el trancrito de una secuencia de DNA 
- Obtiene la traducción de una secuencia de DNA 

**Caso de Prueba 1: Archivo Válido con Nucleótidos Predeterminados**

````bash
python script.py data.fasta
`````
**Contenido de `data.fasta`:**
>sequence1
ATCGATCG


Resultado Esperado:

The number of each nucleotide is:
- Adenine: 2
- Thymine: 2
- Guanine: 2
- Cytosine: 2
La frecuencia de cada codón es: {'ATG': 1, 'CGA': 1}
>sequence1_frame1
AUCGAUCG
>sequence1_frame2
UCGAUCG

**Caso de Prueba 2: Archivo Válido con Nucleótidos Específicos Especificados**
```bash
python script.py data.fasta -n A T
````

**Contenido de `data.fasta`:**
>sequence1
ATCGATCG

**Resultado esperado:**

Te amamos Jenni Rivera, por ti le echamos ganas a la Uni
The count of each nucleotide is:
Count of Adenines: 2
Count of Thymines: 2
La frecuencia de cada codón es: {'ATG': 1, 'CGA': 1}
>sequence1_frame1
AUCGAUCG
>sequence1_frame2
UCGAUCG

**Caso de Prueba 3: Archivo Válido con Nucleótidos Inválidos**

```bash
python script.py data_invalid.fasta
```

**Contenido de data_invalid.fasta:**
>sequence1
ATCGXATCG

**Resultado esperado:**
Error: La secuencia contiene caracteres no válidos.


**Caso de Prueba 4: Archivo Vacío**

```bash
python script.py empty.fasta
```

Crear un archivo vacío empty.fasta.

**Resultado Esperado:**
Error: El archivo está vacío.

**Caso de Prueba 5: Archivo No Encontrado**

```bash
python script.py non_existent_file.fasta
```
**Resultado Esperado**
Error: No se pudo encontrar el archivo 'non_existent_file.fasta'.

**Caso de prueba 6: Archivo Válido con Diferentes Marcos de Lectura**

```bash
python script.py data.fasta -m 1
```
**Contenido de data.fasta:**
>sequence1
ATCGATCG

**Resultado esperado** 
Te amamos Jenni Rivera, por ti le echamos ganas a la Uni
The number of each nucleotide is:
- Adenine: 2
- Thymine: 2
- Guanine: 2
- Cytosine: 2
La frecuencia de cada codón es: {'TCG': 1, 'ATC': 1}
>sequence1_frame2
UCG


**Caso de Prueba 7: Archivo Válido con Todos los Marcos de Lectura**

```bash
python script.py data.fasta -m 2
```
**Contenido de data.fasta:**
>sequence1
ATCGATCG

**Resultado esperado**
The number of each nucleotide is:
- Adenine: 2
- Thymine: 2
- Guanine: 2
- Cytosine: 2
La frecuencia de cada codón es: {'CGA': 1}
>sequence1_frame3
CGAUCG
