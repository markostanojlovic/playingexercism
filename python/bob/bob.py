def hey(phrase):
    phrase = phrase.strip()
    if phrase.isspace() or phrase == '':
        phraseType = 'silence'
    elif phrase[-2:] == '!?' or phrase[-2:] == '?!' or (phrase.isupper() and phrase[-1] == '?'):
        phraseType = 'question yelling'
    elif phrase[-1] == '?':
        phraseType = 'question'
    elif phrase.isupper():
        phraseType = 'yelling'
    else:
        phraseType = 'Whatever.'
    response = {
        'question' : 'Sure.',
        'yelling' : 'Whoa, chill out!',
        'question yelling' : "Calm down, I know what I'm doing!",
        'silence' : 'Fine. Be that way!'
    }
    return response.get(phraseType, 'Whatever.')
