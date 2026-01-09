def is_reverse_combined_palindrome(s1: str, s2: str) -> str:
    '''
    Given two strings, 
    - Reverses the first string
    - Concatenates it with the second string
    - Checks if the result is a palindrome or not

    Examples:
    >>> is_reverse_combined_palindrome("mad", "am")
    False
    >>> is_reverse_combined_palindrome("dam", "am")
    True

    Args:
        s1 (string): The first string
        s2 (string): The second string

    Returns:
        str : check the palindrome or not
    '''
    
    
    combined = s1[::-1] + s2
    return combined == combined[::-1]
    
# #Another Method:
# def is_reverse_combined_palindrome(s1: str, s2: str) -> str:
  
    
#     str1=s1[::-1]
#     #print(str1)
#     str2=str1+s2
#     #print(str2)
#     if str2==str2[::-1]:
#         return True
#     else:
#         return False
    
# is_reverse_combined_palindrome
# Write a function that takes two strings, reverses the first string, concatenates it with the second string, and then check whether the concatenated string is palindrome or not.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example
# is_reverse_combined_palindrome("mad", "am") -> False
# is_reverse_combined_palindrome("dam", "am") -> True
