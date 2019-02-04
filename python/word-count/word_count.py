def word_count(phrase):
    phrase_spaces = phrase.replace(',', ' ').replace('_', ' ').replace('\t', ' ')
    cleaned_phrase = ''.join([char for char in phrase_spaces if char.isalpha() or char.isnumeric() or char in "' "])
    splitted_phrase = [ word.lower().strip("'") for word in cleaned_phrase.split()]
    return {word: splitted_phrase.count(word) for word in splitted_phrase}
