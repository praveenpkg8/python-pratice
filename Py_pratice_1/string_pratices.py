# mylist = ["a", "b", "c", "d"]
# letters = "abcdefghijklmnopqrstuvwxyz"
# st=", ".join(mylist)
# lt = ", ".join(letters)
# print(st)
# print(lt)
#

#
# st = input()
# vt = ''
# for l in st:
#     if l in 'abcdefghijklmnopqrstuvwxyz':
#         vt = vt + l.upper()
#     elif l in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#         vt = vt + l.lower()
#     else:
#         vt += l
#
# print(vt)
#
# st = input()
# vt = ''
# for l in st:
#     if l is ' ':
#         vt += '-'
#     else:
#         vt += l
#
# print(vt)

# string = input()
# vt = ''
# i = 0
# for l in string:
#     if i % 4 == 0:
#         vt += "\n"
#     vt += l
#     i += 1
#
# print(vt)
n = int(input())
for i in range(1,n+1):
    print("-" * ((3*(n-(i-1))-3)//2) + ".|." + "-" * (((3*(n-(i-1))-3)//2)))
