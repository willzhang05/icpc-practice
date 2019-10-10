#!/usr/bin/python3

def main():
    nums = input().split()
    n = int(nums[0])
    m = int(nums[1])
    seen = input()
    ctext = input()
    ctext_codes = list(map(lambda x: ord(x) - 97, ctext))
    decrypt = [' ']*m
    for i in range(n):
        decrypt[m - n + i] = seen[i];
    i = m - n - 1
    while i >= 0:
        b = ctext_codes[i + n]
        a = ord(decrypt[i + n]) - 97
        k = (b-a + 26) % 26
        decrypt[i] = chr(k + 97)
        i -= 1

    print(''.join(decrypt))
        

if __name__ == "__main__":
    main();
