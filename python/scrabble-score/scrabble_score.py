ScrubblePoints = {
    1 : 'AEIOULNRST',
    2 : 'DG',
    3 : 'BCMP',
    4 : 'FHVWY',
    5 : 'K',
    8 : 'JX',
    10 : 'QZ'}

def score(word):
    score_sum = 0
    for letter in word:
        score_sum += [points for points, letters in ScrubblePoints.items() if letter.upper() in letters][0]
    return score_sum
