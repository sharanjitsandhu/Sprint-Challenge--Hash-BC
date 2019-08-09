#  Hint:  You may not need all of these. Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # Create a hashtable with a source and a destination
    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
        if tickets[i].source == "NONE":
            curr_destination = tickets[i].destination
            route[0] = curr_destination

    # Iterating over the rest of an array after first index in the route
    for i in range(1, length):
        next_destination = hash_table_retrieve(hashtable, curr_destination)
        route[i] = next_destination
        curr_destination = next_destination

    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

print(reconstruct_trip(tickets, 3))
