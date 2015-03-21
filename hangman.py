from random import randint

words = [
        "chocolate",
        "ice-cream",
        "cupcake"
        ]

word = words[randint(0,2)]
guessed = False
lives = 6
guess = ['_ '] * len(word)
errors = []


def is_in_word(current_letter):
    in_word = False
    for index, character in enumerate(list(word)):
        if character == current_letter:
            guess[index] = current_letter
            in_word = True
    if not in_word:
        errors.append(current_letter)
    return in_word


print "welcome to hangman!"
print "the word has {} letters".format(len(word))
while not guessed:
    print "{} lives".format(lives)
    print "errors: {}".format(",".join(errors))
    current_letter = raw_input("guess a letter:\n")
    if current_letter not in errors and current_letter not in guess:
        if not is_in_word(current_letter.lower()):
            lives -= 1
        print "".join(guess)
        if '_ ' not in guess:
            guessed = True
            print "Congrats, you win"
        if lives == 0:
            print "too bad, you're dead"
            break
    else:
        print "you've already guessed {}".format(current_letter)


