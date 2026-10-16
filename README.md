# Human TP53 DNA Sequence Analysis Using Python

## Project Overview
This project performs basic bioinformatics analysis of the human TP53 reference mRNA sequence using Python and Biopython. It analyzes nucleotide composition and calculates sequence length, GC content, and AT content.

## Objectives
- Retrieve a real TP53 reference sequence from NCBI.
- Read FASTA files using Biopython.
- Validate DNA nucleotide characters.
- Calculate sequence length and nucleotide counts.
- Determine GC and AT percentages.
- Run the analysis in VS Code and Google Colab.

## Data Source
- Organism: Homo sapiens
- Gene: TP53 (tumor protein p53)
- Reference accession: NM_000546.6
- Sequence type: mRNA
- NCBI: https://www.ncbi.nlm.nih.gov/nuccore/NM_000546.6

## Tools and Technologies
- Python 3
- Biopython
- Visual Studio Code
- Google Colab
- GitHub

## Analysis Workflow
1. Download the TP53 reference mRNA sequence in FASTA format.
2. Load the sequence using Biopython.
3. Convert the sequence to uppercase.
4. Validate nucleotide characters.
5. Calculate sequence length.
6. Count A, T, G, C, and ambiguous N bases.
7. Calculate GC and AT content.
8. Display and document the results.

## Project Structure
human-tp53-dna-analysis/
- README.md
- dna_analyzer.py
- dna_analyzer.ipynb
- requirements.txt
- data/
    - tp53_mrna.fasta
- results/


## Expected Output
The program reports:
- FASTA sequence identifier
- Sequence length
- Nucleotide counts
- GC content (%)
- AT content (%)

## Scientific Note
The selected accession represents a TP53 mRNA transcript, not the complete genomic DNA region. This project focuses on basic sequence composition and does not diagnose cancer, identify pathogenic variants, or establish gene function.

## Future Improvements
- Extract the annotated coding DNA sequence (CDS).
- Perform DNA-to-protein translation.
- Generate nucleotide composition visualizations.
- Export results to CSV or text reports.
- Add sequence comparison and alignment.

## Author
Beginner-level bioinformatics project developed for educational purposes to explore Python-based biological sequence analysis.
