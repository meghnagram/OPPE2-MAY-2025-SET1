with open(filename) as f:
    z = int(f.readline())

    spaces = 0
    direction = 1

    for line in f:
        ch = line.rstrip("\n")          
        print(" " * spaces + ch)  

        if z > 1:
            if spaces == z - 1:
                direction = -1
            elif spaces == 0:
                direction = 1
            spaces += direction

# #aNOTHER mETHOD:

# # Read the file using the variable filename, and print the result in the output.


# with open(filename,'r') as file:
#     ch=file.readline()
#     num=int(ch.rstrip())
#     space = 0
#     inc=1
    
#     line=file.readline()
#     while (line):
#         if num==1:
#             space=0
#         print(' '*space+line,end='')
#         if inc==1:
#             space=space+1
#         else:
#             space=space-1
            
#         if space == num-1:
#             inc=0
#         if space== 0:
#             inc=1
#         line=file.readline()
            
#   File Content Zig-Zag Shift
# A file is given where the first line contains a positive integer z the size of the zigzag.
# Each of the following lines contains exactly one character

# Print the characters in the same order, but prepend each line with a number of leading spaces that follows a zigzag pattern of width z:

# start with 0 spaces,
# increase the number of spaces by 1 each line until z1 spaces are reached,
# then decrease the number of spaces by 1 each line until 0 spaces are reached,
# repeat the upanddown cycle for the whole file.
# If z = 1 the pattern is always 0 spaces.

# Input format (file)

# z
# c1
# c2
# c3
# ...
# z integer, z 1.
# ci a single character (the line may contain trailing newline only).
# Output format

# For every character line ci output a line consisting of the required number of leading spaces followed by ci.
# Do not add spaces after the character.

# Examples

# Input:

# 3
# a
# p
# p
# l
# e
# o
# r
# a
# n
# g
# e
# Output:

# a
#  p
#   p
#  l
# e
#  o
#   r
#  a
# n
#  g
#   e
# Input:

# 2
# a
# p
# p
# l
# e
# o
# r
# a
# n
# g
# e
# Output:

# a
#  p
# p
#  l
# e
#  o
# r
#  a
# n
#  g
# e
# Input:

# 7
# a
# p
# p
# l
# e
# o
# r
# a
# n
# g
# e
# Output:

# a
#  p
#   p
#    l
#     e
#      o
#       r
#      a
#     n
#    g
#   e     


