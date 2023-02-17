#1707
import sys
from collections import deque
input = sys.stdin.readline
k = int(input())

for z in range(k) :
    max_node, n = map(int,input().split())
    g = [[] for _ in range(max_node+1)]
    visited = [False for _ in range(max_node+1)]
    for _ in range(n) :
        a,b = map(int,input().split())
        g[a].append(b)
        g[b].append(a)
    set1 = set()
    set2 = set()
    for x in range(1,max_node+1) :
        if not x in set1 :
            if not x in set2 :
                set1.add(x)
                visited[x] = True
                for i in g[x] :
                    if not visited[i] :
                        set2.add(i)
            else :
                set2.add(x)
                visited[x] = True
                for i in g[x] :
                    if not visited[i] :
                        set1.add(i)
        else :
            set2.add(x)
            visited[x] = True
            for i in g[x] :
                if not visited[i] :
                    set1.add(i)
    if set1 & set2 :
        print('NO')
    else :
        print('YES')
