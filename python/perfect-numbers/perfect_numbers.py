def classify(number):
    if number <= 0:
        raise ValueError('Number has to be positive and higher than 0.')
    if number == 1: return 'deficient'
    aliquot = aliquot_sum(number)
    return (('abundant', 'perfect')[aliquot == number], 'deficient')[aliquot < number]

def aliquot_sum(number):
    return sum((i for i in range(2, number//2 + 1) if number % i == 0))+1

