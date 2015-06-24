def getGuessedWord(secretWord, lettersGuessed):
    notGuessed = set(secretWord)
    
    for letter in lettersGuessed:
        if letter in secretWord:
            notGuessed.remove(letter)
    for letter in notGuessed:
        secretWord = secretWord.replace(letter, ' _ ')
    return secretWord
        

print(getGuessedWord('apple', ['a']))
