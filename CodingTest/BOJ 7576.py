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
        
        
#
