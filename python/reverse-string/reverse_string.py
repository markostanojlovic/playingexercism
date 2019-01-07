def reverse(text):
    try:
        return text[::-1]
    except TypeError: 
        print('Input must be string')
