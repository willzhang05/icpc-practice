p=int(input())
for i in range(p):
    l=input().split()
    k=l[0]
    n=int(l[1])
    s1=int(n*(1+n)/2)
    s2=int(n*(1+(n*2)-1)/2)
    s3=int(n*(2+(n*2))/2)
    print(k,s1,s2,s3)
