# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        s = {}

        while p != None:
            s[p.val] = p
            p = p.parent

        while q != None:
            if q.val in s:
                return q
            q = q.parent

# After watching a youtube explanation:
class Solution2:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pPtr = p
        qPtr = q

        while pPtr.val != qPtr.val:
            pPtr = q if pPtr == None else pPtr.parent
            qPtr = p if qPtr == None else qPtr.parent

        return pPtr