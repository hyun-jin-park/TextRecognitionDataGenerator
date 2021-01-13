import numpy as np 

PASSPORT_LENGHTH=44
CHARACTER = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z',
             '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '<'])
DICTIONARY_SIZE = 10000

if __name__ == "__main__":
    with open('ocr.txt', 'w') as f:
        for i in range(0, DICTIONARY_SIZE):
            index = np.random.randint(0, len(CHARACTER), size=PASSPORT_LENGHTH)        
            f.write(''.join(CHARACTER[index].tolist()) + '\n')
