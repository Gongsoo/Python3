import sys
input = sys.stdin.readline

n, m = map(int,input().split())
trees = list(map(int,input().split()))
upper = max(trees)
lower = 1
ans = 0
while True :
    if upper < lower :
        break
    middle = (upper+lower)//2
    tmp = 0
    for tree in trees :
        if tree >= middle :
            tmp += tree - middle
        if tmp >= m :
            break
    if tmp >= m :
        lower = middle + 1
    else :
        upper = middle - 1

print(upper)