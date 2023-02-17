#1748
n = input()
l = len(n)
n = int(n)
cnt = 0
cnt += (n - 10**(l-1)+1) * l
l-=1
while l != 0 :
    cnt += (10**l - 10**(l-1)) * l
    l-=1
print(cnt)

#15649
from itertools import permutations
n,m = map(int,input().split())
l = list(range(1,n+1))
com = list(permutations(l,m))

for i in sorted(com) :
    for j in i :
        print(j,end = ' ')
        
#15650
from itertools import combinations
n,m = map(int,input().split())
l = list(range(1,n+1))
com = list(combinations(l,m))

for i in sorted(com) :
    for j in i :
        print(j,end = ' ')
        
#15651
from itertools import product
n,m = map(int,input().split())
l = list(range(1,n+1))
com = list(product(l,repeat = m))

for i in sorted(com) :
    for j in i :
        print(j,end = ' ')
#15652
from itertools import combinations_with_replacement
n,m = map(int,input().split())

for i in combinations_with_replacement(range(1,n+1),m) :
    for j in i :
        print(j,end=' ')
#배운것 combinations_with_replacement(list,int) 중복조합
#구현 코드
def combi(level, start):
  #종료조건
  if level >= k:
    print(arr)
    return
  
  for i in range(start, len(A)):
    arr[level] = A[i]
    combi(level+1, i)

combi(0,0)
