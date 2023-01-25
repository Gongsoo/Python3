import math

n, k = map(int,input().split(' '))
a = math.factorial(n+k-1)
b = math.factorial(k-1)
c = math.factorial(n)
print(a//(b*c)%1000000000)

# 보자마자 생각난 것은 중복조합. 고등학생때 많이 푼 기억이 있다. 



n, k = map(int,input().split(' '))
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
dp[0][0] = 1
for i in range(n+1) :
    for j in range(1, k+1) :
        dp[i][j] = dp[i-1][j] +dp[i][j-1]
print(dp[n][k]%1000000000)
# DP로 푼 코드. dp[n-1][k] = dp[0][k-1] + dp[1][k-1] + ... + dp[n-1][k-1]
