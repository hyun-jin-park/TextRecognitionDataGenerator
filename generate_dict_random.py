import random
strings = []
with open('./result.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()

for line in lines:
    items = line.strip().split(',')
    strings.append(items[0])

f = open('random.txt', 'w', encoding='utf8')
for i in range(3, 10):
    for j in range(0, 200000):
        candidate = random.sample(strings, i)
        f.write(''.join(candidate) + '\n')

        


