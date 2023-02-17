# 제출코드
n = int(input())
dp = [0]*(100001)
dp[1] = 1
dp[2] = 2
dp[3] = 3
sq = []
for i in range(4,n+1) :
    if int(i**0.5) == i**0.5 :
        dp[i] = 1
        sq.append(i)
        for j in range(i+i,n+1,i) :
            dp[j] = j//i
    else :
        for j in sq :
            if dp[i] == 0 :
                dp[i] = min(dp[i-1]+1,dp[j] + dp[i-j])
            else :
                dp[i] = min(dp[i],dp[j] + dp[i-j])
print(dp[n])

# 구상한것, 제곱수인지 확인한후 n+1항까지 제곱수의 배수를 먼저 dp list에 저장했다. 예를들면 i=4일때 dp[4] = 1 i = 8일때 dp[8] = 2 ... 근데 생각해보니 굳이 이렇게 안해도 될거같다.
# 그러고 제곱수를 sq list에 저장시켰다. 이것은 for loop과 break로 구현해도 될 것같다.
# sq의 원소들을 전부 확인하면서 제곱합의 최소를 구했다. 전부 확인하지 않으면 12 = 4+4+4 를 12 = 9 +1+1+1 로 찾는 경우가 생긴다.

# 정리
n = int(input())
dp = [i for i in range(0,n+1)]

for i in range(4,n+1) :
    for j in range(1,int(i**0.5)+1) :
        dp[i] = min(dp[i],dp[i-j**2]+1)
print(dp[n])
