# run length encoder

# turn a bit string into run length
# example:
# >>> print(encoder('11011100'))
# 2132

def encoder(s):
    a = s[0]
    p = 0
    ans = []
    for i, n in enumerate(s):
        if n != a and i == len(s)-1:
            ans += [i-p]
            ans += [1]
        elif n == a and i == len(s)-1:
            ans += [i-p+1]
        elif n != a:
            ans += [i-p]
            p = i
            a = n
        else:
            pass
    res = str()
    for i in ans:
        res += str(i)
    return res

print(encoder('11011100')) # 2132
print(encoder('00111001001')) # 232121
print(encoder('101101001101100001000101000111')) # 11211221241311133