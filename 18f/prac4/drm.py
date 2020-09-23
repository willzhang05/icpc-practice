m=input()
mi=int(len(m)/2)
m1=m[:mi]
m2=m[mi:]
s1=sum([ord(c)-65 for c in m1])%26      
s2=sum([ord(c)-65 for c in m2])%26
n1=''.join([chr((ord(c)-65+s1)%26+65) for c in m1])
n2=''.join([chr((ord(c)-65+s2)%26+65) for c in m2])
o=''.join([chr((ord(n1[i])-65+ord(n2[i])-65)%26+65) for i in range(len(n1))])
print(o)
