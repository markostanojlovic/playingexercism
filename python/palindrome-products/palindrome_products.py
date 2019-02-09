def check_input(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError('Bad input.')

def is_palindrome(number):
    if len(str(number)) == 1:
        return True
    num_to_list = [digit for digit in str(number)]
    num_to_list.reverse()
    return number == int(''.join(num_to_list))

def find_palindrome_factors(min_factor, max_factor):
    factors = list(range(min_factor, max_factor+1))
    palindrom_factors = []
    for num in range(min_factor, max_factor+1):
        palindrom_factors += list(((num, factor) for factor in factors if is_palindrome(factor * num)))
        factors.pop(0)
    return palindrom_factors

def largest_palindrome(min_factor, max_factor):
    maxp = max(pal[0]*pal[1] for pal in find_palindrome_factors(min_factor, max_factor))
    return maxp, set(pal for pal in find_palindrome_factors(min_factor, max_factor) if pal[0]*pal[1] == maxp)

def smallest_palindrome(min_factor, max_factor):
    minp = min(pal[0]*pal[1] for pal in find_palindrome_factors(min_factor, max_factor))
    return minp, set(pal for pal in find_palindrome_factors(min_factor, max_factor) if pal[0]*pal[1] == minp)
