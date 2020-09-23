n=input()
s=input()
ls=len(s)
cb=dict()
for i0 in range(ls):
    for i1 in range(ls):
        if i1-i0 >= 3:
            sbs = s[i0:i1]
            if sbs in cb:
                cb[sbs]+=1
            else:
                cb[sbs]=1
sl=len(min(cb.keys(), key=len))
ss=[k for k in cb.keys() if len(k)==sl]
max_o=0
max_k=""
for k in ss:
    if max_o < cb[k]:
        max_o = cb[k]
        max_k = k
print(len(max_k))
