
########################### init ###########################

mylist = [[1,4],[2,19],[3,10],[15,18],[5,16],[0,6],[7,13],[8,11],[9,17],[12,14]]
crdcount = int(len(mylist))

k = [0 for i in range(2*crdcount)]


for n in mylist:
    k[n[0]] = n[1]
    k[n[1]] = n[0]


# 可以在 max_chord 的時候順便紀錄他是 case 幾，這樣 find_chord 就不用再重新看好幾次
crd_path2 = [[-1 for m in range(2*crdcount-n)] for n in range(2*crdcount)]    # crd_path[i][j] == crd_path2[i][j-i]
Case = [[-1 for m in range(2*crdcount-n)] for n in range(2*crdcount)]


######################## max_chord #########################

def max_chord(crd_path,i,j):
    if i >= j:
        return 0
    elif crd_path[i][j-i] >= 0:            # 存過的就可以直接輸出了
        return crd_path[i][j-i]            # 避免存數據的陣列，第一直行直接空掉
   
    # case 1: k在外面 (i,j-1)
    elif k[j] > j or k[j] < i:
        crd_path[i][j-i] = max_chord(crd_path,i,j-1)
        Case[i][j-i] = 1                                               # 加了 case
        return crd_path[i][j-i]
   
    # case 2: k在裡面 ((k+1,j-1)+(i,k-1))+1 cf.case 1
    elif i < k[j] < j:
        s1 = max_chord(crd_path,i,j-1)
        s2 = max_chord(crd_path,k[j]+1,j-1) + max_chord(crd_path,i,k[j]-1) + 1
        if s2 > s1:
            crd_path[i][j-i] = s2
            Case[i][j-i] = 2                                           # 加了 case
            return s2
        else:
            crd_path[i][j-i] = s1
            Case[i][j-i] = 1                                           # 加了 case
            return s1
        # return max(s1,s2)
   
    # case 3: k = i (i+1,j-1)+1
    elif k[j] == i:
        crd_path[i][j-i] = max_chord(crd_path,i+1,j-1) + 1
        Case[i][j-i] = 3                                               # 加了 case
        return crd_path[i][j-i]

    print(crd_path)


####################### find_chord #########################

def find_chord(cur,i,j):
    if i >= j:
        pass
        
    # case 1: k在外面 (i,j-1)
    elif Case[i][j-i] == 1:
        find_chord(cur,i,j-1)
        
    # case 2: k在裡面 ((k+1,j-1)+(i,k-1))+1 cf.case 1
    elif Case[i][j-i] == 2:
        find_chord(cur,i,k[j]-1)
        cur += [[k[j],j]]
        find_chord(cur,k[j]+1,j-1)
        
    # case 3: k = i (i+1,j-1)+1
    elif Case[i][j-i] == 3:
        cur += [[i,j]]
        find_chord(cur,i+1,j-1)


print(max_chord(crd_path2,0,crdcount*2-1))

cur = []
find_chord(cur,0,crdcount*2-1)
print(cur)

######################## 下面還有 ##############################















'''
# 前面都是 recursive (top down) 的方法，但會同樣的 subproblem 會 recursive 好幾次，所以用 bottom up 可以保證全部只看一次
# 填 crd_path 的時候，可以從 i, j 的差小的開始填，每個填一次，但要注意順序不能使用到還沒填過的

crd_path2 = [[-1 for m in range(2*crdcount-n)] for n in range(2*crdcount)]    # crd_path[i][j] == crd_path2[i][j-i]
for i in range(2*crdcount): crd_path2[i][0] = 0

Case = [[-1 for m in range(2*crdcount-n)] for n in range(2*crdcount)]

######################## max_chord #########################

def max_chord(crd_path, pointNum):
    
    for i in range(pointNum):          # i 倒著填
       i = pointNum-1-i
       print(i)
       for j in range(i+1, pointNum):
           # case 1: k在外面 (i,j-1)
           if k[j] > j or k[j] < i:
              crd_path[i][j-i] = crd_path[i][j-1-i]
              Case[i][j-i] = 1
           # case 2: k在裡面 ((k+1,j-1)+(i,k-1))+1 cf.case 1
           elif i < k[j] < j:
              s1 = crd_path[i][j-1-i]
              s2 = crd_path[i][k[j]-i] + crd_path[k[j]][j-k[j]]
              if s2 > s1:
                  crd_path[i][j-i] = s2
                  Case[i][j-i] = 2                                           # 加了 case
              else:
                  crd_path[i][j-i] = s1
                  Case[i][j-i] = 1                                           # 加了 case
          # case 3: k = i (i+1,j-1)+1
           elif k[j] == i:
              crd_path[i][j-i] = crd_path[i+1][j-1-i-1]+1
              Case[i][j-i] = 3                                               # 加了 case

       for a in range(pointNum): print(crd_path[a])
       print('\n')

    return crd_path[0][2*crdcount-1]                                           # 這就是最大值

####################### find_chord #########################

def find_chord(cur,i,j):
    if i >= j:
        pass
        
    # case 1: k在外面 (i,j-1)
    elif Case[i][j-i] == 1:
        find_chord(cur,i,j-1)
        
    # case 2: k在裡面 ((k+1,j-1)+(i,k-1))+1 cf.case 1
    elif Case[i][j-i] == 2:
        find_chord(cur,i,k[j]-1)
        cur += [[k[j],j]]
        find_chord(cur,k[j]+1,j-1)
        
    # case 3: k = i (i+1,j-1)+1
    elif Case[i][j-i] == 3:
        cur += [[i,j]]
        find_chord(cur,i+1,j-1)


print(max_chord(crd_path2,crdcount*2))

cur = []
find_chord(cur,0,crdcount*2-1)
print(cur)

############################################################
'''
