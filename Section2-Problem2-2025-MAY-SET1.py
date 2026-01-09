m,n=map(int,input().split())
matrix=[
    list(map(int,input().split()))
    for i in range(m)
]

# classical way
# rotated = []
# for col in range(n):
#     new_row = []
#     for row in reversed(range(m)):
#         new_row.append(matrix[row][col])
#     rotated.append(new_row)

# using comprehensions
# rotated = [
#     [matrix[row][col] for row in range(m)][::-1]
#     for col in range(n)
# ]

# shortcut
rotated = [col[::-1] for col in zip(*matrix)]

for row in rotated:
    print(*row)

# #aNOTHER mETHOD:

# x,y=map(int,input().split())

# l=[]

# for i in range(x):
#     s=[]
#     a=input()
#     s=a.split()
#     l.append(s)
    
# matrix=[]

# for i in range(y):
#     subm=[]
#     for j in range(x-1,-1,-1):
#         a=l[j][i]
#         subm.append(a)
#     matrix.append(subm)

# for i in range(y):
#     print(*matrix[i])
    
# Rotate Matrix Clockwise 90 degree
# Write a program to rotate the matrix in 90 degree clockwise direction. The program should handle both square and non-square (rectangular) matrices.

# NOTE: This is an I/O type question, you need to write the whole code for taking input and printing the output.

# Input Format

# The first line contains the size of the matrix i.e) m x n.
# The next m lines each contain the element of the matrix.
# Output Format

# The output has to be n x m rotated matrix
# Example

# Input

# 3 3
# 1 2 3
# 4 5 6
# 7 8 9
# Output

# 7 4 1
# 8 5 2
# 9 6 3
# Explanation

# When you rotate a matrix 90 degrees clockwise, you are essentially transforming the matrix so that the columns of the original matrix become the rows of the rotated matrix, but in reverse order.
        
        
    
