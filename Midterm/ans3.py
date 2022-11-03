def encoder(s) -> str:
    start = s[0]
    coder = []
    cnt = 1
    for i in s[1:]:
        if i == start:
            cnt += 1
        else:
            coder.append(cnt)
            start = i
            cnt = 1
    coder.append(cnt)
    return "".join(map(str,coder))

print(encoder('11011100')) # 2132
print(encoder('00111001001')) # 232121
print(encoder('101101001101100001000101000111')) # 11211221241311133