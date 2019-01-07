import string
from functools import reduce


def prod(digi_string):
    digi_list = [int(i) for i in list(digi_string)]
    return reduce(lambda x, y: x * y, digi_list)


def largest_product(series, size):
    if size > len(series) or size < 0:
        raise ValueError('Error: Wrong size.')
    if size == 0 or series == '':
        return 1
    if not series.isdigit():
        raise ValueError('Error: series must have only digits')
    combinations = (series[i:size+i] for i in range(0, len(series)-size+1))
    products = (prod(combination) for combination in combinations)
    return max(products)
