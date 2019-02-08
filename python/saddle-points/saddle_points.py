def saddle_points(matrix):
    saddles = []
    if len(matrix) == 0:
        return set(saddles)
    try:
        reverse_matrix = [[row[col] for row in matrix] for col in range(len(matrix[0]))]
    except IndexError:
        raise ValueError('Irregular matrix')
    for index, row in enumerate(matrix):
        max_indexes = [i for i, value in enumerate(row) if value == max(row)]
        for max_index in max_indexes:
            if row[max_index] == min(reverse_matrix[max_index]):
                saddles.append((index+1, max_index+1))
    return set(saddles)
