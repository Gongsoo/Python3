import sys
input = sys.stdin.readline

n = int(input())

num = list(map(int,input().split()))
visited = [False] * n
result = set()
tmp = []
def dfs(start) :
    if not sum(tmp) in result :
        result.add(sum(tmp))
    for i in range(start,n) :
        if not visited[i] :
            visited[i] = True
            tmp.append(num[i])
            dfs(i)
            visited[i] = False
            tmp.pop()

dfs(0)
for i in range(1,max(result)+1) :
    if not i in result :
        print(i)
        break
else :
    print(max(result)+1)
