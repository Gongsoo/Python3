#10430
A,B,C = map(int,input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)
#2609
import sys
def gcd(x,y) :
    for i in range(max(x,y),0,-1) :
        if not x%i and not y%i :
            return i

a,b= map(int,sys.stdin.readline().split())

print('{}\n{}'.format(gcd(a,b),a*b//gcd(a,b)))
#1934
import sys
def gcd(x,y) :
    for i in range(max(x,y),0,-1) :
        if not x%i and not y%i :
            return i

a,b= map(int,sys.stdin.readline().split())

print(a*b//gcd(a,b))
#1850
n, m = map(int,input().split())
a,b = max(n,m), min(n,m)
def gcd(x,y) :
    
    n, m = divmod(x,y)
    if m :
        x, y = gcd(y,m)
    print(x,y,n,m)
    return x,y
print('1'*gcd(a,b)[1])
#9613
import sys
import math
from itertools import combinations

n = int(input())

for _ in range(n) :
    num = list(map(int,sys.stdin.readline().split()))
    N = num[0]
    num = num[1:]
    num_list = list(combinations(num,2))
    gcd_sum = 0
    for i in num_list :
        gcd_sum += math.gcd(i[0],i[1])
    print(gcd_sum)
