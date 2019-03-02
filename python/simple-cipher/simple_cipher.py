from string import ascii_lowercase
from secrets import choice as RND


class Cipher(object):
    def __init__(self, key=None):
        self.key = ''.join((RND(ascii_lowercase) for i in range(100))) if not key else key

    def shift(self, direction, letter, coder):
        side = 1 if direction == 'left' else -1
        shifted = ord(letter) + side*(ord(coder) - 97) # ord('a') = 97
        return shifted if shifted in range(97, 123) else shifted - side*26 # ord('z') = 122

    def encode(self, text):
        encoded = ''
        key_pointer = list(self.key)
        for char in text:
            coder = key_pointer.pop(0)
            encoded += chr(self.shift('left', char, coder))
            key_pointer.append(coder)
        return encoded

    def decode(self, text):
        decoded = ''
        key_pointer = list(self.key)
        for char in text:
            coder = key_pointer.pop(0)
            decoded += chr(self.shift('right', char, coder))
            key_pointer.append(coder)
        return decoded
