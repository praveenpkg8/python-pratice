# a = [int(x) for x in input().split()]
# n = a[0]
# q = a[1]
#
#
# s = input()
# l = []
# r = []
# k = []
# for i in range(0,q):
#     x = [int(x) for x in input().split()]
#     l.append(x[0])
#     r.append(x[1])
#     k.append(x[2])
#     del x[:]
#
# for i in range(0,q):
#     for t in range(l[i],r[i]+1):
#         print(s[l[i]+k[i]-2])
#         break
# li = [1, 3, 5, 4]
# li.sort()
# print(li)
v = int(input())
for i in range(0,v):
    a = [int(x) for x in input().split()]
    n = a[0]
    t = a[1]
    lst = [int(x) for x in input().split()]
    alst = lst
    alst.sort()
    lst.sort()
    sum = 0
    for k in range(0,t):
        if lst[k] == alst[k]:
            sum += lst[k]
        elif lst[k] < alst[k]:
            sum += lst[k]
        elif lst[k] > alst[k]:
            sum += alst[k]
        alst.append(lst[k]*2)
        alst.sort()
    print(sum)
    del lst[:]
    del alst[:]
    sum = 0




