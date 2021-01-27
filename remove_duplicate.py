import numpy as np 


# def is_valid_eng_name(name):
#     for ch in name:
#         if ord('A') <= ord(ch) <= ord('Z') or ch == '-':
#             pass
#         else:
#             return False
#     return True

# w_f = open('./data/reduce_eng_name_remove_duplicate.txt', 'w', encoding='utf8') 

# dictionary = {} 
# with open('./data/reduce_eng_name_data.txt', 'r', encoding='utf8') as f:
#     line = f.readline()
#     while (line) :
#         line = line.strip()
#         if is_valid_eng_name(line):            
#             if dictionary.get(line) is None :
#                 dictionary[line] = 1 
#                 w_f.write(line + '\n') 
#             else:
#                 dictionary[line] += 1 
#         line = f.readline() 


ch_dictionary = {}
word_dictionary = {}
sample = 0 
with open('./data/reduce_eng_name_remove_duplicate.txt', 'r', encoding='utf8')  as f:
    line = f.readline()
    while (line) :
        line = line.strip()
        word_dictionary[line] = 1
        for ch in line:
            if ch_dictionary.get(ch) is None:
                ch_dictionary[ch] = 0 
            else:
                ch_dictionary[ch] += 1
            sample += 1
        line = f.readline() 
    
sum = 0
for k, v in ch_dictionary.items():
    ch_dictionary[k] = sample /v 
    sum += ch_dictionary[k]

result = 0 
for k, v in ch_dictionary.items():
    ch_dictionary[k] = v/sum 
    print (f'{k} {v}')
    result += ch_dictionary[k]

print(f'total{result}')

arr_ch = [] 
arr_prob = []
for k in sorted(ch_dictionary.keys()):
    arr_ch.append(k) 
    arr_prob.append(ch_dictionary[k])
    
print(arr_ch)
print(arr_prob)
w_f = open('./data/random_eng_name.txt', 'w', encoding='utf8')

arr_ch = np.array(arr_ch)

for j in range(2, 15):
    for i in range(100):
        choice = np.random.choice(len(arr_ch), j, p=arr_prob)
        word = ''.join(arr_ch[choice])
        if word_dictionary.get(word) is None:
            w_f.write(f'{word}\n')
            word_dictionary[word] = 1 

with open('./data/random_eng_name.txt', 'r', encoding='utf8') as f:
    line = f.readline()
    while (line) :
        line = line.strip()
        word_dictionary[line] = 1
        for ch in line:
            if ch_dictionary.get(ch) is None:
                ch_dictionary[ch] = 0 
            else:
                ch_dictionary[ch] += 1
            sample += 1
        line = f.readline() 

sum = 0
for k, v in ch_dictionary.items():
    ch_dictionary[k] = v/sample
    print (f'{k} {v}')
