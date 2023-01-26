import sys
n = int(input())
dp = [[1 for _ in range(10)] for _ in range(1001)]

for i in range(2,n+1) :
    for j in range(8,-1,-1) :
        dp[i][j] = (dp[i][j+1] + dp[i-1][j])%10007
print(sum(dp[n])%10007)
