'''Problem

Given: A string s of length at most 10000 letters.

Return: The number of occurrences of each word in s, where words
are separated by spaces. Words are case-sensitive,
and the lines in the output can be in any order.

Sample Dataset

We tried list and we tried dicts also we tried Zen

Sample Output

and 1
We 1
tried 3
dicts 1
list 1
we 2
also 1
Zen 1
'''

sentence = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'
new = {}

for words in sentence.split(' '):
    if words not in new:
        new[words] = 1
    else:
        new[words] += 1
for key, value in new.items():
    print key, value
