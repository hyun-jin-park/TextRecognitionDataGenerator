classes = {}
with open('./ko_labels.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()

for line in lines:
    ch = line.strip()
    classes[ch] = 0

with open('./ko_labels_refine.txt', 'w', encoding='utf8') as f:
    for index, ch in enumerate(sorted(classes.keys())):
        f.write(f'{index} {ch}\n')

