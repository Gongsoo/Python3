import sys
n = int(input())
dp = [[0 for _ in range(3)]for _ in range(100001)]
dp[0] = [1, 0, 0]
for i in range(1,n+1) :
    dp[i][0] = (dp[i-1][1] + dp[i-1][2] +dp[i-1][0])%9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2])%9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1])%9901
print(sum(dp[n])%9901)

# 0: 사자배치안함 1: 사자 왼쪽배치 2: 사자 오른쪽 배치
# 0일때 이전줄에 0이어도 되는거를 생각못해서,,, 
# 마지막 print할때도 mod를 잊지말자,,,
