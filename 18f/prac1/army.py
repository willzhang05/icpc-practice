import math
ls = []
n = input()
bts = int(n)
for b in range(bts*4):
    n = input()
    ls.append(n)
l = 0
while l<len(ls): 
    nums = ls[l+1].split(' ')
    g = nums[0]
    m = nums[1]
    g_m = max(ls[l+2].split(' '))
    m_m = max(ls[l+3].split(' '))
    l+=4
    if g_m == 0 and m_m == 0:
        print("uncertain")
    if g_m >= m_m:
        print("Godzilla")
    else:
        print("MechaGodzilla")
