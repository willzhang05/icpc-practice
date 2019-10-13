#!/usr/bin/python3

def calc_res(div1, div2):
    ares = div1[0]
    for a in range(1, len(div1)):
        ares |= div1[a]
    bres = div2[0]
    for b in range(1, len(div2)):
        bres |= div2[b]

    return ares & bres

def get_mask(circle):
    max_val = max(circle)
    msb = max_val
    pos = 0
    while (msb != 0x01):
        msb >>= 1
        pos += 1
    msb <<= pos
    #print("%x" % msb)
    return (2**pos, msb)

def print_have_msb(have_msb):
    new_list = [c[1] for c in have_msb]
    print(new_list)


def main():
    n,k = tuple(map(int, input().split()))
    print("k: ", k)
    print("n: ", n)
    circle = list(map(int, input().split()))
    print("circle: ", circle)
    
    place,mask = get_mask(circle)
    dividers = list()
    while mask > 0:
        have_msb = list()
        for j in range(len(circle)):
            if circle[j] & mask:
                have_msb.append(tuple((j, circle[j])))
        if len(have_msb) < k:
            print("dont care ", place, ": ", have_msb)
            place -= 2
            mask >>= 1
            continue
        elif len(have_msb) == k:
            print(place, "values: ", [c[1] for c in have_msb])
            print(" indices: ", [c[0] for c in have_msb])
            place -= 2
            mask >>= 1
        else:
            
            place -= 2
            mask >>= 1
                

if __name__ == "__main__":
    main();
