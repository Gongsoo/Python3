from collections import defaultdict
def check(n,m) :
    for i in range(2,5) :
        for j in range(2,5) :
            if n*i == m*j :
                return True
    return False
def solution(weights):
    answer = 0
    dic = defaultdict(int)
    for i in weights :
        dic[i] +=1
    for j in dic :
        for k in dic :
            if j==k :
                answer+=dic[j]*(dic[j]-1)
            elif check(j,k) :
                answer += dic[j]*dic[k]
    return answer//2
