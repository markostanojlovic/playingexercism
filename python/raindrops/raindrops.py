def raindrops(number):
    word = ''
    if number % 3 == 0:
        word += "Pling"
    if number % 5 == 0:
        word += "Plang"
    if number % 7 == 0:
        word += "Plong"
    if word == '':
        word = str(number)
    return word
