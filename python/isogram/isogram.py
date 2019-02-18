def is_isogram(string):
    aplpha_only = [letter.lower() for letter in string if letter.isalpha()]
    return len(set(aplpha_only)) == len(aplpha_only)
