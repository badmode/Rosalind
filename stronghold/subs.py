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
def findall_iter(sub, string):
    """
    >>> text = "Allowed Hello Hollow"
    >>> tuple(findall_iter('ll', text))
    (1, 10, 16)
    """
    def next_index(length):
        index = 0 - length
        while True:
            index = string.find(sub, index + length)
            yield index
    return iter(next_index(len(sub)).next, -1)
print(findall_iter('ATAT','GATATATGCATATACTT'))
