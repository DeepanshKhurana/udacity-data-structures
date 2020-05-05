def iscircular(linked_list):
    """
    Determine whether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """
    
    if linked_list.head is None:
        return False
    
    node_1 = linked_list.head
    node_2 = linked_list.head

    while node_2 and node_2.next:
        
        node_1 = node_1.next
        node_2 = node_2.next.next
        
        if node_1.value == node_2.value:
            return True

    return False