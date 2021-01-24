words = {}
duplicated = 0 

new_kr_f = open('kr_new.txt', 'w', encoding = 'utf8')

with open('kr.txt', 'r', encoding='utf8') as f:
    line = f.readline().strip()
    while line:
        if len(line.split(' ')) > 1: 
            print(f'{line} has space ')
            line = line.replace(' ', '')

        upper_line = line.upper()        

        if words.get(upper_line) is None:
            words[upper_line] = 1
            new_kr_f.write(f'{upper_line}\n')
        else:            
            duplicated += 1 

        line = f.readline().strip() 

print(f'duplicated line : {duplicated} ')
