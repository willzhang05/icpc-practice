from sys import stdin
n=input().split()
h=n[1]
l=n[2]
n=n[0]
hr=input().split()
d=dict()
for x in stdin:
    ln=input().split()
    if ln[0] not in d:
        d[ln[0]]=set([ln[1]])
    else:
        d[ln[0]].add(ln[1])
    if ln[1] not in d:
        d[ln[1]]=set([ln[0]])
    else:
        d[ln[1]].add(ln[0])
s=set()
us=set()
best=None
for m in hr:
    us.add(m)
while us.__len__() != 0:
    mv=us.pop()
    us.union=d[mv]
    
print(d)
    
