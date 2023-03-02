import sys
from itertools import permutations
input = sys.stdin.readline
n = int(input())
num = list(map(int,input().strip('\n').split()))
p = list(map(int,input().strip('\n').split()))
p_list = []
for i,j in zip(p,['+','-','*','%']) :
    for _ in range(i) :
        p_list.append(j)
result = []
p_lists = list(permutations(p_list,n-1))

for p_l in p_lists :
    tmp = num[0]
    for i,j in zip(num[1:],p_l) :

        if j == '+' :
            tmp +=i
        elif j == '-' :
            tmp -=i
        elif j=='*' :
            tmp *=i
        else :
            if tmp*i > 0 :
                tmp //= i
            else :
                tmp = abs(tmp)
                i = abs(i)
                b = tmp//i
                tmp = -b

    result.append(tmp)
print(max(result))
print(min(result))
#DFS
import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int,input().split()))
a,b,c,d = map(int,input().split())

max_num = -10**9+1
min_num = 10**9-1

def dfs(depth,result,plus,sub,mul,div) :
    global max_num, min_num
    if depth == n :
        max_num = max(max_num,result)
        min_num = min(min_num,result)
        return
    if plus :
        dfs(depth+1,result+num[depth],plus-1,sub,mul,div)
    if sub :
        dfs(depth+1, result - num[depth], plus, sub - 1, mul, div)
    if mul :
        dfs(depth+1, result * num[depth], plus, sub, mul - 1, div)
    if div :
        dfs(depth+1, int(result/num[depth]), plus, sub, mul, div - 1)
dfs(1,num[0],a,b,c,d)
print(max_num)
print(min_num)