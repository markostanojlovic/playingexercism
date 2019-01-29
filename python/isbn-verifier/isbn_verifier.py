def verify(isbn):
    isbn_strip = isbn.replace('-','')
    if not isbn_strip[:-1].isdigit() or not isbn_strip[-1] in '0123456789X' or not len(isbn_strip)==10:
        return False
    if isbn_strip[-1] == 'X':
        return sum([(10-i)*int(isbn_strip[i]) for i in range(9)], 10) % 11 == 0
    else:
        return sum([(10-i)*int(isbn_strip[i]) for i in range(10)]) % 11 == 0
