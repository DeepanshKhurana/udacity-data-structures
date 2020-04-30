def hamming_distance(str1, str2):

    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """
    
    if len(str1) == len(str2):
        distance = 0
        
        for idx in range(len(str1)):
            if str1[idx] != str2[idx]:
                distance += 1
            
        return distance
    
    return None