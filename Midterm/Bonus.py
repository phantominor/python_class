# ### <span style="color:red">Bonus Question:</span> (5 pts)
# You are in a maze and stopped by a magnificent door. You need to enter a password to open the door.
# The password is hidden in an equation.
# For example,
# given an equation as follows:
# $$ a^b + \frac{c}{d} + e = 13.2 $$
# the password is `abcde`, so you need to solve `abcde` that satisfy the equation.
# Assume that we know that {a, b, c, d, e} belong to {2, 3, 4, 5, 6, 7, 8, 9}.
# If you solve `abcde`, you will get the password `23654`, since this sequence satisfies the equation: $2^3 + \frac{6}{5} + 4 = 13.2$.

# Define a function that can help you solve these kinds of problems. The input is a lambda function, the corresponding answer, and a number set (no duplicate for the elements). 
# The function outputs the password (datatype: str) to open the door.
# If more than one sequence satisfies the equation, just return one of them. Assume that the lambda function takes four to eight variables, and the inputs `abcde` of the lambda function are different.

# <span style="color:green"> <b>Hint:</b></span>
# The number of arguments of a lambda function `func` can be found by:
# ```func.__code__.co_argcount```


# <span style="color:green"> <b>Examples:</b></span>
# ```python
# >>> print(door((lambda a,b,c,d,e: a**b + c/d + e), 13.2, [2,3,4,5,6,7,8]))
# 23654  # since 2**3 + 6/5 + 4 = 13.2
# >>> print(door((lambda a,b,c,d,e: a**(b-c) + d*e), 19, [2,3,4,5,6,7,8]))
# 26435 # since 2**(6-4) + 3*5 = 19
# >>> print(door((lambda a,b,c,d: a**2 + b/c + d**3), 18.6, [2,3,4,5,7,8,10]))
# 3852
# ```

def perm_1(nums,j):
    ans = [[]]  # 所有可能排列
    for n in nums:  # 將序列一個一個插進去
        sub_perm = []  # 準備將新插入數字的排列方式存入新list
        for p in ans:  # 一個個叫出還沒插完的可能性排列
            for i in range(len(p)+1):  # 跑出可以插入的位置可能
                sub_perm.append(p[:i] + [n] + p[i:])  # 插入n
        ans = sub_perm  # 刷新所有可能之序列

# print(perm_1([1,2,3,4],3))

def perm_2(nums,j):
    ans = [[]]
    for n in nums:
        if len(ans[0]) >= j:
            break
        for i in range(len(nums)):
            if n not in ans[i]:
                ans[i].append(n)
    return ans
print(perm_2([1,2,3,4],3))