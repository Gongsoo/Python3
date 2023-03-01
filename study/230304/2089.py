n = int(input())
if not n :
    print('0')
    exit(0)
bi = ''
while n != 0 :

    tmp = n%-2
    if tmp == -1 :
        bi += '1'
        n = n//-2 + 1
    else :
        bi += str(tmp)
        n = n//-2
print(bi[::-1])