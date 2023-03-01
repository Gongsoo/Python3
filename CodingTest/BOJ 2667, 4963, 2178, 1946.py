#2667 
#bfs는 신이다
import sys
from collections import deque
input = sys.stdin.readline
k = int(input())
li = [list(map(int,input().strip('\n'))) for _ in range(k)]
answer = []
visited = [[False for _ in range(k)] for _ in range(k)]
num = 1
def bfs(visited,now) :
    cnt = 1
    x,y = now
    visited[x][y] = True
    q = deque([(x,y)])
    while q :
        tx, ty = q.popleft()
        for idx, idy in [(0,1),(0,-1),(1,0),(-1,0)] :
            if 0<= idx+tx < k and 0 <= idy+ty < k :
                if not visited[idx+tx][idy+ty] and li[idx+tx][idy+ty]:
                    q.append((tx+idx,ty+idy))
                    visited[tx+idx][ty+idy] = True
                    cnt+=1
    return cnt

for i in range(k) :
    for j in range(k) :
        if li[i][j] and not visited[i][j]:
            cnt = bfs(visited,[i,j])
            answer.append((num,cnt))
            num+=1

print(len(answer))
answer.sort(key = lambda x : x[1])
for a in answer :
    print(a[1])
#4963
import sys
from collections import deque
input = sys.stdin.readline
while True :
    w, h = map(int,input().split())
    if not w and not h :
        break
    li = [list(map(int,input().strip('\n').split())) for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]
    num = 0
    def bfs(visited,now) :

        x,y = now
        visited[x][y] = True
        q = deque([(x,y)])
        while q :
            tx, ty = q.popleft()
            for idx, idy in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)] :
                if 0<= idx+tx < h and 0 <= idy+ty < w :
                    if not visited[idx+tx][idy+ty] and li[idx+tx][idy+ty]:
                        q.append((tx+idx,ty+idy))
                        visited[tx+idx][ty+idy] = True

    for i in range(h) :
        for j in range(w) :
            if li[i][j] and not visited[i][j]:
                bfs(visited,[i,j])
                num+=1

    print(num)

#2178
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int,input().split())
li = [list(map(int,input().strip('\n'))) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dp = [[100*100+1 for _ in range(m)] for _ in range(n)]
dp[0][0] = 1
def bfs(visited,now,depth) :
    global answer
    if now == [n-1,m-1] :
        answer = min(answer,depth)
    x,y = now
    visited[x][y] = True
    q = deque([now])
    while q :
        tx, ty = q.popleft()
        for idx, idy in [(0,1),(0,-1),(1,0),(-1,0)] :
            nx, ny = idx+tx, idy+ty
            if 0<= nx < n and 0 <= ny < m :
                if not visited[nx][ny] and li[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    dp[nx][ny] = min(dp[nx][ny],dp[tx][ty]+1)

bfs(visited,[0,0],1)
print(dp[-1][-1])


#1946
import sys
from collections import deque
input = sys.stdin.readline
k = int(input())
for _ in range(k):
    n = int(input())
    ans = 0
    rank = []
    for i in range(n) :
        a,b = map(int,input().split())
        rank.append([a,b])
    rank.sort(key = lambda x : x[0])
    e_s, i_s = rank[0]
    for x, y in rank :
        if y <= i_s :
            i_s = y
            ans+=1
    print(ans)
