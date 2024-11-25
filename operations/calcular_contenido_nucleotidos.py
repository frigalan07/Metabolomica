'''
calcular_contenido_nucleotidos: Modulo para calcular el contenido de cada nucleotido en secuencias de DNA.

Este módulo proporciona funciones para determinar las veces que aparece un nucleotido  
en una secuencia de ADN dada. Esto es util para estudios genéticos y genómicos ya que proporciona
informacion importante para la comprensión y manipulación del material genético.

Funciones:
- calculate_nucleotide_content(DNA, nucleotide): Devuelve el número de apariciones los nucleotidos en la secuencia.
'''

def calculate_nucleotide_content(DNA, nucleotide):
    '''
    Calcula el contenido porcentual de cada codon en una secuencia de ADN.

    Args:
        DNA (str): La secuencia de ADN a analizar.
        nucleotide (str): El nucleotido o nucleotidos a contar.

    Returns:
        int: El número de veces que aparece un nucleótido específico o los 4 de una secuencia dada.
    '''
    
    if nucleotide=="A":
        print(f"El total de Adeninas es:{DNA.upper().count('A')}") 
    
    if nucleotide=="T":
        print(f"El total de Timinas es:{DNA.upper().count('T')}")

    if nucleotide=="G":
        print(f"El total de guaninas es:{DNA.upper().count('G')}")

    if nucleotide=="C":
        print(f"El total de citocinas es:{DNA.upper().count('C')}")

    if nucleotide=="ATGC":
        print(f"El total de cada base es: A:{DNA.upper().count('A')} C:{DNA.upper().count('C')} T:{DNA.upper().count('T')} G:{DNA.upper().count('G')}")

