def pascal(n):
    l = [1,1]
    print('1')
    for i in range(1,n):
        print(' '.join(map(str,l)))
        l2 = [l[i]+l[i+1] for i in range(len(l)-1)]
        l2.insert(0,1)
        l2.insert(len(l2),1)
        l = l2[:]

pascal(10)