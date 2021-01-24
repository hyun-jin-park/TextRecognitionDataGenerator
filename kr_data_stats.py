import os

# path = './trdg/dicts/kr.txt'
path = 'kr_new.txt'

korean = 0
english = 0
digits = 0
symbol = 0 

other = {} 

new_f = open('kr3.txt', 'w', encoding='utf8')

with open(path, 'r') as f:

    line = f.readline().strip()
    while (line):
        valid = True
        for ch in line: 
            if ord('가') <= ord(ch)  <= ord('힣') : 
                korean += 1 
            elif ord('a') <= ord(ch) <= ord('z') or ord('A') <= ord(ch) <= ord('Z'):
                english += 1
            elif ch in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                digits += 1
            elif ch in ['.', '(', ')', '-' ] :
                symbol += 1
            else:
                if other.get(ch) is not None:
                    other[ch] += 1
                else:
                    other[ch] = 1             
                valid = False 
                break

        if valid:
            new_f.write(line + '\n')

        line = f.readline().strip()

print (f'korean: {korean} english: {english} digits:{digits} symbol: {symbol}')

for k, v in other.items():
    print (f'{k} {v}')


