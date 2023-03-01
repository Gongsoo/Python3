import sys
input = sys.stdin.readline

A, B = map(int,input().split())
m = int(input())
nums = list(map(int,input().split()))
nums.reverse()
post_num_to_10 = 0
for n, num in enumerate(nums) :
    post_num_to_10 += num*(A**n)

pre_num = []
while post_num_to_10 :
    post_num_to_10, mod = divmod(post_num_to_10,B)
    pre_num.append(mod)
pre_num.reverse()
for p in pre_num :
    print(p,end=' ')