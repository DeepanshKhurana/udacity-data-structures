def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    
    carry = 1
    
    for idx in range(len(arr), 0, -1):
        
        digit = carry + arr[idx - 1]
        
        carry = digit//10
        
        if carry == 0:
            arr[idx-1] = digit
            break
        else: arr[idx-1] = digit % 10
            
    arr = [carry] + arr
    
    pos = 0
    while arr[pos] == 0:
        pos+=1
        
    return(arr[pos:])