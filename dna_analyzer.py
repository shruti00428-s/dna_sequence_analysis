#DNA sequence Analyzer

from Bio import SeqIO

#Read fasta file 
sequence = SeqIO.read("data/tp53.fasta", "fasta")

#Calculate sequence length
length = len(sequence)

#Count each nucleotide
a_count = sequence.count("A")
t_count = sequence.count("T")
g_count = sequence.count("G")
c_count = sequence.count("C")

#Calculate GC and AT content
gc_content = ((g_count + c_count)/length)*100

at_content = ((a_count + t_count)/length)*100


#Display the results 
print("DNA SEQUENCE ANALYZER")
print("---------------------")
print("DNA Sequence:", sequence)
print("Sequence Length:", length)
print("A Count:", a_count)
print("T Count:", t_count)
print("G Count:", g_count)
print("C Count:", c_count)
print(f"GC Content:{gc_content:2f}%")
print(f"AT Content:{at_content:2f}%")


