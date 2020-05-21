# Code

def factorial(n):
    """
    Calculate n!
    
    Args:
       n(int): factorial to be computed
    Returns:
       n!
    """
    
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
    pass