import itertools
n=int(input())
l1=input()
l1=l1.split(' ')
l2=input()
l2=l2.split(' ')
p=itertools.permutations(l1)
found=False
for i in p:
    for e in l2:
        if e != i:
            
            break
    found=True
return 
