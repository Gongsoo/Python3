
n = int(input())
words = []
for _ in range(n):
    words.append(input())
dic = {}
for word in words :
    s = len(word)-1
    for w in word :
        if w in dic :
            dic[w] += 10**s
        else :
            dic[w] = 10**s
        s-=1
dic = sorted(dic.values(), reverse = True)
answer, m = 0,9

for i in dic :
    answer += i * m
    m-=1
print(answer)