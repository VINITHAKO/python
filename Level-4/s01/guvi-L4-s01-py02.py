import  sys, string, math, itertools
s,k = input().split()
k = int(k)
L = list(s)
#print(L)
min1 = min(L)
#print(min1)
i1 = L.index(min1)
#print(i1)
if k <= i1 :
    L2 = L[:i1]
    #print(L2)
    while k :
        max1 = max(L2)
        #print(max1)
        L.remove(max1)
        L2.remove(max1)
        k -= 1
    s2 = ''.join(L)
    print(s2)
else :
    L2 = L[i1:]
    L = L2[:]
    k -= i1
    #print(L2)
    while k :
        max1 = max(L2)
        #print(max1)
        L.remove(max1)
        L2.remove(max1)
        k -= 1
    s2 = ''.join(L)
    print(s2)