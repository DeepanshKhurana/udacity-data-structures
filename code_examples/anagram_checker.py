def anagram_checker(str1, str2):

    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    
    if len(str1) == len(str2):
        if sorted(str1) == sorted(str2):
            return True
    
    return False