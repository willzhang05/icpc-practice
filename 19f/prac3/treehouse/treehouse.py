#!/usr/bin/python3
import sys
import heapq


class TreeHouse:
    def __init__(self, uid, x, y):
        self.id = uid
        self.x = x
        self.y = y
        self.adj = set()
        self.val = sys.maxsize

    def __lt__(self, other):
        return self.val < other.val 

    def __eq__(self, other):
        return self.id == other.id

    def __gt__(self, other):
        return self.val > other.val

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    def __hash__(self):
        return hash("(" + str(self.x) + ", " + str(self.y) + ") " + str(self.adj) + " " + str(self.val))
        
def main():
    params = input()
    params_split = params.split()
    n = int(params_split[0])
    e = int(params_split[1])
    p = int(params_split[2])
    thouses = list()
    for i in range(n):
        thouse = input()
        coords = list(map(float, thouse.split()))
        thouses.append(TreeHouse(i, coords[0], coords[1]))
    mstset = set()
    heapq.heapify(thouses)
    for i in range(p):
        cable = input()
        between = list(map(int, cable.split()))
        thouses[between[0]].adj.add(between[1])
        thouses[between[1]].adj.add(between[0])
        mstset.add(thouses[between[0]])
        mstset.add(thouses[between[1]])
    print(mstset)
    while len(mstset) < n:
        u = heapq.heappop(thouses)
        mstset.add(u)
        for a in u.adj:
            graph[a
            
            

        


if __name__ == "__main__":
    main();
