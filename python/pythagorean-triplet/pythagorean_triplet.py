from itertools import combinations_with_replacement

def triplets_with_sum(sum_of_triplet):
    triplets = []
    comb = combinations_with_replacement([i for i in range(1,sum_of_triplet // 2)], 2)
    for i in comb:
        last = sum_of_triplet - sum(i)
        if last > i[0] and last > i[1]:
            triplet = (*i, last)
            if is_triplet(triplet):
                triplets.append(triplet)
    return set(triplets)


def triplets_in_range(range_start, range_end):
    pass

def is_triplet(triplet):
    t = list(triplet)
    t.sort()
    return t[0]**2 + t[1]**2 == t[2]**2
