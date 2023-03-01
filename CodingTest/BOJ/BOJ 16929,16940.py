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


#16964 set은 신이다
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(is_dfs) :
    tmp = is_dfs.popleft()
    if not is_dfs :
        print(1)
        exit()
    visited[tmp] = True
    set_g = set(g[tmp])
    for i in range(len(g[tmp])) :
        if is_dfs[0] in set_g and not visited[is_dfs[0]] :
            dfs(is_dfs)
    return False

n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(n-1) :
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
visited = [False for _ in range(n+1)]
is_dfs = deque(list(map(int,input().strip('/n').split())))
if is_dfs[0] != 1 :
    print(0)
    exit()
if not dfs(is_dfs) :
    print(0)
    
#2146 내일 풀어볼게요
#아이디어 : 섬 테두리좌표를 얻어놨는데 그거보다 그냥 바로 bfs해ㅓ 다 채우던가 아니면 좌표기반으로 다시 bfs할것인가 고민해보쟈
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(is_dfs) :
    tmp = is_dfs.popleft()
    if not is_dfs :
        print(1)
        exit()
    visited[tmp] = True
    set_g = set(g[tmp])
    for i in range(len(g[tmp])) :
        if is_dfs[0] in set_g and not visited[is_dfs[0]] :
            dfs(is_dfs)
    return False

def bfs(g,num,now) :
    q= deque([now])
    while q :
        tx, ty = q.popleft()
        for idx, idy in [(0,1),(0,-1),(1,0),(-1,0)] :
            nx, ny = idx+tx, idy+ty
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and g[nx][ny]==1:
                visited[nx][ny] = True
                q.append([nx,ny])
                g[nx][ny] -= num
            elif 0<=nx<n and 0<=ny<n and g[nx][ny] == 0 :
                side[-1].add((nx,ny))


n = int(input())
g = [list(map(int,input().strip('/n').split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
num = 2
side = []
for i in range(n) :
    for j in range(n) :
        if g[i][j] == 1 :
            side.append(set())
            g[i][j] -=num
            visited[i][j] = True
            bfs(g,num,[i,j])
            num+=1

