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


#===============================================================



#
# v = int(input())
# for i in range(0,v):
#     a = [int(x) for x in input().split()]
#     n = a[0]
#     t = a[1]
#     lst = [int(x) for x in input().split()]
#     alst = lst
#     alst.sort()
#     lst.sort()
#     sum = 0
#     for k in range(0,t):
#         if lst[k] == alst[k]:
#             sum += lst[k]
#         elif lst[k] < alst[k]:
#             sum += lst[k]
#         elif lst[k] > alst[k]:
#             sum += alst[k]
#         alst.append(lst[k]*2)
#         alst.sort()
#     print(sum)
#     del lst[:]
#     del alst[:]
#     sum = 0


# a = [int(x) for x in input().split()]
# a.sort()
# x=max(a)
# for i in range(0,len(a)):
#     if a[i] == x:
#         break
# print(a[i-1])

# n = int(input())
# marksheet = [[input(), float(input())] for _ in range(n)]
# print(marksheet)
# marksheet.sort()
# print(marksheet)
#

N = int(input())

students = list()
for i in range(N):
    students.append([input(), float(input())])

scores = set([students[x][1] for x in range(N)])
scores = list(scores)
scores.sort()
print(scores)

students = [x[0] for x in students if x[1] == scores[1]]
print(students)
students.sort()
print(students)
#
#
# for s in students:
#    print(s)

# lt = [37.21, 37.21, 41, 39, 37.2]
# lt.sort()
# print(lt)



