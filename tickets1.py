num_tickets = 8
tickets_liked = int(raw_input("How many tickets would you like?:\n"))

message_string = ""
if tickets_liked <= num_tickets:
    num_tickets = num_tickets - tickets_liked
    message_string = "OK! {} tickets for you. {} tickets left"
else:
    message_string = "Sorry! Can't give you {} tickets. Only {} tickets left"

print message_string.format(tickets_liked, num_tickets)

