'''Given: Two DNA strings s and t

(each of length at most 1 kbp).

Return: All locations of t
as a substring of s

.
Sample Dataset

GATATATGCATATACTT
ATAT

Sample Output

2 4 10
'''

s = 'GATATATGCATATACTT'
s2 = 'ATAT'
print s.find(s2)
