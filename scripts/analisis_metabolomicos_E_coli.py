'''
Nombre:
    Análisis metabolómicos de E. Coli

Version:
    3.12.2

Autor:
    Galán Hernández Frida
    García González Carlos

Descripcion:
    Este programa hecho en Python tienen la funcionalidad de calcular la frecuencia de nucleótidos, 
    la frecuencia de codones, además de que transcribe una secuencia de DNA a RNA y la traduce a una cadena de aminoácidos
Argumentos:
    - nombre archivo (path)
    - n (T,A,G,C) para establecer el nucleótido de interesa 
    - m (0,1,2) para establecer el marco de lectura, solo forward 
Usage:
    python scripts/analisis_DNA.py PATH DE LA ARCHIVO CON LA SECUENCIA -n NUCLEÓTIDO -m MARCO DE LECTURA
    python3 scripts/analisis_DNA.py /Users/frida_galan/Desktop/PythonSEM2/Notas_Biopython/seq.nt.fa -n T -m 0 
'''
# Librerias estadar importadas para la función del programa
import sys
import argparse

# Importaciones especificas de la libreria Biopython
from Bio import SeqIO
from Bio.Seq import Seq

# Se ajustan las rutas segun el entorno virtual de Python
sys.path.append("/Users/frida_galan/Desktop/PythonSEM2/Proyecto_final/analisis_DNA/operations")
sys.path.append("/Users/frida_galan/Desktop/PythonSEM2/Proyecto_final/analisis_DNA/utils")
# Aplicaciones locales del paquete
from file_io import read_dna_sequence
from validators import validate_fasta_format
from calcular_contenido_nucleotidos import calculate_nucleotide_content
from calcular_frecuencia_codones import calculate_codon_frequency
from traduccion_dna import translate_sequence
from transcrito_dna import transcribe_sequence
from file_io import ignore_head_FASTA

'''Se parsean los argumentos usando la libreria de argparse'''
parser = argparse.ArgumentParser(
    description="El siguiente script sirve para analizar una secuencia de DNA, incluye distintas funcionalidades")

parser.add_argument("Input_file",
                    help="El nombre o la ruta al archivo FASTA que se quiera procesar",
                    type=str)

parser.add_argument("-n", "--Nucleotidos",
                    help="El nucleótido para calcular cuántas veces aparece, por defecto son los 4 (A T G C)",
                    type=str,
                    default="ATCG",
                    choices=["A", "T", "G", "C"],
                    required=False)

parser.add_argument("-m", "--Marco_lectura",
                    help="El marco de lectura a elegir, solo se puede FORWARD, inserte 0 para el mc 1, 1 para mc 2 o 2 para mc 3",
                    type=int,
                    default=0,
                    choices=[0, 1, 2],
                    required=False)

args = parser.parse_args()

if __name__ == "__main__":
    print("Te amamos Jenni Rivera, por ti le echamos ganas a la Uni")
 
    # Abrimos archivo y realizamos validaciones de formato
    ruta_archivo = args.Input_file
    path_seq= read_dna_sequence(ruta_archivo)
    val_fasta = validate_fasta_format(ruta_archivo)
    secuencia = ignore_head_FASTA(ruta_archivo)

    if val_fasta:
        # Calculamos la cantidad de nucleótidos 
        calculate_nucleotide_content(secuencia, args.Nucleotidos)

        # Calculamos la frecuencia de codones 
        frec_codons = calculate_codon_frequency(secuencia)
        print(f"La frecuencia de cada codón es: {frec_codons}")

        #Transcripción de la secuencia de DNA dada por el usuario 
        print(f"La transcripción de la secuencia de DNA del archivo {ruta_archivo} es la siguiente: \n")
        transcribe_sequence(args.Marco_lectura,ruta_archivo)

        # Traducción de la secuencia de DNA dada por el usuario
        print(f"La traducción de la secuencia de DNA del archivo {ruta_archivo} es la siguiente: \n") 
        translate_sequence(args.Marco_lectura, ruta_archivo)



