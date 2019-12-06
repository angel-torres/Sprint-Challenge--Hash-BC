#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # add all weights to ht
    for weight in weights:
        hash_table_insert(ht, weight, weight)
    
    # initialice indices list
    indices = []
    
    # for each weight in weights check if the limit - weight exists in the hash table
    for index in range(len(weights)):
        if hash_table_retrieve(ht, limit - weights[index]) != None:
            indices.append(index)

    # sort indices in reverse order
    indices.sort(reverse = True)

    # if the indices lenght is less than 2 then return None
    if len(indices) < 2:
        return None

    return tuple(indices)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
