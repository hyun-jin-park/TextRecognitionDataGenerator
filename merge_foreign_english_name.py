
def convert_passport_name(converter, src):
    result = ''
    src = src.upper()
    for ch in src:
        if ord('A') <= ord(ch) <= ord('Z') or ch == '-':
            result += ch 
            continue

        if converter.get(ch) is not None:
            result += converter[ch]
    return result 


first_name = {}
last_name = {} 

passport_character_converter = {}
with open ('./data/passport_character_conversion.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()
    for line in lines:
        item = line.strip().split()
        src = item[0]
        target = item[1]
        passport_character_converter[src] = target 

def save_data(file_path, dictionary):
    with open(file_path, 'w', encoding='utf8') as f:
        for k in dictionary.keys():
            f.write(f'{k}\n')


def load_data(file_path, dictionary):
    with open(file_path, 'r', encoding='utf8') as f:
        lines = f.readlines( )
        for line in lines:
            name = line.strip().split()
            if len(name) > 0 :
                name = name[0].upper()
                passport_name = convert_passport_name(passport_character_converter, name)
                dictionary[name] = 0


load_data('./data/name-dataset/names_dataset/first_names.all.txt', first_name) 
print(f'{len(first_name)}')
load_data('./data/NameDatabases/NamesDatabases/first names/all.txt', first_name)
print(f'{len(first_name)}')
load_data('./data/People-Name-List/Crawled-People-Names/First names', first_name)
print(f'{len(first_name)}')

load_data('./data/name-dataset/names_dataset/last_names.all.txt', last_name)
print(f'{len(last_name)}')
load_data('./data/NameDatabases/NamesDatabases/surnames/all.txt', last_name)
print(f'{len(last_name)}')
load_data('./data/People-Name-List/Crawled-People-Names/Last Names', last_name)
print(f'{len(last_name)}')


save_data('merged_first_name', first_name)
save_data('merged_last_name', last_name)
