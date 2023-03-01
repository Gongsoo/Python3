#7576
#하,,
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int,input().split())

box = [list(map(int,input().strip('\n').split())) for _ in range(m)]
day = [[0 for _ in range(n)] for _ in range(m)]
start = deque()
for i in range(m) :
    for j in range(n) :
        if box[i][j] == 1 :
            start.append([i,j])

while start :
    tx, ty = start.popleft()
    for idx, idy in [(0,1),(0,-1),(1,0),(-1,0)] :
        nx, ny = idx+tx, idy+ty
        if 0<= nx < m and 0<= ny < n and box[nx][ny]==0:
            box[nx][ny] = box[tx][ty]+1
            start.append([nx,ny])
answer = max(map(max,box)) -1 # 이렇게 표현할 수도 있다,, 천재인가,,?
for b in box :
    if 0 in b :
        answer = -1
print(answer)

#7562
import sys
from collections import deque
input = sys.stdin.readline
k = int(input())

for __ in range(k) :
    
    n = int(input())
    x, y = map(int,input().split())
    tx, ty = map(int,input().split())
    
    g = [[0 for _ in range(n)] for _ in range(n)]
    start = deque()
    start.append((x,y))
    while start :
        i, j = start.popleft()
        if [i,j] == [tx,ty] :
            print(g[i][j])
            break
        for idx, idy in [(1,2),(1,-2),(-1,2),(-1,-2),(-2,1),(2,-1),(-2,-1),(2,1)] :
            nx, ny = i+idx, j+idy
            if 0<=nx<n and 0<=ny<n and g[nx][ny]==0 :
                g[nx][ny] = g[i][j]+1
                start.append((nx,ny))
        
        
#16947 
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs(idx, cnt):
    if cycle_station[idx]:
        if cnt - distance[idx] >= 3:
            return idx
        else: return -1
        
    cycle_station[idx] = 1
    distance[idx] = cnt
    
    for y in link[idx]:
        cycleStartNode = dfs(y, cnt + 1)
        
        if cycleStartNode != -1:
            cycle_station[idx] = 2
            if idx == cycleStartNode: return -1
            else: return cycleStartNode
            
    return -1

if __name__ == '__main__':
    N = int(input())
    link = [[] * N for _ in range(N)]
    # cycle_station[i] = 0 : 방문하지 않은 노드
    # cycle_station[i] = 1 : 방문한 노드
    # cycle_station[i] = 2 : 사이클에 속하는 노드
    cycle_station = [0] * N
    distance = [0] * N

    for _ in range(N):
        a, b = map(int, input().split())
        link[a - 1].append(b - 1)
        link[b - 1].append(a - 1)

    dfs(1, 0)

    queue = deque()
    for i in range(N):
        if cycle_station[i] == 2:
            queue.append(i)
            distance[i] = 0
            
        else:
            distance[i] = -1
            
    while queue:
        now = queue.popleft()
        
        for y in link[now]:
            if distance[y] == -1:
                queue.append(y)
                distance[y] = distance[now] + 1
                
    print(*distance)
    

