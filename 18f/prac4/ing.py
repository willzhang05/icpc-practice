n=input().split()
h=int(n[0])
c=int(n[1])
m=[int(c) for c in input().split()]
#print(m)
t=0
i=0
lc=c
while i < len(m):
    #print("cal " + str(c))
    #print(m[i], c)
    mi=min(m[i],c)
    #print("eat " + str(mi))
    x=1
    while i+x < len(m) and i-x >= 0 and  < m[i-x]:
        #print("hi " + str(m[i]), str(lc))
        x+=1

    i+=x

        c=lc
        t+=lc
        i+=2
        continue
   
    t+=mi
    c=int(c*(2/3))
    lc=c
    #print('total '+str(t))
    i+=1
print(t)
