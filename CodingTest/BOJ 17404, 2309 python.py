# 17404
import sys
n = int(input())
answer = 1001*1001
rgb = [0] + [list(map(int,sys.stdin.readline().strip('\n').split(' '))) for _ in range(n)]
dp = [[0 for _ in range(3)] for _ in range(n+1)]
for num in range(3) :
    for now in range(3) :
        if num == now :
            dp[1][now] = rgb[1][now]
        else :
            dp[1][now] = 1001*1001
    for i in range(2,n+1) :
        dp[i][0] = min(dp[i-1][1] + rgb[i][0],dp[i-1][2] + rgb[i][0])
        dp[i][1] = min(dp[i - 1][0] + rgb[i][1], dp[i - 1][2] + rgb[i][1])
        dp[i][2] = min(dp[i - 1][0] + rgb[i][2], dp[i - 1][1] + rgb[i][2])
    for j in range(3) :
        if j == num :
            continue
        answer = min(answer,dp[n][j])
    print(dp)
print(answer)

# 2309
from itertools import combinations
t = []
for _ in range(9) :
    t.append(int(input()))
t_con = list(combinations(t,7))

for i in t_con :
    if sum(i) == 100 :
        ans = sorted(i)
        for j in ans :
            print(j)
        break

