#1248
n = int(input())
a = [[0]*n for _ in range(n)]
b = list(input())
v, k = [], 0

def possible(idx):
    s = 0
    for i in range(idx, -1, -1):
        s += v[i]
        if a[i][idx] == '+' and s <= 0:
            return False
        if a[i][idx] == '0' and s != 0:
            return False
        if a[i][idx] == '-' and s >= 0:
            return False
    return True

def solve(idx):
    if idx == n:
        print(' '.join(map(str, v)))
        exit(0)
    for i in range(-10, 11):
        v.append(i)
        if possible(idx):
            solve(idx+1)
        v.pop()

for i in range(n):
    for j in range(i, n):
        a[i][j] = b[k]
        k += 1
solve(0)

#11723
import sys
input = sys.stdin.readline
n = int(input())
S = [0 for _ in range(20)]

for _ in range(n) :
    command = input().split() + [0]
    command[1] = int(command[1])
    
    if command[0] == 'add' :
        S[command[1]-1] = 1
    elif command[0] == 'remove' :
        S[command[1]-1] = 0
    elif command[0] == 'check' :
        print(1 if S[command[1]-1] else 0)
    elif command[0] == 'toggle' :
        if S[command[1]-1] :
            S[command[1]-1] = 0
        else :
            S[command[1]-1] = 1
    elif command[0] == 'all' :
        S = [1 for _ in range(20)]
    elif command[0] == 'empty' :
        S = [0 for _ in range(20)]

#1182
import sys
from itertools import combinations
input = sys.stdin.readline
n, target = map(int,input().split())
li = list(map(int,input().split()))
cnt = 0
for i in range(1,1<<n) :
    
    tmp = sum(li[j] for j in range(n) if (i&(1<<j))>0)
    
    if tmp == target :
        cnt+=1
print(cnt)

#14391 다시보기
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
cost = [list(map(int,input().rstrip())) for _ in range(n)]
ans = 0
for i in range(1<<n*m) :
    total = 0
    for row in range(n) :
        row_sum = 0
        for col in range(m) :
            idx = row*m + col
            if i&(1<<idx) !=0 :
                row_sum = row_sum*10+cost[row][col]
            else :
                total += row_sum
                row_sum = 0
        total += row_sum
    for col in range(m) :
        col_sum = 0
        for row in range(n) :
            idx = row*m + col
            if i&(1<<idx) ==0 :
                col_sum = col_sum*10+cost[row][col]
            else :
                total += col_sum
                col_sum = 0
        total += col_sum
    ans = max(ans,total)
print(ans)

#13023
import sys

input = sys.stdin.readline
n, m = map(int,input().split())
g = [[]for _ in range(n)]
visited = [False for _ in range(n)]

def dfs(x, depth) :
    visited[x] = True
    if depth >=4 :
        print(1)
        exit()
    for i in g[x] :
        if not visited[i] :
            visited[i] = True
            dfs(i,depth+1)
            visited[i] = False

for _ in range(m) :
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(n) :
    visited[i] = True
    dfs(i,0)
    visited[i] = False
print(0)
