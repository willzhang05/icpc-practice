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
    if i+1 < len(m) and i-1 >= 0 and c - m[i] >= 0:
        #print("hi " + str(m[i]), str(lc))
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
