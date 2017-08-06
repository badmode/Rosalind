'''Given: Three positive integers k, m, and n, representing a population
 containing k+m+n organisms: k individuals are homozygous dominant for a
  factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will
 produce an individual possessing a dominant allele (and thus displaying
 the dominant phenotype). Assume that any two organisms can mate.
Sample Dataset

2 2 2

Sample Output

0.78333
'''
def mendel(k,m,n):
	pop = k + m + n
	pop += 0.0

	DD0 = (k/pop)

	Dr0 = (m/pop)*(k/(pop-1))
	Dr1 = (m/pop)*((m-1)/(pop-1))*(0.75)
	Dr2 = (m/pop)*(n/(pop-1))*(0.5)
	het0 = Dr0 + Dr1 + Dr2
	rr0 = (n/pop)*(k/(pop-1))
	rr1 = (n/pop)*(m/(pop-1))*(0.5)
	rec0 = rr0 + rr1
	return DD0 + het0 + rec0
print mendel(27, 29, 27)
