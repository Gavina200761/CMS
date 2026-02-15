class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name: str, number: str): # contact class
        #initializing a Contact with a name and phone number
        self.name = name
        self.number = number

    def __str__(self) -> str:
        #returns the contact in the format '[NAME]: [NUMBER]'
        return f"{self.name}: {self.number}"

class Node: # node class
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''

    def __init__(self, key: str, value: 'Contact', next=None):
        # initialize a Node for separate chaining.

        # attributes:
        self.key = key
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.key!r})"

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    pass # Delete this line when implementing the class

# Test your hash table implementation here.  