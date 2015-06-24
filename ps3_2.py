def isWordGuessed(secretWord, lettersGuessed):
    for letter in lettersGuessed:
        secretWord = secretWord.replace(letter, '')
    if secretWord == '':
        return True
    return False

print(isWordGuessed('aaabb', ['c','a','a']))
