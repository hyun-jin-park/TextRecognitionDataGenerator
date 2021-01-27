from os import write
import random 
classes = {}

with open('kr_labels.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        try: 
            classes[line.split()[1]] = 0
        except:
            print(line)
            exit(1)

with open('kr_labels.txt', 'w', encoding='utf8') as f:
    for index, k in enumerate(sorted(classes.keys())):
        f.write(f'{index}\t{k}\n')


def strip_invalid_character(line):
    result = ''
    for ch in line: 
        if classes.get(ch) is not None:
            result += ch 
    return result 


def write_dictionary(path, dictionary):
    with open(path, 'w', encoding='utf8') as f:
        for k in sorted(dictionary.keys()):
            f.write(f'{k}\n')


def read_dictionary(path):
    word_dictionary = {}    

    with open(path, 'r', encoding='utf8') as f:
        line = f.readline()
        while (line) :
            line = line.strip()
            line = strip_invalid_character(line)
            if len(line) > 0 : 
                for ch in line:
                    classes[ch] +=1 
                if word_dictionary.get(line) is not None: 
                    word_dictionary[line] += 1 
                else:
                    word_dictionary[line] = 1
            line = f.readline() 
    return word_dictionary


kor_words = read_dictionary('./data/final/kor_name.txt')
address_words = read_dictionary('./data/final/address.txt')

write_dictionary('./data/final/kor_name_no_invalid.txt', kor_words)
write_dictionary('./data/final/address_no_invalid.txt', address_words)

classes_reverse = sorted(classes.items(), reverse=True, key=(lambda x: x[1]))
with open('classes.txt', 'w', encoding='utf8') as f:
    for item in classes_reverse:
        f.write(f'{item[0]} {item[1]}\n')

# classes = {}
# with open('classes.txt', 'r', encoding='utf8') as f:
#     lines = f.readlines()
#     for line in lines:
#         items = line.strip().split()
#         word = items[0]
#         count = int(items[1])        
#         if ord('A') <= ord(word) <= ord('Z'):
#             continue 

#         if count < 1000 : 
#             classes[word] = count

wf = open('from_wiki_data', 'w', encoding='utf8') 

with open('namuwiki_dictionary.txt', 'r', encoding='utf8') as f:
    line = f.readline()
    while line:
        word = line.strip().split()[0]
        word = strip_invalid_character(word)
        if len(word) < 15: 
            is_write = True
            for ch in word:
                if classes.get(ch) is not None and classes[ch] < 1000:
                    classes[ch] += 1
                    if is_write:
                        is_write = False
                        wf.write(f'{word}\n')                    
        line = f.readline()
wf.close()

low = 0 
arr = [] 
for k, v in classes.items():
    if v < 1000:
        print (f'{k} {v}')
        low += 1
        arr.append(k)

import random
with open('kor_random.txt', 'w', encoding='utf8') as f:
    for i in range(2, 11):
        arr = [] 
        for k, v in classes.items():
            if v < 1000:
                arr.append(k)

        if len(arr) == 0:
            break

        for j in range(0, 2000):
            line = random.sample(arr, i)
            for ch in line: 
                classes[ch] += 1
            line = ''.join(line)
            f.write(f'{line}\n')

print ('-----------final----------')
for k, v in classes.items():
    if v < 1000:
        print (f'{k} {v}')
        low += 1
        arr.append(k)
