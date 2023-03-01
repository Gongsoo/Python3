#11724
import sys
from collections import deque
input = sys.stdin.readline
def bfs(s,g,visited) :
    q = deque([s])
    visited[s] = True
    while q :
        x = q.popleft()
        for i in g[x] :
            if not visited[i] :
                visited[i] = True
                q.append(i)
n,m = map(int,input().split())
g = [[] for _ in range(n+1)]
for _ in range(m) :
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
visited = [False for _ in range(n+1)]
cnt = 0
for i in range(1,n+1) :
    if not visited[i] :
        bfs(i,g,visited)
        cnt +=1
print(cnt)

#1260 출력이 날 힘들게해,,
import sys
from collections import deque
input = sys.stdin.readline
def dfs(s,g) :
    visited[s] = True
    print(s,end=' ')
    for i in g[s] :
        if not visited[i] :
            dfs(i,g)
def bfs(s,g) :
    q = deque([s])
    visited[s] = True
    while q :
        x = q.popleft()
        print(x,end=' ')
        for i in g[x] :
            if not visited[i] :
                visited[i] = True
                q.append(i)
n,m,v = map(int,input().split())
g = [[] for _ in range(n+1)]
for _ in range(m) :
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
    g[a].sort()
    g[b].sort()
visited = [False for _ in range(n+1)]
dfs(v,g)
print()
visited = [False for _ in range(n+1)]
bfs(v,g)
