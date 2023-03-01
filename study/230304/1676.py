n = int(input())
num = 0
while n >=5 :
    n,m = divmod(n,5)
    num+=n
print(num)