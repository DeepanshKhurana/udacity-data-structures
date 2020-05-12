# Our Stack Class - Brought from previous concept
# No need to modify this
class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
    
    
    stack = Stack()
    
    for char in equation:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.pop() == None:
                return False
    
    if stack.size() == 0:
        return True
    else: return False
        
    # TODO: Interate through equation checking parentheses
    
    # TODO: Return True if balanced and False if not
    
    