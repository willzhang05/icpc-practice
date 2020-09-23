import math
pos=input().split()
pos=[float(t) for t in pos]
first_times=input().split()[1:]
second_times=input().split()[1:]
if pos[0] > pos[1]:
    temp=pos[0]
    pos[0]=pos[1]
    pos[1]=temp
    temp=first_times
    first_times=second_times
    second_times=temp
    
fs_times=set([int(first_times[t]) for t in range(0, len(first_times), 2)])
ss_times=set([int(second_times[t]) for t in range(0, len(second_times), 2)])
fst_times=set([int(first_times[t]) for t in range(1, len(first_times), 2)])
sst_times=set([int(second_times[t]) for t in range(1, len(second_times), 2)])
#print(fs_times)
#print(ss_times)
#print(fst_times)
#print(sst_times)
#print('-')
time=0
incr_first=False
incr_second=False
while time < 10e5:
    #print(pos,time)
    if incr_first:
        pos[0]+=1
    if incr_second:
        pos[1]+=1
    if time in fs_times:
        incr_first=True
    if time in ss_times:
        incr_second=True
    if time in fst_times:
        incr_first=False
    if time in sst_times:
        incr_second=False
    if pos[0]+4.4 > pos[1]:
        print("bumper tap at time " + str(time))
        exit(0)
    time += 1
print("safe and sound")       
