# Define Node class

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Define Linked List

class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

# Define Prepend

def prepend(self, value):
    """ Prepend a value to the beginning of the list. """
    # TODO: Write function to prepend here
    if self.head is None:
        self.head = Node(value)
        return
    
    new_head = Node(value)
    new_head.next = self.head
    self.head = new_head
        

LinkedList.prepend = prepend

# Define Append

def append(self, value):
    """ Append a value to the end of the list. """    
    
    if self.head is None:
        self.head = Node(value)
        return
    
    node = self.head
    last_node = Node(0)
    
    while node:
        last_node = node
        node = node.next
        
    last_node.next = Node(value)
    

LinkedList.append = append

# Define Search

def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    # TODO: Write function to search here
    
    if self.head is None:
        return
    
    node = self.head
    
    while node:
        if node.value == value:
            return node
        node = node.next

    raise ValueError("Value not found!")
    
LinkedList.search = search

# Define Remove

def remove(self, value):
    """ Remove first occurrence of value. """
    # TODO: Write function to remove here
    
    if self.head is None:
        return
    
    if self.head.value == value:
        self.head = self.head.next
        return
    
    node = self.head
    
    while node.next:
        if node.next.value == value:
            node.next = node.next.next
            return
        node = node.next
        
    raise ValueError("Value not found!")

LinkedList.remove = remove

# Define Pop

def pop(self):
    """ Return the first node's value and remove it from the list. """
    # TODO: Write function to pop here
    
    if self.head is None:
        return
    
    x = self.head.value
    self.remove(x)
    return x

LinkedList.pop = pop

# Define Insert

def insert(self, value, pos):
    """ Insert value at pos position in the list. If pos is larger than the
    length of the list, append to the end of the list. """
        
    # TODO: Write function to insert here    
    
    if self.head is None:
        return
    
    node = self.head
    length = len(self.to_list())
    
    if pos == 0:
        self.prepend(value)
        return
    
    elif pos >= (length-1):
        self.append(value)
        return
        
    else:
        idx = 0
        
        while node:
            if pos == idx+1:    
                new_node = Node(value)
                new_node.next = node.next
                node.next = new_node
                return
            
            else:
                node = node.next
                idx += 1

LinkedList.insert = insert

# Define Size

def size(self):
    """ Return the size or length of the linked list. """
    # TODO: Write function to get size here
    
    return(len(self.to_list()))

LinkedList.size = size

# Asserts

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"

# Test append - 1
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

# Test append - 2
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# Test insert 
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# Test size function
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"

