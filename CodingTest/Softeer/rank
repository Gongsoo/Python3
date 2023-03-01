import sys
input = sys.stdin.readline

n = int(input())
score = []
for _ in range(3) :
    score.append(list(map(int,input().strip('\n').split())))
score.append([sum(i) for i in zip(*score)])

for i in score :
    tmp = sorted(i,key = lambda x : -x)
    max_score = 1001
    dic = {}
    for n,t in enumerate(tmp) :
        if t in dic :
            continue
        else :
            dic[t] = n+1
    for j in i :
        print(dic[j],end=' ')
    print()
