def getAvailableLetters(lettersGuessed):
    import string
    available = string.ascii_lowercase
    for letter in lettersGuessed:
        available = available.replace(letter, '')
    return available 

print(getAvailableLetters(['a', 'z', 'a', 'o']))
