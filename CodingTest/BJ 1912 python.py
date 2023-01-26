

import sys
n = int(input())
s = [0]+list(map(int,sys.stdin.readline().strip('\n').split(' ')))
dp = [0]*(n+1)
for i in range(1,n+1) :
    dp[i] = s[i]
    tmp = 0
    for j in range(i,0,-1) :
        tmp += s[j]
        dp[i] = max(dp[i],tmp)
print(max(dp[1:]))
# 첫번째 생각. i이전의 부분수열의 합을 전부 비교해 최댓값을 찾아보려 했으나, s의 길이가 100000이라 2중 for loop 사용하면 시간이 오래걸려 시간초과 발생.... 








import sys
n = int(input())
s = [0]+list(map(int,sys.stdin.readline().strip('\n').split(' ')))
dp = [0]*(n+1)
dp[1] = s[1]
for i in range(2,n+1) :
    dp[i] = max(dp[i-1]+s[i],s[i])

print(max(dp[1:]))
# 그냥 i바로 직전값을 사용해 최댓값을 구했다.
