

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash_value = 5381
    for i in list(bytes(string, encoding='utf-8')):
        hash_value = (hash_value * 33) + i
    return hash_value % max


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    index_value = hash(key,hash_table.capacity)
    if(hash_table.storage[index_value] is not None and hash_table.storage[index_value].key != key):
        print("overwriting a value with a different key")
    hash_table.storage[index_value] = Pair(key,value)


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index_value = hash(key,hash_table.capacity)
    if(hash_table.storage[index_value] is None):
        print("overwriting a value with a different key")
    else:
        hash_table.storage[index_value] = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index_value = hash(key,hash_table.capacity)
    if(hash_table.storage[index_value] is None):
        return None
    else:
        return hash_table.storage[index_value].value


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
