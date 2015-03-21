from random import randint

number = randint(1,10)
playing = True

while playing:
    parsed = False
    guess = 0
    while not parsed:
        try:
            guess = int(raw_input("What number, from 1 to 10 am I thinking of?\n"))
            parsed = True
        except ValueError:
            print "that's not a number, try again"

    if guess > number:
        print "your guess is too high, try again"
    elif guess < number:
        print "your guess is too low, try again"
    else:
        print "yes, the number is {}! you win!".format(number)
        playing = False
