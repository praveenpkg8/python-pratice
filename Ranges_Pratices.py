# o = range(0, 100)
# print(o)
# for i in o:
#     print(i)
# p = o[::5]
# print(p)
# for i in p:
#     print(i)

# a = [int(x) for x in input().split()]
# print(a)

# ==============================
# ab = 'prizes$'
# e = ''
# for a in ab:
#     if not a == '$':
#         e += a
# x = input()
# print(e in x)
#
# # ==============================
# a, b = 12, 13
# print(a, b)
# a, b = b, a
# print(a, b)

# ==============================
# Function definition is here
# def printme(str):
#     print(str)
#     return;
#
#
# # Now you can call printme function
# printme("I'm first call to user defined function!")
# printme("Again second call to the same function")

# # ==============================
# x=1990
# print(x%4)

# # ==============================
import math
# k = -20.12
# print(abs(k))
# print(math.fabs(k))
# k = [1, 2, 3]
# k.append(0)
# print(sorted(k))
# 0
# st = input()
# vt = ''
# for i in range(0,len(st),2):
#     vt[i] = st[i+1]
#     vt[i+1] = st[i]
#
# print(vt)



grades = [int(x) for x in input().split()]
for i in range(0,len(grades)):
    if grades[i] >= 38:
        if(grades[i] % 5 > 2):
            grades[i] = grades[i] + (5-(grades[i]%5))
print(grades)