# jabber = open("/Users/praveenkumar/Desktop/sample.txt", 'r')
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line,end=' ')
#
# jabber.close()

# with open("/Users/praveenkumar/Desktop/sample.txt",'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line,end=' ')
#
#
# with open("/Users/praveenkumar/Desktop/sample.txt",'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for lin in lines[::-1]:
#     print(lin, end='')

#
# city = ['chennai', 'mumbai', 'delhi', 'kolkata', 'banglore']
#
# with open("cities.txt", 'w') as citi:
#     for cit in city:
#         print(cit, file=citi)

#
# city = []
#
# with open("cities.txt", 'r') as citi:
#     for cit in citi:
#         city.append(cit.strip('\n'))
# print(city);


city = "hello", ["hi", "hello"], 1, [1, 2, 3]

with open("tck.txt",'w') as citi:
    for cit in city:
        print(cit, file=citi)