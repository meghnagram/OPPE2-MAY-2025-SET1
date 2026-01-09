import string 
# string.ascii_lowercase is a string with all lowercase alphabets.
# string.ascii_lowercase = 'abc...xyz'



def is_pangram(text: str) -> bool:
    '''
    Given a string, check if it is a pangram (contains all letters of the alphabet at least once).

    Examples:
    >>> is_pangram("the quick brown fox jumps over the lazy dog")
    True
    >>> is_pangram("this is not a pangram")
    False
    >>> is_pangram("abcdefghijklmnopqrstuvwxyz")
    True 
    >>> is_pangram("zyxwvutsrqponmlkjihgfedcba")
    True 

    Args:
        text (str): The input string

    Returns:
        bool: True if the string is a pangram, False otherwise
    '''
    
    
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(text.lower())


# #another Method:
# def is_pangram(text: str) -> bool:
   
#     letters='abcdefghijklmnopqrstuvwxyz'
    
#     for ch in letters:
#         if ch in text.lower():
#             c=0
#         else:
#             c=1
#             # print(ch)
#             break
#     if c==1:
#         return False
#     else:
#         return True

# Pangram Check
# Write a function is_pangram that takes a string text as input and returns True if the string is a pangram, False otherwise.

# A pangram is a sentence containing every letter of the alphabet at least once.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example

# >>> is_pangram("the quick brown fox jumps over the lazy dog")
# True
# >>> is_pangram("this is not a pangram")
# False
# >>> is_pangram("abcdefghijklmnopqrstuvwxyz")
# True 
# >>> is_pangram("zyxwvutsrqponmlkjihgfedcba")
# True 
        
