#!/usr/bin/python3

def main():
    nums = input().split()
    n = int(nums[0])
    m = int(nums[1])
    seen = input()
    #seen_codes = list(map(lambda x: ord(x) - 97, seen))
    ctext = input()
    ctext_codes = list(map(lambda x: ord(x) - 97, ctext))
    #find key first
    decrypt = seen
    i = n - 1
    j = m - n
    while len(decrypt) < m:
        a = ord(decrypt[0]) - 97
        b = ctext_codes[j]
        #print("a", chr(97 + a))
        #print("b", chr(97 + b))
        p = 0
        value = 0
        possible = list()
        while True:
            value = b+26*p-a
            if value >= 26:
                break
            if value < 26 and value >= 0:
               possible.append(chr(97 + value))
               decrypt = ''.join((str(chr(97 + value)),decrypt))
            p += 1

        print(possible)
        #print(list(map(lambda x: ord(x) - 97, possible)))
        i -= 1
        j -= 1
    print(decrypt)
        

if __name__ == "__main__":
    main();
