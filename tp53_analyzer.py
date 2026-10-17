#tp53 sequence Analyzer

#check the version of biopython 
import Bio; print(Bio.__version__)

#import SeqIO module from Biopython 
from Bio import SeqIO

#read FASTA file
record = SeqIO.read("data/human_tp53_sequence.fasta", "fasta")

#validate the nucleotide sequence
valid_bases = set("ACGTN")

if not record.seq:
    raise ValueError("The FASTA Sequence is empty.")

if not set(record.seq).issubset(valid_bases):
    raise ValueError("Unexpected characters in the DNA Sequence.")


#Calculate sequence length
length = len(record.seq)

#Count each nucleotide
a_count = record.seq.count("A")
t_count = record.seq.count("T")
g_count = record.seq.count("G")
c_count = record.seq.count("C")
n_count = record.seq.count("N")


#Calculate GC and AT content
gc_content = ((g_count + c_count)/length)*100

at_content = ((a_count + t_count)/length)*100


#Display the results 
print("HUMAN TP53 SEQUENCE ANALYSIS")
print("---------------------")
print("TP53 Sequence:", record.seq)
print("Sequence Length:", length)
print("A Count:", a_count)
print("T Count:", t_count)
print("G Count:", g_count)
print("C Count:", c_count)
print("N Count:", n_count)
print(f"GC Content:{gc_content:2f}%")
print(f"AT Content:{at_content:2f}%")
print(f"Unclassified bases: {n_count}")


