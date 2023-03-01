#15654
from itertools import permutations
n,m = map(int,input().split())
li = list(map(int,input().split()))

com = list(permutations(sorted(li),m))
for i in com :
    for j in i :
        print(j,end=' ')
#15655
from itertools import combinations
n,m = map(int,input().split())
li = list(map(int,input().split()))

com = list(combinations(sorted(li),m))
for i in com :
    for j in i :
        print(j,end=' ')
#15656
from itertools import product
n,m = map(int,input().split())
li = list(map(int,input().split()))

com = list(product(sorted(li),repeat = m))
for i in com :
    for j in i :
        print(j,end=' ')
#15657
from itertools import combinations_with_replacement
n,m = map(int,input().split())
li = list(map(int,input().split()))

com = list(combinations_with_replacement(sorted(li),m))
for i in com :
    for j in i :
        print(j,end=' ')

#15663
from itertools import permutations
n,m = map(int,input().split())
li = list(map(int,input().split()))

com = list(permutations(sorted(li),m))
for i in sorted(set(com)) :
    for j in i :
        print(j,end=' ')

#15664

n,m = map(int,input().split())
li = sorted(list(map(int,input().split())))

visited = [False for _ in range(n)]
ans = []
def dfs(start) :
    if len(ans) == m :
        for i in ans :
            print(i, end=' ')
        return
    tmp = 0
    for i in range(start,n) :
        if not visited[i] and tmp!=li[i] :
            visited[i] = True
            ans.append(li[i])
            tmp = li[i]
            dfs(i+1)
            visited[i] = False
            ans.pop()
dfs(0)#재귀함수 공부하기

#15665
n,m = map(int,input().split())
li = sorted(list(map(int,input().split())))

ans = []
def dfs() :
    if len(ans) == m :
        for i in ans :
            print(i, end=' ')
        return
    tmp = 0
    for i in range(0,n) :
        if tmp!=li[i] :
            ans.append(li[i])
            tmp = li[i]
            dfs()
            ans.pop()
dfs()

#15666