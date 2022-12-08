global aa
aa = [[1 for j in range(10)] for i in range(10)]
def fxn(c):
    if c == 0 or c == 1:
        return 1
    else:
        aa[c][c-2] = fxn(c-1)
        return fxn(c-1) + fxn(c-2)

fxn(9)
print(aa)