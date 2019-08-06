

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"\nkey: {self.key}  value: {self.value}\n"


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

    def print_me(self):
        for i in self.storage:
            print(i)
            if i is not None and isinstance(i.next, LinkedPair):
                head = i
                while(head.next is not None):
                    print(head.next)
                    head = head.next


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash_value = 5381
    for i in list(bytes(string,encoding="UTF-8")):
        hash_value = (hash_value * 33) + i
    return hash_value % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key,hash_table.capacity)
    if hash_table.storage[index] is None:
        hash_table.storage[index] = LinkedPair(key,value)
    elif hash_table.storage[index].key == key:
        hash_table.storage[index].key, hash_table.storage[index].value = key, value
    else:
        next_LL = hash_table.storage[index]
        while(next_LL is not None):
            if next_LL.next is None:
                next_LL.next = LinkedPair(key,value)
                break
            elif next_LL.next.key == key:
                next_LL.next.key, next_LL.next.value = key, value
                break
            else:
                next_LL = next_LL.next
        
        


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key,hash_table.capacity)
    if hash_table.storage[index] is None:
        return None
    elif hash_table.storage[index].key == key and hash_table.storage[index].next is None:
        hash_table.storage[index] = None
    elif hash_table.storage[index].key == key and isinstance(hash_table.storage[index].next,LinkedPair):
        hash_table.storage[index] = hash_table.storage[index].next
    elif hash_table.storage[index].key != key and hash_table.storage[index].next is None:
        return None
    else:
        next_LL = hash_table.storage[index]
        while(next_LL.next is not None):
            if next_LL.next.key == key:
                next_LL.next = None
                break
            else:
                next_LL = next_LL.next
        return None
            




# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key,hash_table.capacity)
    if hash_table.storage[index] is None:
        return None
    elif hash_table.storage[index].key == key:
        return hash_table.storage[index].value
    elif hash_table.storage[index].key != key and hash_table.storage[index].next is None:
        return None
    else:
        next_LL = hash_table.storage[index]
        while(next_LL.next is not None):
            if next_LL.next.key == key:
                return next_LL.next.value
            else:
                next_LL = next_LL.next
        return None



# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    new_capacity = hash_table.capacity * 2
    temp_ht = HashTable(new_capacity)

    for i in hash_table.storage:
        if i is None:
            continue

        hash_table_insert(temp_ht, i.key, i.value)

        if i.next is not None:
            next_LL = i.next
            while(next_LL is not None):
                hash_table_insert(temp_ht, next_LL.key, next_LL.value)
                next_LL = next_LL.next

    return temp_ht


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")

    ht.print_me()
Testing()
