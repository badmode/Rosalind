'''Problem

The GC-content of a DNA string is given by the percentage of symbols
in the string that are 'C' or 'G'. For example, the GC-content of
"AGCTATAG" is 37.5%. Note that the reverse complement of any DNA
string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database.
A commonly used method of string labeling is called FASTA format.
In this format, the string is introduced by a line that begins with
'>', followed by some labeling information. Subsequent lines contain
the string itself; the first line to begin with '>' indicates the label
of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled
by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code
between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp
each).

Return: The ID of the string having the highest GC-content,
followed by the GC-content of that string. Rosalind allows for
a default error of 0.001 in all decimal answers unless otherwise
stated; please see the note on absolute error below.

Sample Dataset

>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

Sample Output

Rosalind_0808
60.919540
'''
'''import math
from Bio import SeqIO
def parser(name, sequence):
    count = 0
    for i in sequence:
        if i == 'G':
            count += 1
        elif i == 'C':
            count += 1
        else:
            count += 0
    print(name)
    print(sequence)
    percentage = float(count/len(sequence))
    print(percentage)
'''

def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))
    return
def parser(name, sequence):
    count = 0
    for i in sequence:
        if i == 'G':
            count += 1
        elif i == 'C':
            count += 1
        else:
            count += 0
    print(name)
    percentage = float((count/len(sequence)) * 100)
    print(percentage, '%')
with open('rosalind_gc.txt') as fp:
    for name, seq in read_fasta(fp):
        parser(name, seq)
