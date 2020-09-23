from sys import stdin
h=[]
o=[]
for x in stdin:
    l=x.strip()
    if l=='#':
        if len(h) <= 2:
            i=-1
        else:
            if len(h)%2==0:
                i=int(len(h)/2)
            else:
                i=int((len(h)+1)/2)-1
        #print(str(h) + "sending")
        print(h[i])
        del h[i]
    else:
        if len(h) == 0:
            h.append(int(l))
        elif int(l) >= h[-1] :
            h.append(int(l))
        else:
            a=0
            while a < len(h) and int(l) > h[a]:
                a+=1
            h.insert(a,int(l))
        #print("adding " + l)
        #print(h)
