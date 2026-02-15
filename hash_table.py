class Contact:
    
    # Contact class to represent a contact with a name and number.

    
    def __init__(self, name: str, number: str): # contact class
        #initializing a Contact with a name and phone number
        self.name = name
        self.number = number

    def __str__(self) -> str:
        #returns the contact in the format '[NAME]: [NUMBER]'
        return f"{self.name}: {self.number}"

class Node: # node class
    
    # Node class to represent a single entry in the hash table.


    def __init__(self, key: str, value: 'Contact', next=None):
        # initialize a Node for separate chaining.

        # attributes:
        self.key = key
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.key!r})"

class HashTable:
    
    # HashTable class to represent a hash table for storing contacts.

    def __init__(self, size: int = 10):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key: str) -> int:
        # Convert a string key into an array index.
        return sum(ord(ch) for ch in key) % self.size

    def insert(self, key: str, number: str):
        
        # Insert or update a contact.
        contact = Contact(key, number)
        idx = self.hash_function(key)

        head = self.data[idx]
        # if bucket empty -> place new node
        if head is None:
            self.data[idx] = Node(key, contact)
            return

        # traverse to find existing key; update if found
        curr = head
        while curr:
            if curr.key == key:
                curr.value = contact
                return
            curr = curr.next

        # not found -> insert new node at head
        new_node = Node(key, contact, head)
        self.data[idx] = new_node

    def search(self, key: str):
        # Return the Contact for `key`, or None if not found.
        idx = self.hash_function(key)
        curr = self.data[idx]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return None

    def print_table(self):
        # Print the table showing contacts at each index.
        for i, node in enumerate(self.data):
            print(f"{i}:", end=" ")
            if not node:
                print("None")
                continue
            parts = []
            curr = node
            while curr:
                parts.append(str(curr.value))
                curr = curr.next
            print(" -> ".join(parts))

# Test your hash table implementation here.
if __name__ == "__main__":
    ht = HashTable(5)

    print("Inserting contacts...")
    ht.insert("Alice", "123-456-7890")
    ht.insert("Bob", "234-567-8901")
    ht.insert("Charlie", "345-678-9012")
    ht.insert("Diana", "456-789-0123")
    ht.insert("Eve", "567-890-1234")

    # update existing (duplicate-name update)
    ht.insert("Alice", "999-999-9999")

    print("\nSearch results:")
    print("Alice ->", ht.search("Alice"))
    print("Zoe   ->", ht.search("Zoe"))

    # Edge case: force a collision
    alice_idx = ht.hash_function("Alice")
    colliding_name = None
    for i in range(1000):
        candidate = f"Name{i}"
        if candidate == "Alice":
            continue
        if ht.hash_function(candidate) == alice_idx:
            colliding_name = candidate
            break
    assert colliding_name is not None, "Failed to find a colliding name"

    print(f"\nFound colliding name '{colliding_name}' that maps to index {alice_idx}. Inserting it...")
    ht.insert(colliding_name, "111-222-3333")

    # bucket contents for the collided index
    print(f"\nBucket {alice_idx} contents after collision:")
    curr = ht.data[alice_idx]
    while curr:
        print(" -", curr.value)
        curr = curr.next

    # Edge case: inserting a value with the same name
    ht.insert("Bob", "000-000-0000")
    print("\nAfter updating Bob's number:")
    print("Bob ->", ht.search("Bob"))

    # verify behavior
    assert ht.search("Alice").number == "999-999-9999"
    assert ht.search(colliding_name) is not None and ht.search(colliding_name).number == "111-222-3333"
    assert ht.search("Bob").number == "000-000-0000"

    print("\nFull table:")
    ht.print_table()

    print("\nAll edge-case tests passed")

# A hash table is appropriate for fast lookups because it maps keys to array indices using a hash function, enabling average‑case constant‑time access for search, insert, and delete operations.
# Unlike a list or a balanced tree, a hash table avoids scanning elements lookups. Performance depends on a good hash function and a reasonable load factor.

# I went with separate chaining: each bucket is just the start of a singly linked list of Node objects that hold the contacts.
# When inserting, the code scans the list to update an existing entry or attaches a new node if the key isn’t there. Lookups work by walking that same chain until they find a matching name.
# Separate chaining is simple, handles collisions gracefully, and works well even when the table gets fairly full. Other approaches—like open addressing or using balanced trees instead of linked lists—can offer better worst‑case guarantees.

# If you need quick lookups, inserts, or deletes and you don’t care about keeping things sorted, a hash table is usually the right choice. That’s why they’re used in dictionaries, caches, and symbol tables.
# Reach for a list when the dataset is tiny or mostly accessed in sequence. Choose a balanced tree if you need sorted order, expect to perform range queries, or want reliable worst‑case performance.
# In short, hash tables are fast on average, while trees give you order and predictable performance.