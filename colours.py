colour_responses = {
                    "red" : "and violets are blue",
                    "green": "i like turtles",
                    "blue": "once upon a blue moon...",
                    "yellow": "pikachuuuuu",
                    "purple": "are you chuck bass?",
                    "mint": "oh so fresh. kinda like toothpaste.",
                    "black": "looks good on everyone"
                    }

fav_colour = raw_input("What's your favorite colour?:\n").lower()

print colour_responses.get(fav_colour, "{}? Goodness.".format(fav_colour))
