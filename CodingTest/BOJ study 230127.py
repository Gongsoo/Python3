#11722
n = int(input())
s = [0]+list(map(int,input().split(' ')))
dp = [1 for _ in range(n+1)]

for i in range(1,n+1) :
    for j in range(1,i+1) :
        if s[i] < s[j] :
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))

#11054
n = int(input())
s = [0]+list(map(int,input().split(' ')))
dp = [1 for _ in range(n+1)]
dp1 = [1 for _ in range(n+1)]
for i in range(1,n+1) :
    for j in range(1,i+1) :
        if s[i] > s[j] :
            dp[i] = max(dp[i],dp[j]+1)
for i in range(n,0,-1) :
    for j in range(n,i-1,-1) :
        if s[i] > s[j] :
            dp1[i] = max(dp1[i],dp1[j]+1)

for i in range(1,n+1) :
    dp[i] = dp[i]+dp1[i]-1
print(max(dp))

#13398
N = int(input())
a = list(map(int, input().split()))
dp = [[0] * N for _ in range(2)]
dp[0][0] = a[0]
dp[1][0] = -1000
for i in range(1, N):
    dp[0][i] = max(dp[0][i - 1] + a[i], a[i])
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + a[i])
print(max(max(dp[0]), max(dp[1])))

#2133
n = int(input())
dp = [0 for _ in range(31)]
dp[0] = 1
dp[2] = 3

for i in range(4,31,2) :
    dp[i] = dp[i-2]*3
    for j in range(4,i+1,2) :
        dp[i] +=dp[i-j]*2
print(dp[n])

#14852
n = int(input())
dp = [1 for _ in range(n+2)]
dp[1]=2
dp[2]=7
for i in range(3,n+1) :
    dp[i] = (dp[i-1]*3 + dp[i-2] - dp[i-3])%1000000007
print(dp[n]%1000000007)
