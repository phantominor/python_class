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

def hollow_diamond(n):
    for row in range(1, 2*n):
        if row <=2 or row >= 2*n-2:
            print(' '*(max(n-row,row-n)) + '*'*(2*min(row,2*n-row)-1) + ' '*(max(n-row,row-n)-1))
        else:
            print(' '*(max(n-row,row-n)) + '**' + ' '*(2*min(row,2*n-row)-5) + '**' + ' '*(max(n-row,row-n)-1))

hollow_diamond(3)
