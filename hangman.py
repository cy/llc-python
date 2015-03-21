from random import randint

words = [
        "chocolate",
        "icecream",
        "cupcake"
        ]

word = words[randint(0,len(words)-1)]
guessed = False
guess = ['_ '] * len(word)
errors = []

hangman = [
""""
------
|    |
|
|
|
|
|
|
|
------
""",
""""
------
|    |
|    0
|
|
|
|
|
|
------
""",
""""
------
|    |
|    0
|   -+-
|
|
|
|
|
------
""",
""""
------
|    |
|    0
|  /-+-
|
|
|
|
|
------
""",

""""
------
|    |
|    0
|  /-+-/
|    |
|    
|   
|
|
------
""",
""""
------
|    |
|    0
|  /-+-/
|    |
|    | 
|   
|
|
------
""",
""""
------
|    |
|    0
|  /-+-/
|    |
|    | 
|   /
|
|
------
""",
""""
------
|    |
|    0
|  /-+-/
|    |
|    | 
|   / \\
|
|
------
"""
]

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
print hangman[0]
print "".join(guess)
while not guessed:
    print "errors: {}".format(",".join(errors))
    current_letter = raw_input("guess a letter:\n")
    if current_letter not in errors and current_letter not in guess:
        is_in_word(current_letter.lower())
        print "".join(guess)
        print hangman[len(errors)]
        if '_ ' not in guess:
            guessed = True
            print "Congrats, you win"
        if len(errors) == len(hangman) - 1:
            print "too bad, you're dead. the word was {}".format(word)
            break
    else:
        print "you've already guessed {}".format(current_letter)

