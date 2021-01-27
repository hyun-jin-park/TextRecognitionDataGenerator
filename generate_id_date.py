import os
import random 

general_id_target = 5000
driver_id_target  = 3000
date_target = 2000

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

with open('id_date_single_char.txt', 'w' , encoding='utf8') as f:
    for i in range(0, general_id_target):
        first =  ''.join(random.sample(digits, 6))
        second = ''.join(random.sample(digits, 7))
        f.write(f'{first}-{second}\n')
    
    for i in range(0, driver_id_target):
        first = ''.join(random.sample(digits, 2))
        second = ''.join(random.sample(digits, 2))
        third = ''.join(random.sample(digits, 6))
        fourth = ''.join(random.sample(digits, 2))
        f.write(f'{first}-{second}-{third}-{fourth}\n')

    for i in range(0, date_target):
        first = ''.join(random.sample(digits, 4))
        seonc = ''.join(random.sample(digits, 2))
        third = ''.join(random.sample(digits, 2))
        f.write(f'{first}.{second}.{third}.{fourth}\n')
        f.write(f'{first}.{second}.{third}.{fourth}.\n')