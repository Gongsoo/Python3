import sys
n = int(input())
cost = sys.stdin.readline().strip('\n').split(' ')
cost = [0]+list(map(int,cost))
dp = [False]*(n+1)
for i in range(1,n+1) :
    for j in range(1,i+1) :
            dp[i] = max(dp[i],dp[i-j]+cost[j])

print(dp[n])




import sys
n = int(input())
cost = sys.stdin.readline().strip('\n').split(' ')
cost = [0]+list(map(int,cost))
dp = [False]*(n+1)
for i in range(1,n+1) :
    for j in range(1,i+1) :
        if dp[i] == False :
            dp[i] = cost[j] + dp[i-j]
        else :
            dp[i] = min(dp[i],dp[i-j]+cost[j])

print(dp[n])
