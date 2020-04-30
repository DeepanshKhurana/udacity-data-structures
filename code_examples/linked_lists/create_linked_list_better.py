def create_linked_list_better(input_list):
    
    head = None
    tail = None
    
    for item in input_list:
        if head is None:
            head = Node(item)
            tail = head
        else:
            tail.next = Node(item)
            tail = tail.next
    return head