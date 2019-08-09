#  Hint:  You may not need all of these. Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(0, length):
        hash_table_insert(ht, weights[i], i)

    for i in range(0, length):
        element = limit - weights[i]
        index = hash_table_retrieve(ht, element)
        if index:
            return (index, i)

    return None


weights = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(weights, 5, 25))


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
