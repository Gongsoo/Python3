from main import PrimeFinder
n = int(input())
a = PrimeFinder()
era = a.eratos(10**7)
i = 2
while n != 1 :
    if not era[i] :
        i+=1
        continue
    else :
        if not n%i :
            n //= i
            print(i)
        else :
            i+=1
            continue
