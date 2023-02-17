n = int(input())
dp = [[0 for _ in range(10)] for i in range(n+1)]
dp[1] = [0,1,1,1,1,1,1,1,1,1]

for i in range(2,n+1) :
    for j in range(1,9) :
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]

print(sum(dp[n])%1000000000)
#새로운 유형의 dp문제였다. 각 길이 별 끝나는 숫자의 갯수를 저장하고 그에따른 점화식을 세워 문제를 풀었다.
