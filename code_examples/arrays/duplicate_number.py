'''
You have been given an array of length = n.
The array contains integers from 0 to n - 2.
Each number in the array is present exactly once except for one number which is present twice.
Find and return this duplicate number present in the array
'''

def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    sum_1 = 0
    sum_2 = 0
    for element in arr:
        sum_1 += element
    for number in range(0, len(arr) - 1, 1):
        sum_2 += number
        
    return(sum_1-sum_2)