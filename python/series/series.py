def slices(series, length):
    if len(series) == 0 or length > len(series) or length < 1:
        raise ValueError('Bad input values.')
    iterations = len(series) - length + 1
    result = []
    for i in range(iterations):
        result.append(series[:length])
        tmp = list(series)
        tmp.remove(tmp[0])
        series = ''.join(tmp)
    return result
