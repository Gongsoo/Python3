import sys
input = sys.stdin.readline
N = int(input())

for _ in range(N) :
    n = int(input())
    m = int(input())
    floors = [[]for f in range(n+1)]
    floor = 0
    while floor != n+1 :
        if floor == 0:
            for i in range(m) :
                floors[floor].append(i+1)
        else :
            for i in range(m) :
                floors[floor].append(sum(floors[floor-1][:i+1]))
        floor +=1
    print(floors[n][m-1])
