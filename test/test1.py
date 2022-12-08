# input = [[1,4],[2,19],[3,10],[15,18],[5,16],[0,6],[7,13],[8,11],[9,17],[12,14]]
# output = 5 chords, [[0,6],[1,4],[8,11],[12,14],[15,18]]

# input = [[0,12],[2,6],[3,8],[13,9],[4,5],[7,11],[1,10]]
# output = 4 chords, [[0,12],[2,6],[4,5],[7,11]]

# import sys
# sys.setrecursionlimit(10000)

mylist = [[1,4],[2,19],[3,10],[15,18],[5,16],[0,6],[7,13],[8,11],[9,17],[12,14]]
crdcount = int(len(mylist))
k = [0 for i in range(2*crdcount)]

for n in mylist:
    for m in range(2*crdcount):
        if n[0] == m:
            k[m] = n[1]
        elif n[1] == m:
            k[m] = n[0]
        else:
            pass

global crd_path
crd_path = [i for i in range(10)]

def max_chord(i,j):
    if i >= j:
        return 0
    # case 1: k在外面 (i,j-1)
    elif k[j] > j or k[j] < i:
        crd_path[i] = 1
        return max_chord(i,j-1)
    # case 2: k在裡面 ((k+1,j-1)+(i,k-1))+1 cf.case 1
    elif i < k[j] < j:
        s1 = max_chord(i,j-1)
        s2 = max_chord(k[j]+1,j-1) + max_chord(i,k[j]-1) + 1
        if s2 > s1:
            crd_path[i] = 2
            return s2
        else:
            crd_path[i] = 3
            return s1
        # return max(s1,s2)
    # case 3: k = i (i+1,j-1)+1
    elif k[j] == i:
        crd_path[j] = 4
        return max_chord(i+1,j-1) + 1
print(crd_path)

print(max_chord(0,6))