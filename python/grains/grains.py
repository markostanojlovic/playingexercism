def on_square(integer_number):
    if not isinstance(integer_number,int) or integer_number not in range(1,65):
        raise ValueError('Error: Not number on chessboard.')
    return [2**x for x in range(integer_number)][integer_number-1]


def total_after(integer_number):
    if not isinstance(integer_number,int) or integer_number not in range(1,65):
        raise ValueError('Error: Not number on chessboard.')
    return sum([2**x for x in range(integer_number)])
