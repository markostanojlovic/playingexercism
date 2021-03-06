from collections import Counter

def word_count(phrase):
    phrase_spaces = phrase.replace(',', ' ').replace('_', ' ').replace('\t', ' ')
    cleaned_phrase = ''.join((char for char in phrase_spaces if char.isalpha() or char.isnumeric() or char in "' "))
    return dict(Counter((word.lower().strip("'") for word in cleaned_phrase.split())))
