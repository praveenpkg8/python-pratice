# fruit = {
#     "a": "apple",
#     "c": "cat",
#     "b": "ball",
#     "d": "dog",
#     "h": "hen"
# }

# print(fruit)
# for i in range(20):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print("==="*40)
#
# order = sorted(list(fruit.keys()))
#
# print(order)
#
# fruitkey = fruit.keys()
# print(fruit)
# print(fruit.items())
# ftuple = tuple(fruit.items())
# print(ftuple)
#
# for scan in ftuple:
#     item, desc = scan
#     print(item + " = "+ desc)


# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
#     student_marks[name] = sum(scores)
# query_name = input()
# d = student_marks[query_name]
# print(format(d/3,'.2f'))
#
# l = [1, 2, 3, 4]
# print(l[len(l)-1])
#
# ar = list(map(int, input().rstrip().split()))
# temp = 0
# count = 0
# for i in ar:
#     if i >= temp:
#         temp = i
#         print(temp)
#         count += 1
# print(count)

arr = input().split(':')
print(arr)
wt = ''
zn = ''
for i in arr:
    for k in i:
        if k in '0123456789':
            wt +=k
        else:
            zn += k
print(wt)
print(zn)

if zn == 'PM':
    print(zn)
else:
    k = 1
    for i in wt:
        if k % 2 == 0:
            print(i, end='')
            print(":", end='')
            k += 1
        else:
            print(i, end='')
            k += 1


