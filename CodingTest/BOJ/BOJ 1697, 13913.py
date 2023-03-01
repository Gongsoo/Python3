#1697

import sys
from collections import deque
input = sys.stdin.readline


def bfs(x,n) :
    q = deque([x])
    while q :
        now = q.popleft()
        for i in [now-1,now+1,2*now] :
            if 0<= i <100001 and board[i] == 0 and not visited[i]:
                visited[i] = True
                board[i] = board[now] + 1
                q.append(i)
            if i == n :
                break
x, n = map(int,input().split())
board = [0] * 100001
visited = [False] * 100001
visited[x] = True
bfs(x,n)
print(board[n])

#13913
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(now,target,depth,max_depth) :
    if now == target :
        for i in step :
            print(i,end = ' ')
        exit(0)
        return
    if depth >= max_depth :
        return
    for i in g[now] :
        if not visited[i] :
            visited[i] = True
            step.append(i)
            dfs(i,target,depth+1,max_depth)
            visited[i] = False
            step.pop()



def bfs(x,n) :
    q = deque([x])
    while q :
        now = q.popleft()
        for i in [now-1,now+1,2*now] :
            if 0<= i <100001 and board[i] == 0 and not visited[i]:
                visited[i] = True
                g[i].append(now)
                g[now].append(i)
                board[i] = board[now] + 1
                q.append(i)
            if i == n :
                break
x, n = map(int,input().split())
board = [0] * 100001
visited = [False] * 100001
visited[x] = True
g = [[] for _ in range(100001)]
bfs(x,n)
visited = [False] * 100001
step = [x]
visited[x] = True


print(board[n])
dfs(x,n,0,board[n])
