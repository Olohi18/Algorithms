# Name:  - Olohi John
# Peers:  - N/A
# References:  - URL of resources used <br>
import math # pyright: ignore[reportUnusedImport]
import time
import csv          # Used to read a .csv file.

# Next up: 
    # Fix bug in reHash function. See first line under "Questions"
    # Start the profiling part of the assignment
# Design decisions
    # array of hashtable contains ints and hashnodes. Ints to represent empty slots and hashnodes to represent occupied spots
# Questions
    # my reHash doesn't seem to update the hashtable on the outside
    # Am I allowed to add things to strings like string = "girl"; string += "boss" 

### DO NOT EDIT ###
def new_array(size: int):
    """ Creates a new array of a given size.
    :param size: (int) the number of 0s you want in the array
    :return : (list) the array with zeros 
    >>> new_array(3)
    [0,0,0]
    """
    L = [0] * size
    return L

class HashNode:
    """Class to instantiate linked list node objects, with both a key and a value.
    >>> node = HashNode(7, "Matt Damon")
    >>> print(node)
    {key:7, value:Matt Damon}
    """
    
    def __init__(self, key:int, value:str) -> None:
        """ Constructor of new node with a key and value. Initially nodes do not have a next value.
        :param key: (int) the key that will be added to the node
        :param value: (str) the value that will be added to the node
        :return : (HashNode) a pointer to the object
        """
        self.key = key
        self.value = value
        self.next: HashNode | None = None 
        
    def __str__(self) -> str:
        """ Returns a string representation of the object.
        :return : (str) a string description of the HashNode object.
        """
        return "{key:" + str(self.key) + ", value:" + self.value + "}"     
### END OF DO NOT EDIT###

# Hint: create a linked list class here...
class LinkedList:
    def __init__(self, head:HashNode) -> None:
        self.head = head # the head of the list
        self.length = 1 # keeps track of the length of the list
    def insert(self, prev:HashNode|None, to_add:HashNode) -> bool:
        """
        Inserts the node, to_add, to the linkedlist

        @param prev: (HashNode) the node after which to insert to_add
        @param to_add: (HashNode) the node to insert into the linked list

        >>> insert(Node(5), Node(6))
        True
        """
        # if prev is None, set to_add as the head of the linkedlist
        if prev is None:
            self.head = to_add
        # if prev, set insert to_add between prev and next
        else:
            to_add.next = prev.next
            prev.next = to_add
        self.length += 1
        return True
    
    def deleteNode(self, prev:HashNode) -> bool: #type: ignore override
        """
        Deletes the node after prev from the linked list

        @param prev: (HashNode) the node before the node to be removed from the linkedlist
        
        >>> delete(Node(5))
        True
        """
        if prev.next is None:
            return False
        prev.next = prev.next.next
        self.length -= 1
        return True
    
    def deleteKey(self, key:int) -> bool: #type: ignore override
        if self.head is None:
            return False
        elif self.head.key == key:
            self.head = self.head.next
            self.length -= 1
            return True
        else:
            prev = self.search(key)
            if prev is None:
                return False
            else:
                return self.deleteNode(prev)

        

    
    def search(self, key:int) -> HashNode | None: #type: ignore override
        """
        Returns the previous of the first node with key, key, in the linkedlist
    
        @param value: (int) the key whose node is to be found in the linkedlist

        >>> linkedlist = node1(1, node(2, node(3, node(2))))
        >>> linkedlist.search(3)
        node(2, node(3, node(2))) 
        """
        current:HashNode|None = self.head
        while current and current.next:
            if current.next.key == key:
                return current
            current = current.next
        return None
    
    def search(self, index:int) -> HashNode | None: #type: ignore override
        """
        Returns the node at index, index, in the linkedlist or None if it doesn't exist

        @param index: (int) the position of the hashnode to be found in the linkedlist

         >>> linkedlist = node1(1, node(2, node(3, node(2))))
        >>> linkedlist.search(2)
        node(3, node(2))
        """
        
        count:int = 0
        current:HashNode|None = self.head
        while count <= index and current:
            if count == index:
                return current
            current = current.next
            count += 1
        return None
    


class HashTable:
    
    def __init__(self, size:int, hash_choice:int) -> None:
        """
        Constructor to initialize a new hash table

        @param size: (int) number of entries in the hashtable
        @param hash_choice: (int) determines the hash function to be applied
        """
        self.size:int = size
        self.hash_choice:int = hash_choice                  # Which hash function you will use.
        #TODO Finish constructor...
        self.arrayHash: list[int | HashNode] = [0] * self.size # unoccupied areas are represent with ints. Occupied slots with Hashnodes
        self.occupied:int = 0
        pass
    
    def __str__(self) -> str:
        """
        Prints out the contents of the hashtable
        """
        string: str = (f"Hashmap:\n") + "{" 
        number_printed: int = 0
        array_index: int = 0
        while number_printed <= self.occupied and array_index < self.size:
            if self.arrayHash[array_index] != 0:
                current = self.arrayHash[array_index]
                while current:
                    string += (f"{current.key}: {current.value},\n") # how do I tell pylance that I'm sure that current is a node
                    current = current.next
                    number_printed += 1
            array_index += 1
        return string + "}\n"
        
    def hashFunc(self, key:int) -> int|None:
        if type(key) != int:
            return None
        if self.hash_choice == 0:
            return hash(key) % self.size    #Embedded Python hash function.
        elif self.hash_choice == 1:
            return 0    #Everything in the has ia stored in a single linked list.
        elif self.hash_choice == 2:
            # simple: get key mod hashsize
            if key < 0:
                return -key % self.size
            else:
                return key % self.size
        elif self.hash_choice == 3:
            # slightly more complex: multiply by 0 < constant < 1
            constant:float = 0.8
            if key < 0:
                index:int = int((-key) * constant)
            else:
                index = int(key * constant)
            if index < self.size:
                return index
            else:
                return index % self.size
        elif self.hash_choice == 4:
            # do research on an SHA function if time allows. If not, put another simple one
            pass
        return None
    
    def insert(self, key:int, val:str) -> bool: 
        # Might need to check that space isn't above profiling limit
        """
        Inserts a new key,value pair to the existing hash table

        @param key: (int) the key to be inserted into the hashtable
        @param val: (str) the value of the key to be inserted into the hashtable
        >>> ll = new LinkedList()
        >>> ll.insert(5, "apple")
        True
        """
        if self.isOverLoadFactor():
            self.reHash()
        if self.hashFunc(key) is not None: 
            index:int = self.hashFunc(key) #type: ignore
            new_node:HashNode = HashNode(key, val)
            if self.arrayHash[index] == 0:
                self.occupied += 1
                self.arrayHash[index] = new_node
                return True
            else:
                self.occupied += 1
                current:HashNode = self.arrayHash[index] #type: ignore because self.arrayHash[index] must be a HashNode at this point
                if current.key == key:
                        current.value = val
                        return True
                while current.next:
                    if current.key == key:
                        current.value = val
                        return True
                    current = current.next
                current.next = new_node
                return True
        return False
    
    def insertNode(self, new_node:HashNode) -> bool:
        # Might need to check that space isn't above profiling limit
        """
        Inserts a new key,value pair to the existing hash table

        @param key: (int) the key to be inserted into the hashtable
        @param val: (str) the value of the key to be inserted into the hashtable
        >>> ll = new LinkedList()
        >>> ll.insert(5, "apple")
        True
        """
        if self.isOverLoadFactor():
            print(f"entered rehASH")
            self.reHash()
        if self.contains(new_node.key) is True: # implement a search function 
            return False
        if self.hashFunc(new_node.key) is not None: 
            index:int = self.hashFunc(new_node.key) #type: ignore
            if self.arrayHash[index] == 0:
                self.occupied += 1
                self.arrayHash[index] = new_node
                return True
            else:
                self.occupied += 1
                current:HashNode = self.arrayHash[index] #type: ignore because self.arrayHash[index] must be a HashNode at this point
                while current.next:
                    current = current.next
                current.next = new_node
                return True
        return False

    def getValue(self, key:int) -> str|None:
        """
        Returns the value associated with a key in the hashtable

        @param key: (int) the key whose value is to be found 
        @return val: (str) the value associated with key or None if key is not in hashtable

        >>> ll = new LinkedList()
        >>> ll.insert(5, "apple")
        >>> ll.getValue(5)
        "apple"
        """
        index: int = self.hashFunc(key) #type: ignore
        if self.arrayHash[index] == 0:
            return None
        else:
            current = self.arrayHash[index]
            while current:
                if current.key == key:
                    return current.value
                current = current.next
            return None

    def remove(self, key:int) -> bool:
        """
        Removes an entry from the hashtable and returns True or False depending on whether the operation was successful

        @param key: (int) the key to be removed from the linkedlist

        >>> ll = new LinkedList()
        >>> ll.insert(5, "apple")
        >>> ll.remove(5, "apple)
        True
        """
        index: int = self.hashFunc(key) #type: ignore
        current:HashNode|int = self.arrayHash[index]
        if type(current) is HashNode:
            # Node to be removed is the head and has no nexts
            if current.key == key and current.next is None:
                self.arrayHash[index] = 0
                self.occupied -= 1
                return True
            # Node to be removed is the head and has a next
            elif current.key == key and current.next is not None:
                self.arrayHash[index] = current.next
                self.occupied -= 1
                return True
            # Node to be removed is not the head
            while current.next:
                if current.next.key == key:
                    current.next = current.next.next
                    self.occupied -= 1
                    return True
                current = current.next
            return False
        # index returned by hash is empty (stores an int), so return 0
        else:
            return False
        
    
    def isOverLoadFactor(self) -> bool:
        """
        Returns true if the load factor for the hashtable >= 0.7
        
        >>> ll.isOverLoadFactor()
        True
        """
        load:float = self.occupied/self.size
        return load >= 0.7
    
    def reHash(self) -> bool:
        """
        Rehashes all of the key,value pairs onto a new hash table
        """
        
        prev_array = self.arrayHash
        new_table = HashTable(self.size*2, self.hash_choice)
        self = new_table
        self.size = new_table.size
        self.hash_choice = new_table.hash_choice
        # iterate through current hashtable array
        for i in range(len(prev_array)):
            # iterate through the linkedlists of every element and add them to new_array based on a rehash
            if prev_array[i] == 0:
                continue
            else:
                current:HashNode = prev_array[i]
                while current:
                    self.insertNode(current) 
                    current = current.next
        # print(f"current length is {self.size} which is  > than previous size of {len(prev_array)}")
        return True

        # reset self.arrayHash to new_array and update self.size
        # self.occupied and self.hashchoice should remain the same
    
    def contains(self, key:int):
        for current in self.arrayHash:
            if current == 0:
                continue
            else:
                while current:
                    if current.key == key: # current is a Node so ignore type error
                        return True
                    current = current.next
        return False

def testMain() -> None:            
    # Use this function to test your code as you develop, especially your singly-linked list. 
    # Review, but do not use, profileMain or releaseMain until you are well into development.
    hash_choice:int = 0    
    initial_bucket_size:int = 10 
    test_map:HashTable = HashTable(initial_bucket_size, hash_choice)

    # Test for insert-- when hash function initialized, insert should call rehash within
    print(f"Result of insert is {test_map.insert(5, "apple")}")
    print(f"Result of insert is {test_map.insert(1, "mango")}")
    print(f"Result of insert is {test_map.insert(2, "fish")}")
    print(f"Result of insert is {test_map.insert(2, "girl")}") # should update value associated with 2 to girl
    print(f"Result of insert is {test_map.insert(2000000000000000000000, "girl")}")
    print(f"Result of insert is {test_map.insert(2, "girl")}")
    print(f"Result of insert is {test_map.insert(8, "girl")}")
    print()
    print(f"Result of insertNode is {test_map.insertNode(HashNode(7, "milk"))}")
    print()
    print(f"hashmap contains {0}: {test_map.contains(0)}")
    print(test_map)

    # # Test for getValue
    # print(test_map.getValue(2)) # girl
    # print(test_map.getValue(89)) # None
    # print()

    # # Test for remove
    # print(test_map.remove(5)) # True
    # print(test_map.remove(5)) # False
    # print()

    # Test for isOverLoadFactor() -- retest after creating your hash functions
    print(f"length of hash is {test_map.size} and there are {test_map.occupied} occupied slots\n")
    print(test_map.isOverLoadFactor()) # True
    print(f"Result of insert is {test_map.insert(9, "boy")}")
    print(f"Result of insert is {test_map.insert(10, "boy")}")
    print(f"Result of insert is {test_map.insert(11, "boy")}")
    print(f"Result of insert is {test_map.insert(12, "boy")}")
    print()
    print(f"length of hash is {test_map.size} and there are {test_map.occupied} occupied slots\n") # problem: test_map doesn't seem updated
    print(test_map.isOverLoadFactor()) # True
    print()
    print(test_map)


def releaseMain() -> None:
    # You should update these three values as you test your implementation.
    hash_to_test = 0    
    initial_bucket_size = 10 
    initial_num_to_add = 100

    hash_table = HashTable(initial_bucket_size, hash_to_test)
    with open('hwk4-people.csv') as csv_file:    
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = csv_reader.__next__() # pyright: ignore[reportUnusedVariable]
        for row_iterator in range(initial_num_to_add): # pyright: ignore[reportUnusedVariable]
            row = csv_reader.__next__()
            hash_table.insert(int(row[0]),row[1])
        print("Hash Map Initialized")
                
        option = ""
        while option != "QUIT":
            option = input("Select an option (ADD, GET, REMOVE, PRINT, CHECK, REHASH, QUIT): ").upper()        

            if option == "ADD":
                row = csv_reader.__next__()
                hash_table.insert(int(row[0]),row[1])
                print("Added - Key:", int(row[0]), "\tValue:", row[1])
            elif option == "GET":
                key = int(input("Which # would you like to get the value of? "))
                val = hash_table.getValue(key)
                if val is None:
                    print("Error,", key, "not found.")
                else:
                    print(val)
            elif option == "REMOVE":
                key = int(input("Which # would you like to remove? "))
                suc = hash_table.remove(key)
                if suc:
                    print(key, "was removed.")
                else:
                    print("Error,", key, "was not removed.")                    
            elif option == "PRINT":
                print(hash_table)   # calls the __str__ method.  
            elif option == "CHECK":
                isOver = hash_table.isOverLoadFactor()
                if isOver:
                    print("Your load factor is over 0.7, it's time to rehash.")
                else:
                    print("Load factor is ok.")
            elif option == "REHASH":
                suc = hash_table.reHash()
                if suc:
                    print("Rehash was successful.")
                else:
                    print("ERROR: rehash failed.")
            elif option == "QUIT" or option == "Q":
                break 
            else:
                print("Error: invalid input, please try again.")
                
        print("Goodbye!")
            

def profilerMain() -> None:    
    # You should update these three values as you profile your implementation.
    num_hash_implemented = 2    
    initial_bucket_size = 10 
    initial_num_to_add = 100

    for i in range(0, num_hash_implemented):        
        hash_table = HashTable(initial_bucket_size, i)
        with open('hwk4-people.csv') as csv_file:    
            csv_reader = csv.reader(csv_file, delimiter=',')
            header = csv_reader.__next__()  # pyright: ignore[reportUnusedVariable]
            for row_iterator in range(initial_num_to_add): # pyright: ignore[reportUnusedVariable]
                row = csv_reader.__next__()
                hash_table.insert(int(row[0]),row[1])
            print("Hash Map", i, "Initialized")
            start_time_create = time.time()    # Get start Time.
            #### Start of code you want to profile ####
            
            # Add/Edit code to profile
            row = csv_reader.__next__() 
            hash_table.insert(int(row[0]),row[1])
            
            #### End of code you want to profile ####
            end_time_create = time.time()      # Get end Time. 
            calc = end_time_create - start_time_create  
            print("Hash Map", i, "Test \tTime:", calc, "seconds.")
        
    

if __name__ == "__main__":
    # Swap these options to profile or test your code.
    testMain()
    #profilerMain()     
    #releaseMain()
    
