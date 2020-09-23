p=int(input())
for i in range(p):
    l=input().split()
    k=int(l[0])
    m=int(l[1])
    init=[c for c in str(l[2])]
    creeper=False
    repeat=False
    visited=set()
    for x in range(m):
        init.extend(reversed(init))
        print(init)
        n=''.join(sorted(init))
        n.replace('0','')
        #print(n)
        print('.')
        if len(n) >= 8 and set([]):
            creeper=True
            break
        if n in visited:
            repeat=True
            break
        init=[c for c in n]   
        visited.add(n)
        
    out=''.join(init)
    if creeper:
        out = "C"
    if repeat:
        out = "R"
    #print(k, out, n)
        
        
    
    
