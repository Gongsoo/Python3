import sys
n = int(input())
s = [0] + list(map(int,sys.stdin.readline().strip('\n').split(' ')))

dp = [0 for _ in range(n+1)]

for i in range(1,n+1) :
    dp[i] = s[i]

    for j in range(1,i+1) :
        if s[i] > s[j]:
            dp[i] = max(dp[i],dp[j]+s[i])
print(max(dp))