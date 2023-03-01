import sys
from main import PrimeFinder
'''
a = PrimeFinder()
t1 = time.time()
print(a.eratos(10**5),time.time()-t1)#0.0138
t1 = time.time()
print(a.loop(10**5),time.time()-t1)#26.4349
t1 = time.time()
print(a.improved_loop(10**5),time.time()-t1)#0.1649
'''
input = sys.stdin.readline

n = int(input())
num_list = list(map(int,input().split()))
num_prime = 0
a = PrimeFinder()
era = a.eratos(1000)
for i in num_list :
    if era[i]:
        num_prime +=1
print(num_prime)
