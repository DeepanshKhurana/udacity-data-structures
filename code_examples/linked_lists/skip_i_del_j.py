# You are given the head of a linked list and two integers, i and j.
# You have to retain the first i nodes and then delete the next j nodes. 
# ontinue doing so until the end of the linked list.
# Example:
# linked-list = 1 2 3 4 5 6 7 8 9 10 11 12
# i = 2
# j = 3
# Output = 1 2 6 7 11 12

def skip_i_delete_j(head, i, j):
    """
    :param: head - head of linked list
    :param: i - first `i` nodes that are to be skipped
    :param: j - next `j` nodes that are to be deleted
    return - return the updated head of the linked list
    """
    
    if i == 0:
        return None
    
    if j == 0:
        return head
    
    if head is None or j < 0 or i < 0:
        return head
    
    current = head
    previous = None
    
    while current:
        
        for x in range(i-1):
            if current is None:
                return head
            current = current.next
        previous = current
        current = current.next
        
        for y in range(j):
            if current is None:
                break
            next_node = current.next
            current = next_node
            
        previous.next = current
        
    return head
    