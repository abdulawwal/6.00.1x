def isWordGuessed(secretWord, lettersGuessed):
    for letter in lettersGuessed:
        secretWord = secretWord.replace(letter, '')
    if secretWord == '':
        return True
    return False

def getGuessedWord(secretWord, lettersGuessed):
    notGuessed = set(secretWord)
    
    for letter in lettersGuessed:
        if letter in secretWord:
            notGuessed.remove(letter)
    for letter in notGuessed:
        secretWord = secretWord.replace(letter, ' _ ')
    return secretWord

def getAvailableLetters(lettersGuessed):
    import string
    available = string.ascii_lowercase
    for letter in lettersGuessed:
        available = available.replace(letter, '')
    return available 

def hangman(secretWord):
    lettersGuessed = []
    guesses = 8
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of word that is', len(secretWord), 'letters long.'
    while not isWordGuessed(secretWord, lettersGuessed) and guesses > 0:
        print '----------'
        print 'You have', guesses, 'guesses left.'
        print 'Available letters:', getAvailableLetters(lettersGuessed)
        guess = raw_input('Please guess a letter: ')
        guess = guess.lower()
        if guess in lettersGuessed:
            print "Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed)
        elif guess not in getAvailableLetters(lettersGuessed) or len(guess) != 1:
            next
        else:
            lettersGuessed.append(guess)
            if guess not in secretWord:
                print "Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed)
                guesses = guesses - 1
            else:
                print "Good guess:", getGuessedWord(secretWord, lettersGuessed)
    if isWordGuessed(secretWord, lettersGuessed):
        print '-------------'
        print 'Congratulations, you won!'
    else:
        print '-------------'
        print 'Sorry, you ran out of guesses. The word was', secretWord

hangman('apple')
    
