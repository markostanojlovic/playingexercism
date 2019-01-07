def prime_factors(natural_number):
    remain, factors = natural_number, []
    for _ in range(natural_number):
        gen = (j for j in range(2, remain + 1) if remain % j == 0)
        try:
            factor = next(gen)
        except StopIteration:
            return factors
        factors.append(factor)
        remain = int(remain / factor)
        if remain == 1:
            return factors

