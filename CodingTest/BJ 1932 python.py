import sys
n = int(input())
tri = [0] + [list(map(int,sys.stdin.readline().strip('\n').split(' '))) for _ in range(n)]

dp = [0]+[[0 for _ in range(i+1)] for i in range(n)]
dp[1] = tri[1]
for i in range(2,n+1) :
    for j in range(len(tri[i])) :
        if j == 0 :
            dp[i][j] = dp[i-1][j] + tri[i][j]
        elif j == i-1 :
            dp[i][j] = dp[i-1][j-1] + tri[i][j]
        else:
            dp[i][j] = max(dp[i-1][j] + tri[i][j],dp[i-1][j-1] + tri[i][j])

print(max(dp[n]))

# 트리나 힙으로 하면 되지 않을까라고 생각했지만 멍청한 나는 노가다로 풀었다.. 
