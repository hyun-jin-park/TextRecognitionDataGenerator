import random 

w_f = open('./data/reduce_eng_name_data.txt', 'w', encoding='utf8') 

with open('./data/alien_eng_last_name.txt', 'r', encoding='utf8') as f:
    line = f.readline()
    while (line) :
        if random.randint(0, 10) < 1:
            w_f.write(line) 
        line = f.readline() 
        



