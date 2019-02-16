from functools import reduce

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def raindrops(number):
    word = ''
    factorized = factors(number)
    found = False
    if 3 in factorized:
        word += "Pling"
        found = True
    if 5 in factorized:
        word += "Plang"
        found = True
    if 7 in factorized:
        word += "Plong"
        found = True
    if not found:
        word = str(number)
    return word
