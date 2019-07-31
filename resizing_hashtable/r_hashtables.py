

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.key + ': ' + self.value)


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * capacity

    def __repr__(self):
        return str(self.storage)


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for s in string:
        hash = (hash * 33) + ord(s)
    return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    # if hash_table.count/hash_table.capacity > 0.5:
    #     hash_table_resize(hash_table)

    index = hash(key, hash_table.capacity)
    current_pair = hash_table.storage[index]
   
    while current_pair is not None and current_pair.key != key:
        current_pair = current_pair.next

    if current_pair is None:
        new_pair = LinkedPair(key, value)
        new_pair.next = hash_table.storage[index]
        hash_table.storage[index] = new_pair
        hash_table.count += 1
    else:
        current_pair.value = value


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    current_pair = hash_table.storage[index]
    prev_pair = None

    if current_pair is not None:
        while current_pair is not None and current_pair.key != key:
            prev_pair = current_pair
            current_pair = current_pair.next

        if prev_pair is None and current_pair.key == key:
            hash_table.storage[index] = None
            hash_table.count -= 1
        
        elif current_pair is None:
            print('could not find that key')
        else:
            prev_pair.next = None
    else:
        print('could not find that key')


 
  


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    current_pair = hash_table.storage[index]

    if hash_table.storage[index] == None:
       return print('There is no value at index ' + str(index))

    if current_pair.key != key:
        while current_pair.key != key:
            current_pair = current_pair.next

    if current_pair.key == key:
        return current_pair.value
    else:
        return print('could not find that key/value')



# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    new_table = HashTable(hash_table.capacity * 2)
    temp_array = []

    for pair in hash_table.storage:
        if pair is not None:
            if pair.next == None:
                temp_array.append(pair)
            else:
                current_pair = pair
                temp_array.append(current_pair)
                while current_pair.next is not None:
                    temp_array.append(current_pair.next)
                    current_pair = current_pair.next

    for pair in temp_array:
        hash_table_insert(new_table, pair.key, pair.value)

    return new_table




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


# Testing()
ht = HashTable(8)

hash_table_insert(ht, "key-0", "val-0")
hash_table_insert(ht, "key-1", "val-1")
hash_table_insert(ht, "key-2", "val-2")
hash_table_insert(ht, "key-3", "val-3")
hash_table_insert(ht, "key-4", "val-4")
hash_table_insert(ht, "key-5", "val-5")
hash_table_insert(ht, "key-6", "val-6")
hash_table_insert(ht, "key-7", "val-7")
hash_table_insert(ht, "key-8", "val-8")
hash_table_insert(ht, "key-9", "val-9")



ht = hash_table_resize(ht)
print(ht)
# print(hash_table_retrieve(ht, "key-0"))




