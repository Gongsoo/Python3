import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int,input().split())
cards = list(map(int,input().split()))

blacks = list(combinations(cards,3))
ans = 0
for black in blacks :
    tmp = sum(black)
    if tmp > m :
        continue
    else :
        ans = max(ans,tmp)
print(ans)