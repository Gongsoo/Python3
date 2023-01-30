#1476
n = list(map(int,input().split()))
year = 1
E = [15] + list(range(1,15))
S = [28] + list(range(1,28))
M = [19] + list(range(1,19))
while True :
    if E[year%15]==n[0] and S[year%28]==n[1] and M[year%19]==n[2] :
        break
    else:
        year +=1
print(year)

#1107
n = int(input())
m = int(input())
b = set()
cnt = abs(100-n)
if m!=0 :
    b = set(input().split(' '))
for i in range(1000001) :
    for j in str(i) :
        if j in b :
            break
    else :
        cnt = min(cnt,len(str(i))+abs(i-n))
print(cnt)

#6064
import math
N = int(input())
for _ in range(N) :
    n,m,x,y = map(int,input().split())
    max_num = n*m//math.gcd(n,m)
    while x<=max_num :
        if (x-y)%m == 0 :
            break
        else: 
            x +=n
    else :
        x = -1
    print(x)
