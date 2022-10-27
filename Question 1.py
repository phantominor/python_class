# Hollow diamond

# Print a hollow diamond with double * boundary.
# Example
# >>> hollow_diamond(7)
#       *
#      ***
#     ** **
#    **   **
#   **     **
#  **       **
# **         **
#  **       **
#   **     **
#    **   **
#     ** **
#      ***
#       *

"""Solution"""

def hollow_diamond(n):
    for i in range(2*n-1):
        i = i if i<n else 2*n-2-i
        if i == 0:
            print(" "*(n-1)+"*"+" "*(n-1))
        elif i == 1:
            print(" "*(n-2)+"***"+" "*(n-2))
        else:
            print(" "*(n-1-i)+"**"+ " "*(2*i-3)+"**"+" "*(n-1-i))

def hollow_diamond_2(n):
    for row in range(1, 2*n):
        if row <=2 or row >= 2*n-2:
            print(' '*(max(n-row,row-n)) + '*'*(2*min(row,2*n-row)-1) + ' '*(max(n-row,row-n)-1))
        else:
            print(' '*(max(n-row,row-n)) + '**' + ' '*(2*min(row,2*n-row)-5) + '**' + ' '*(max(n-row,row-n)-1))

hollow_diamond_2(3)

