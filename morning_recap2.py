parsed = False
user_input = 0
while not parsed:
    try:
        user_input = int(raw_input("gimme a number:\n"))
        parsed = True
    except ValueError:
        print "not a number, try again."

if user_input < 10 or user_input > 20:
    print "your input is less than 10 or greater than 20"
elif user_input > 10 and user_input < 20:
    print "your input is greater than 10 and less than 20"
else:
    print "your input doesn't matter"


