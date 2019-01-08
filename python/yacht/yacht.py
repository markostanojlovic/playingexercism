# Score categories
# Change the values as you see fit
YACHT = 'yacht'
ONES = 'ones'
TWOS = 'twos'
THREES = 'threes'
FOURS = 'fours'
FIVES = 'fives'
SIXES = 'sixes'
FULL_HOUSE = 'full'
FOUR_OF_A_KIND = 'four'
LITTLE_STRAIGHT = 'littles'
BIG_STRAIGHT = 'bigs'
CHOICE = 'choice'

def yacht(dice):
    if all([x == dice[0] for x in dice]):
        return 50
    else:
        return 0

def ones(dice):
    return dice.count(1)

def twos(dice):
    return 2 * dice.count(2)

def threes(dice):
    return 3 * dice.count(3)

def fours(dice):
    return 4 * dice.count(4)

def fives(dice):
    return 5 * dice.count(5)

def sixes(dice):
    return 6 * dice.count(5)

def full(dice):
    if len(set(dice)) == 2 and dice.count(dice[0]) in [2,3]:
        return sum(dice)
    else:
        return 0

def four(dice):
    dice_set = set(dice)
    counts = [dice.count(i) for i in dice_set]
    if len(counts) > 2:
        return 0
    elif len(counts) == 1:
        return 4 * dice[0]
    else:
        if counts[0] == 4:
            return 4 * dice[0]
        else:
            return 4* dice[1]

def littles(dice):
    if set(dice) == set([1,2,3,4,5]):
        return 30
    else:
        return 0

def bigs(dice):
    if set(dice) == set([2,3,4,5,6]):
        return 30
    else:
        return 0

def choice(dice):
    return sum(dice)


def score(dice, category):
    return globals()[category](dice)
