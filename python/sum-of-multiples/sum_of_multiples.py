def sum_of_multiples(limit, multiples):
    s = set()
    for i in [x for x in multiples if x != 0]:
        s.update([j for j in range(1,limit) if j%i == 0])
    return sum(s)
