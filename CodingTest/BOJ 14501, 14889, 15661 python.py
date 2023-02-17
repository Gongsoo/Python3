# 14501
n = int(input())
li = [[0,0]] + [list(map(int,input().split())) for _ in range(n)]

visited = [False for _ in range(n+1)]
visited[0] = True
arr = []
max_pay = 0
def dfs(day) :
    global max_pay
    if day == n+1 :
        max_pay = max(max_pay,sum(arr))
        return
    for i in range(day,n+1) :
        if not visited[i] :
            visited[i] = True
            if day+li[i][0]-1 <= n :
                arr.append(li[i][1])

                dfs(i+li[i][0])
            else :
                arr.append(0)

                dfs(i+1)
            visited[i] = False
            arr.pop()
dfs(1)
print(max_pay)

#14889
from itertools import combinations
n = int(input())
li = [list(map(int,input().split())) for _ in range(n)]

visited = [False for _ in range(n)]

start = []
link = []
min_abil = 100*200
def dfs(s) :
    global min_abil
    
    if len(start) == n//2 :
        s_sum = 0
        l_sum = 0
        for i in range(n) :
            if i not in start :
                link.append(i)
        comb_start = combinations(start,2)
        comb_link = combinations(link,2)
        for i in comb_start :
            s_sum += li[i[0]][i[1]] +li[i[1]][i[0]]
        for i in comb_link :
            l_sum += li[i[0]][i[1]] +li[i[1]][i[0]]
        min_abil = min(min_abil,abs(l_sum-s_sum))
        link.clear()
        return
    for i in range(s,n) :
        if not visited[i]:
            visited[i] = True
            start.append(i)
            dfs(i)
            visited[i] = False
            start.pop()

dfs(0)
print(min_abil)

#15661(분석해보자)

import sys
input = sys.stdin.readline
M = int(sys.stdin.readline())
N = M // 2
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
row = [sum(i) for i in stat]
col = [sum(i) for i in zip(*stat)]
newstat = [i+ j for i, j in zip(row, col)]
allstat = sum(newstat) // 2
newstat.sort()
c = [0]
for i in newstat[:N]:
    c.extend([i + j for j in c])
c = set(c)
bot_up = [i in c for i in range(allstat + 1)]
for i in newstat[N:]:
    bot_up[i:] = [a or b for a, b in zip(bot_up[i:], bot_up)]
for i in range(allstat, -1, -1):
    if bot_up[i]:
        print(allstat - i)
        break

# 2529
n = int(input())
li = list(map(str,input().split()))
num = list(range(10))
visited = [False for _ in range(10)]
arr = []
ans = []
def dfs() :
    if len(arr) == n+1 :
        for i in range(n) :
            if li[i] == '>' :
                if arr[i] > arr[i+1] :
                    continue
                else :
                    break
            else:
                if arr[i] < arr[i+1] :
                    continue
                else :
                    break
        else:
            ans.append(''.join(map(str,arr)))
        return
    for i in range(10):
        if not visited[i] :
            visited[i] = True
            arr.append(num[i])
            dfs()
            visited[i] = False
            arr.pop()
dfs()
print(ans[-1])
print(ans[0])
