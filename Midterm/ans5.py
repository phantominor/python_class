def dora(intervals):
    intervals = sorted(intervals)
    t = [0 for _ in range(101)]
    t[1] = 1
    dic = dict()
    for s,e in intervals:
        if t[s] == 1: t[e] = 1
        dic[e] = dic.get(s,0) + 1
    pp = [dic[i] for i in dic.keys() if t[i] == 1]
    if len(pp) == 0:
        return 0
    return max(pp)

print(dora([(1,2),(2,4),(4,5),(5,6),(6,7),(7,8),(8,9),(2,3),(3,14),(14,15)]))  # 7
print(dora([(1,2),(1,4),(1,5),(5,6),(4,7),(7,8),(2,19),(19,20),(20,23),(23,24)]))  # 5