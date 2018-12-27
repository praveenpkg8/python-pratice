strr = input()
rs = strr.split()
print(rs)
rst = rs[0]
rstr = ""
for i in range(len(rst)//2,len(rst)):
    rstr = rstr + rst[i]
for i in range(len(rst)//2,-1,-1):
    rstr = rstr + rst[i]
print(rstr)
