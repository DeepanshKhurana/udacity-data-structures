'''
You have been given an array containg numbers.
Find and return the largest sum in a contiguous subarray within the input array.

arr= [1, 2, 3, -4, 6] #8 (Entire Array)

arr = [1, 2, -5, -4, 1, 6] #7 (Last Two Elements)

'''

def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    
    current_sum = arr[0]
    max_sum = arr[0]
    
    for item in arr[1:]:
        
        current_sum = max(current_sum + item, item)
        max_sum = max(current_sum, max_sum)
        
    return(max_sum)
