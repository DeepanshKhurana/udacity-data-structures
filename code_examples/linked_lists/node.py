class Node():
    def __init__(self, num):
        self.value = num
        self.next = None
        
head = Node(2)
head.next = Node(1)
head.next.next = Node(4)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)

def traversal(head):
    pos = head
    
    while pos is not None:
        print(pos.value)
        pos = pos.next
        
traversal(head)