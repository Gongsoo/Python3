# () lv2
from collections import deque
def c(s) :
    s= deque(list(s))
    stack = []
    while s :
        tmp = s.popleft()
        if tmp == '(' :
            stack.append(tmp)
        else :
            if stack and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(tmp)
    return False if stack else True

def s(p) :
    for i in range(2,len(p)+1) :
        tmp = p[:i]
        if tmp.count('(') == tmp.count(')') :
            if i == len(p) :
                return p,''
            else :
                return p[:i],p[i:]

def n(p) :
    global answer
    if not p :
        return ''
    u,v = s(p)
    if not c(u) :
        answer+= '(' + n(v) + ')'
        for i in range(1,len(u)-1) :
            if u[i] == '(' :
                answer += ')'
            else :
                answer += '('
        return answer
    else :
        answer+= u + n(v)
        return answer
        
def solution(p):
    global answer
    answer = ''
    if c(p) :
        return p
    return n(p)

#skill tree lv2
def solution(skill, skill_trees):
    cnt = 0
    for tree in skill_trees :
        tmp = ''
        for i in tree :
            if i in skill :
                tmp+=i
        #print(tmp,tree,skill)
        for n in range(1,len(tmp)+1) :
            if skill[:n] in tmp[:n] :
                continue
            else :
                break
        else :
            #print(tmp,tree,skill)
            cnt+=1
    return cnt

# visit lv2
def solution(dirs):
    answer = 0
    dic = {'U': (0,1),'D': (0,-1), 'R': (1,0), 'L': (-1,0)}
    now = [0,0]
    visited = set()
    for i in dirs :
        nx, ny = now
        idx, idy = dic[i]
        x, y = nx+idx, ny+idy
        if x >5 or y >5 or x<-5 or y<-5 :
            now = nx, ny
            continue
        visited.add((nx,ny,x,y))
        visited.add((x,y,nx,ny))
        now = [x,y]
    #print(visited)
    #print(len(visited))
    
    
    return len(visited)//2

