import sys
n = int(input())
s = [0]+list(map(int,sys.stdin.readline().strip('\n').split(' ')))
dp = [1 for _ in range(n+1)]
for i in range(1,n+1) :
    for j in range(1,i) :
        if s[i] > s[j] :
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))

#i보다 작은 숫자범위 0~j 까지 loop하면서 i번째 숫자보다 작은 숫자들의 dp값중 최댓값에 1을 더해주는 식으로 문제를 풀이하였다.
