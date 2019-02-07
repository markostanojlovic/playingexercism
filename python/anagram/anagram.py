from collections import Counter

def find_anagrams(word, candidates):
    return [candidate for candidate in candidates
                if Counter(candidate.lower()) == Counter(word.lower())
                and not word.lower() == candidate.lower()]
