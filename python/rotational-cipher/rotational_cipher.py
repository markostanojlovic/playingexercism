from string import ascii_letters

def shift(char, size):
    if not char in ascii_letters:
        return char
    shifted =  ord(char.lower()) + size
    new_ord = shifted if shifted < 123 else shifted - 26
    if char.isupper():
        return chr(new_ord - 32)
    else:
        return chr(new_ord)

def rotate(text, key):
    if type(key) != int or not key in range(0,27):
        raise ValueError('Wrong key')
    return ''.join([shift(chr,key) for chr in text])
