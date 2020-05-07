'''
Given a linked list, swap the two nodes present at position i and j,
assuming 0 <= i <= j.
The positions are based on 0-based indexing.

linked_list = 3 4 5 2 6 1 9
positions = 2 5
output = 3 4 1 2 6 5 9

'''



"""
:param: head- head of input linked list
:param: `position_one` - indicates position (index) ONE
:param: `position_two` - indicates position (index) TWO
return: head of updated linked list with nodes swapped

TODO: complete this function and swap nodes present at position_one and position_two
Do not create a new linked list
"""
def swap_nodes(head, left_index, right_index):
    
    if left_index == right_index:
        return head
    
    one_previous = None
    one_current = None

    two_previous = None
    two_current = None
    
    current = head
    index = 0
    new = None
    
    while current:
        
        if index == left_index:
            one_current = current
            
        elif index == right_index:
            two_current = current
            break
            
        if one_current is None:
            one_previous = current
            
        two_previous = current
        
        current = current.next
        index += 1
        
        
    two_previous.next = one_current
    temp = one_current.next
    one_current.next = two_current.next
    two_current.next = temp
    
    # if the node at first index is head of the original linked list
    if one_previous is None:
        new = two_current
    else:
        one_previous.next = two_current
        new = head
    
    return new