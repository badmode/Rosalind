from Bio import SeqIO

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
