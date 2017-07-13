'''Given: Two positive integers a and b (a<b<10000).

Return: The sum of all odd integers from a
through b, inclusively.

Sample Dataset

100 200

Sample Output

7500
'''

start = 4665
end = 9326
to_be_summed = []
for all in range(start, end):
    if start % 2 == 0:
        start += 1
    else:
        to_be_summed.append(start)
        start += 1
print(sum(to_be_summed))
