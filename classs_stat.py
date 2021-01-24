classes = {}
error = {}
with open('./ko_labels.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()

for line in lines:
    ch = line.strip()
    classes[ch] = 0

with open('./ko_labels_refine.txt', 'w', encoding='utf8') as f:
    for index, ch in enumerate(sorted(classes.keys())):
        f.write(f'{index} {ch}\n')


with open ('./trdg/dicts/kr.txt', 'r', encoding='utf8') as f:
    line = f.readline().strip()
    while line:
        for ch in line:
            if classes.get(ch) is not None:
                classes[ch] += 1
            elif error.get(ch) is not None:
                error[ch] += 1
            else:
                error[ch] = 1
        line = f.readline().strip()

classes_reverse = sorted(classes.items(), reverse=True, key=lambda item: item[1])
for k, v in classes_reverse:
    if v < 10000: 
        print (f'{k}, {v}')

# print('-------------error------------------')
# for k, v in error.items():
#     if v > 1 :
#         print (f'{k}')

