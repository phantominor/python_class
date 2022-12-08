
########################### init ###########################

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
'''
可以醬
for n in mylist:
   k[n[0]] = n[1]
   k[n[1]] = n[0]
'''


######################## max_chord #########################

def max_chord(crd_path,i,j):                             '''多傳一個參數'''
    print(crd_path)
    
    if i >= j:
        return 0
   
    elif crd_path[i][j] != -1:                           '''init 成 -1, 如果做過了就可以直接用，沒填過再往下做，不然會重複做很多次'''
        return crd_path[i][j]
   
    # case 1: k在外面 (i,j-1)
    elif k[j] > j or k[j] < i:
        crd_path[i][j] = max_chord(crd_path,i,j-1)
        return crd_path[i][j]                            '''醬比較快吧，不然要再多 call 一層'''
   
    # case 2: k在裡面 ((k+1,j-1)+(i,k-1))+1 cf.case 1
    elif i < k[j] < j:
        s1 = max_chord(crd_path,i,j-1)
        s2 = max_chord(crd_path,k[j]+1,j-1) + max_chord(crd_path,i,k[j]-1) + 1
        if s2 > s1:
            crd_path[i][j] = s2                          '''s2'''
            return s2
        else:
            crd_path[i][j] = s1                          '''s1'''
            return s1
        # return max(s1,s2)
   
    # case 3: k = i (i+1,j-1)+1
    elif k[j] == i:
        crd_path[i][j] = max_chord(crd_path,i+1,j-1) + 1
        return crd_path[i][j]                          '''crd_path[i][j]'''

    print(crd_path)
    '''也可以上面的 return 都拿掉，在這邊 return crd_path[i][j]'''


####################### find_chord #########################

def find_chord(cur,i,j):
    if i >= j:
        pass
      
    # case 1: k在外面 (i,j-1)
    elif k[j] > j or k[j] < i:
        find_chord(i,j-1)                                   '''可以不 return '''
        
    # case 2: k在裡面 ((k+1,j-1)+(i,k-1))+1 cf.case 1
    elif i < k[j] < j:
        s1 = crd_path[i][j-1]
        s2 = crd_path[k[j]+1][j-1] + crd_path[i][k[j]-1] + 1
        if s2 > s1:
            cur += [[k[j],j]]
        else:
            find_chord(i,j-1)                               '''可以不 return '''
         
    # case 3: k = i (i+1,j-1)+1
    elif k[j] == i:
        cur += [[i,j]]
        find_chord(i+1,j-1)                                '''可以不 return '''

'''find_chord 這樣做的話會看過很多重複的東西(畫樹狀圖可以看得出來)，所以可以把它是 case 幾記下來(看下面)'''


crd_path = [[-1 for m in range(2*crdcount)] for n in range(2*crdcount)]    '''有一個方法是做三角形陣列比較省空間，看下面'''
cur = []

print(max_chord(crd_path,0,crdcount*2-1))    '''這裡是醬吧'''
find_chord(cur,0,crdcount*2-1)
print(cur)

############################################################







'''
可以在 max_chord 的時候順便紀錄他是 case 幾，這樣 find_chord 就不用再重新看好幾次
######################## max_chord #########################

crd_path2 = [[-1 for m in range(2*crdcount)] for n in range(2*crdcount-n)]    # crd_path[i][j] == crd_path2[i][j-i]
Case = [[-1 for m in range(2*crdcount)] for n in range(2*crdcount-n)]

def max_chord(crd_path,i,j):
    
    if i >= j:
        return 0
    elif crd_path[i][j-i] >= 0:
      return crd_path[i][j-i]
   
    # case 1: k在外面 (i,j-1)
    elif k[j] > j and k[j] < i:
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
        find_chord(i,j-1)
        
    # case 2: k在裡面 ((k+1,j-1)+(i,k-1))+1 cf.case 1
    elif Case[i][j-i] == 2:
        find_chord(i,k[j]-1)
        cur += [[k[j],j]]
        find_chord(k[j]+1,j-1)
         
    # case 3: k = i (i+1,j-1)+1
    elif Case[i][j-i] == 3:
        cur += [[i,j]]
        find_chord(i+1,j-1)


crd_path = [[-1 for m in range(2*crdcount)] for n in range(2*crdcount)]
cur = []

print(max_chord(crd_path,0,crdcount*2-1))
find_chord(cur,0,crdcount*2-1)
print(cur)

############################################################
'''




########################################################################################################




'''
前面都是 recursive (top down) 的方法，但會同樣的 subproblem 會 recursive 好幾次，所以用 bottom up 可以保證全部只看一次
填 crd_path 的時候，可以從 i, j 的差小的開始填，每個填一次，但要注意順序不能使用到還沒填過的
######################## max_chord #########################

crd_path2 = [[-1 for m in range(2*crdcount)] for n in range(2*crdcount-n)]    # crd_path[i][j] == crd_path2[i][j-i]
Case = [[-1 for m in range(2*crdcount)] for n in range(2*crdcount-n)]

def max_chord(crd_path,i,j):

    for i in [2*crdcount-2-a for a in range(2*crdcount-1)]:          # i 倒著填
       for j in range(i, 2*crdcount):
           if i >= j:
              crd_path[i][j-i] = 0
   
           # case 1: k在外面 (i,j-1)
           elif k[j] > j and k[j] < i:
              crd_path[i][j-i] = crd_path[i][j-1-i]
              Case[i][j-i] = 1
            
           # case 2: k在裡面 ((k+1,j-1)+(i,k-1))+1 cf.case 1
           elif i < k[j] < j:
              s1 = crd_path[i][j-1-i]
              s2 = crd_path[i][k-i] + crd_path[k][j-k] + 1
              if s2 > s1:
                  crd_path[i][j-i] = s2
                  Case[i][j-i] = 2                                           # 加了 case
              else:
                  crd_path[i][j-i] = s1
                  Case[i][j-i] = 1                                           # 加了 case
            
          # case 3: k = i (i+1,j-1)+1
          elif k[j] == i:
              crd_path[i][j-i] = crd_path[i+1][j-1-i-1]
              Case[i][j-i] = 3                                               # 加了 case

    print(crd_path)
    return crd_path[0][2*crdcount-1]                                           # 這就是最大值

############################################################
'''
