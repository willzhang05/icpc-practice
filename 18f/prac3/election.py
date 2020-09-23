import math
def nCr(n,r):
    f=math.factorial
    return f(n)/(f(r)*f(n-r))

t=int(input())
for i in range(t):
    nums=input().split()
    n=int(nums[0])
    v1=int(nums[1])
    v2=int(nums[2])
    w=float(nums[3])*.01
    print(nums)
    print(w)
    m=v1+v2
    #votes=v1+((n-m)*.5)
    if v1 >= int(n/2):
        print("GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!")
        continue
    #print(n-m)
    #prob=nCr(n-m,k)*((0.5)**k)*(0.5**(n-m-k))
    for t in range(m, n):#int(n/2)-v1):
        k=(n-m)-int((n-m)/2)
        print(k)
        prob += nCr(n-m,k)*(0.5**k)*(0.5**(n-m-k))
    print(prob)
    if prob > float(w):
        print("GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!")
    elif prob == float(w):
        print("PATIENCE, EVERYONE!")
    else:
        print("RECOUNT!")
        
