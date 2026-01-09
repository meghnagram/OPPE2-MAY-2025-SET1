def is_arithmetic_progression(sequence: list) -> bool:
    '''
    Given a sequence of numbers, determine if it is an arithmetic progression.

    An arithmetic progression is a sequence where the difference between consecutive terms is constant.

    Examples:
    is_arithmetic_progression([1, 3, 5, 7, 9])
    >>> True
    is_arithmetic_progression([2, 4, 6, 8, 10])
    >>> True
    is_arithmetic_progression([9, 6, 3, 0, -3, -6])
    >>> True
    is_arithmetic_progression([1, 3, 5, 6, 11])
    >>> False
    is_arithmetic_progression([0, 0, 0, 0, 0])
    >>> True
    is_arithmetic_progression([1, 2, 4, 8, 16])
    >>> False

    Args:
        sequence (list): A list of numbers

    Returns:
        bool: True if the sequence is an arithmetic progression, False otherwise
    '''
    
    
    if len(sequence) <= 2:
        return True
    diff = sequence[1] - sequence[0]

    # procedural way
    for i in range(len(sequence)-1):
        if sequence[i+1] - sequence[i] != diff:
            return False
    return True

    # using comprehensions
    return all(sequence[i+1]-sequence[i] == diff for i in range(len(sequence)-1))

# #Another METHOD:

# def is_arithmetic_progression(sequence: list) -> bool:
   
#     diff=sequence[0]-sequence[1]
#     for i in range(len(sequence)-1):
#         if sequence[i]-sequence[i+1]!=diff:
#             return False
#     return True
    
#      Check for Arithmetic Progression
# Write a function is_arithmetic_progression(sequence) that takes a sequence of numbers as input and returns True if the sequence is an arithmetic progression, and False otherwise.

# An arithmetic progression is a sequence where the difference between consecutive terms is constant.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example

# is_arithmetic_progression([1, 3, 5, 7, 9])
# >>> True
# is_arithmetic_progression([2, 4, 6, 8, 10])
# >>> True
# is_arithmetic_progression([9, 6, 3, 0, -3, -6])
# >>> True
# is_arithmetic_progression([1, 3, 5, 6, 11])
# >>> False
# is_arithmetic_progression([0, 0, 0, 0, 0])
# >>> True
# is_arithmetic_progression([1, 2, 4, 8, 16])
# >>> False   
        
    

    
