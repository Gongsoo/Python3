import sys
n = int(input())
a = [0] + [int(input()) for _ in range(n)]
dp = [[0 for _ in range(3)] for _ in range(n+1)]
dp[1] = [0,a[1],0]

for i in range(2,n+1) :
    dp[i][0] = max(dp[i-1])
    dp[i][1] = a[i] + dp[i-1][0]
    dp[i][2] = a[i] + dp[i-1][1]
print(max(dp[n]))

#아.. 1차원으로 푸려고 고집부리다가 시간만 잡아먹었따.. 고집을 부리지말자 영수야..
#dp[i]의 각 배열은 0 : i번째 포도주를 안마셨을때 1 : 연달아 한잔을 마셨을때 2 : 연달아 두잔을 마셨을때 각 경우의 i번째 포도주를 마셨을 때 최대값이다.
