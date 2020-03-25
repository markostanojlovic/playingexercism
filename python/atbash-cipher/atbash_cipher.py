from string import ascii_lowercase as lc
from string import digits

def encode(plain_text):
    encoded = [char for char in 
                   [lc[-1 * (lc.index(char) + 1)] 
                        if char in lc else char 
                        for char in list(plain_text.replace(' ', '').lower())]
                   if char in lc + digits]
    return ''.join(list(letter + ' ' if index % 5 == 0 
                    else letter 
                    for index, letter in enumerate(list(encoded), start=1))).strip()


def decode(ciphered_text):
    return encode(ciphered_text).replace(' ','')
