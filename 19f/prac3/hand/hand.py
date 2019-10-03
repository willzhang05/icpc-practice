#!/usr/bin/python3

def main():
    hand = input()
    cards = hand.split()
    occur = {}
    for c in cards:
        if c[0] in occur:
            occur[c[0]] += 1
        else:
            occur[c[0]] = 1
    max_o = 0
    max_card = 0
    for o in occur:
        if occur[o] > max_o:
            max_o = occur[o]
            max_card = o
            
        
    print(max_o)


if __name__ == "__main__":
    main();
