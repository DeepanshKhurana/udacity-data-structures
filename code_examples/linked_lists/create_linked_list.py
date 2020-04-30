def create_linked_list(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    head = None

    for item in input_list:
        if head is None:
            head = Node(item)
        else:
            pos = head
            while pos.next:
                pos = pos.next
            pos.next = Node(item)
    
    return head