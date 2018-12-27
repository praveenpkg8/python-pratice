# N, M = map(int, input().split())
# for i in range(1, N, 2):
#     print(str('.|.' * i).center(M, '-'))
# print('WELCOME'.center(M, '-'))
# for i in range(N-2, -1, -2):
#     print(str('.|.' * i).center(M, '-'))
#

n = int(input())
m = n
for i in range(1,n+1,2):
    print(str(chr(64 + m) * i).center(n * 3,'-'))
    m -= 1
for i in range(n-2, -1, -2):
    print(str(chr(64 + m) * i).center(n * 3,'-'))

