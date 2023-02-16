#16929
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(board,start,now,depth) :
    global dots
    x, y = now
    color = board[x][y]
    if start == now and depth>=4 :
        dots = True
        return
    for idx, idy in [(0,1),(0,-1),(1,0),(-1,0)] :
        nx, ny = idx + x, idy + y
        if 0<=nx<n and 0<=ny<m :
            if not visited[nx][ny] and board[nx][ny] == color :
                visited[nx][ny] = True
                dfs(board,start,[nx,ny],depth+1)
            elif start == [nx,ny] and depth>=4 :
                dfs(board,start,[nx,ny],depth)


n, m = map(int,input().split())
board = [list(input().strip('\n')) for _ in range(n)]

for i in range(n) :
    for j in range(m) :
        visited = [[False for _ in range(m)] for _ in range(n)]
        dots = False
        visited[i][j] = True
        dfs(board,[i,j],[i,j],1)
        if dots :
            print('Yes')
            exit()
print('No')

#16940
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(n-1) :
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
is_bfs = list(map(int,input().split()))
is_bfs = deque(is_bfs)
visited = [False for _ in range(n+1)]

q = deque()
q.append(is_bfs.popleft())
if q[0] != 1 :
    print(0)
    exit()
while q :
    next_node = q.popleft()
    visited[next_node] = True
    tmp = []
    check = []
    for i in g[next_node] :
        if not visited[i] :
            visited[i] = True
            zz = is_bfs.popleft()
            check.append(zz)
            tmp.append(i)
    tmp = set(tmp)
    for j in check :
        if not j in tmp :
            print(0)
            exit()
        else :
            q.append(j)
print(1)
