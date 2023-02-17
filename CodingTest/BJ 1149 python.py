import sys
n = int(input())
dp = [[0 for _ in range(3)] for _ in range(1001)]
cost = [0]+[list(map(int,sys.stdin.readline().strip('\n').split(' '))) for _ in range(n)]

for i in range(1,n+1) :
    dp[i][0] = min(dp[i-1][1] + cost[i][0],dp[i-1][2] + cost[i][0])
    dp[i][1] = min(dp[i-1][0] + cost[i][1],dp[i-1][2] + cost[i][1])
    dp[i][2] = min(dp[i-1][1] + cost[i][2],dp[i-1][0] + cost[i][2])
print(min(dp[n]))

# r,g,b각각 최소값을 구한 뒤 세개의 최소값으로 
