# Pascal's triangle

# The input is an integer n>3, and the function prints Pascal's triangle with n layers. 
# You do not need to center align the triangle.

def fact(i):
    if i == 0:
        return 1
    else:
        cur = fact(i-1)
        res = i * cur
    return res

def C(p,q):
    return int(fact(p)/(fact(q)*fact(p-q)))

def pascal(n):
    for j in range(n):
        for k in range(j+1):
            print(C(j,k),end = ' ')
        print()

pascal(10)