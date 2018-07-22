fruit = {
    "a": "apple",
    "c": "cat",
    "b": "ball",
    "d": "dog",
    "h": "hen"
}

# print(fruit)
# for i in range(20):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print("==="*40)
#
# order = sorted(list(fruit.keys()))
#
# print(order)

fruitkey = fruit.keys()
print(fruit)
print(fruit.items())
ftuple = tuple(fruit.items())
print(ftuple)

for scan in ftuple:
    item, desc = scan
    print(item + " = "+ desc)
