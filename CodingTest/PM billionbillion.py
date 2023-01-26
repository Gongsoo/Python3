from collections import defaultdict

'''
def prime(n) :
    era = [True] * (n+1)
    era[0],era[1] = False, False
    prime = []
    for i,j in enumerate(era) :
        if j :
            for k in range(i+i,len(era),i) :
                era[k] = False
            prime.append(i)
    return prime


def count(e) :
    
    dic = defaultdict(int)
    cnt = 0
    while n!=1 :
        if n%p[cnt] == 0 :
            n //= p[cnt]
            dic[p[cnt]] +=1
        else:
            cnt+=1
    num = 1
    for i in dic :
        num = num*(dic[i]+1)
    return num
'''
#first i tried 소인수분해 with prime, but it took a lot of time. i need another method. 

def solution(e, starts):
    answer = []
    cnt = []
    divisor=[0 for i in range(e+1)]
    for i in range(2,e+1):
        for j in range(1,min(e//i+1,i)):
            divisor[i*j]+=2
    for i in range(1,int(e**(1/2))+1):
        divisor[i**2]+=1
    '''
    data = [1] * (e+1)
    
    for i in range(2,e+1) :
        for j in range(i,e+1,i) :
            data[j] +=1
    '''
    # This is the best method of 소인수분해 i think.
    
    
    tmp = 0
    for i in range(1,e+1) :
        if tmp >= i :
            cnt.append(tmp)
        else :
            tmp = divisor[i:].index(max(divisor[i:]))+i
            cnt.append(tmp)
            
    '''
    arr = [0]*(e+1)
    max_val = data[-1]
    idx = len(data)-1
    for i in reversed(range(0,e)) :
        if data[i] >= max_val :
            idx = i
            max_val = data[i]
        arr[i] = idx
    '''
    This algorithm don't require 'index' 
    
    for i in starts :
        answer.append(cnt[i-1])
    return answer
