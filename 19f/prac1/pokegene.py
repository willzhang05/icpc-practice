#!/usr/bin/python3

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.children = []

def helperSearch(root: 'TreeNode', target: 'TreeNode', currentPath):
    if root == None:
        return None
    
    if root.val == target.val:
        return currentPath
    
    l = helperSearch(root.left, target, currentPath + 'l')
    r = helperSearch(root.right, target, currentPath + 'r')
    
    if l != None:
        return l
    
    if r != None:
        return r
    
    return None
    

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #search tree for both nodes
        #creating a string like llrrlr
        #then if the strings have the same chars
        #it will have a common ancestor
        l = helperSearch(root,p,"")
        r = helperSearch(root,q,"")
        print(l,r)
        i=0
        while (i < len(l) and i < len(r) and l[i] == r[i] ):
            if l[i] == "l":
                root = root.left
            else:
                root = root.right
            i+=1
            
        return root

def main():
    nq = input()
    nq = nq.split()
    n = int(nq[0])
    q = int(nq[1])
    print(n)
    print(q)
    root = TreeNode(None)
    for i in range(n):
        gene = input()
        for c in gene:
            if len(root.children) == 0:
                root.children.append(TreeNode(c))

        print(gene)
        


if __name__ == "__main__":
    main();
