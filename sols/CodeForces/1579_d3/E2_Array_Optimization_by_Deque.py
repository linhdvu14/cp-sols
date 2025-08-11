''' E2. Array Optimization by Deque
https://codeforces.com/contest/1579/problem/E2
'''

# ====================================================
# With fenwick OS tree
# ====================================================
class OsTree:
    def __init__(self, max_val=10**6):
        self.N = max_val
        self.tree = [0]*(self.N+1)  # tree[i] = count nodes with val i
        self.size = 0               # count inserted numbers

    def _cumsum(self, i):  # sum tree[1..i]
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)  # 110 -> 100
        return s

    def _add(self, i, val):  # add val to tree[i] (1-based)
        while i <= self.N:
            self.tree[i] += val
            i += i & (-i)  # 101 -> 110
    
    def insert(self, val):  # increment count of val 
        self._add(val, 1)
        self.size += 1
    
    def get_rank(self, val):  # how many numbers <= val
        return self._cumsum(val)


def solve_ostree(nums, N):
    val2idx = {v:i+1 for i,v in enumerate(sorted(list(set(nums))))}  # num -> sorted idx
    tree = OsTree(2*10**5)
    res = 0
    for num in nums:
        idx = val2idx[num] 
        smaller = tree.get_rank(idx-1)          # count strictly smaller
        bigger = tree.size - tree.get_rank(idx) # count strictly bigger
        res += min(smaller, bigger)
        tree.insert(idx)
    return res
 

# ====================================================
# With treap (TLE, can AC if split/merge iteratively)
# ====================================================
from random import randint

class Node:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority
        self.left = None
        self.right = None
        self.size = 1

class Treap:
    def __init__(self):
        self.root = None
    
    def _rand(self):
        return randint(1,2**32)
    
    # split subtree rooted here into 2 treaps: one < val, one >= val
    def split(self, root, val):
        if not root: return (None, None)
        if root.val < val:
            x, y = self.split(root.right, val)
            root.right = x
            root.size = 1
            if root.left: root.size += root.left.size
            if root.right: root.size += root.right.size
            return (root, y)
        else:
            x, y = self.split(root.left, val)
            root.left = y
            root.size = 1
            if root.left: root.size += root.left.size
            if root.right: root.size += root.right.size
            return (x, root)

    # merge 2 treaps into new treap, assuming x vals <= y vals
    def merge(self, x, y):
        if not x or not y: return x or y
        if x.priority > y.priority:  # make x root
            x.right = self.merge(x.right, y)
            x.size = 1
            if x.left: x.size += x.left.size
            if x.right: x.size += x.right.size
            return x
        else:
            y.left = self.merge(x, y.left)
            y.size = 1
            if y.left: y.size += y.left.size
            if y.right: y.size += y.right.size
            return y

    # split current tree, then merge 2 trees with new node
    def insert(self, val):
        y = Node(val, self._rand())
        x, z = self.split(self.root, val)
        self.root = self.merge(self.merge(x, y), z)
    

    # how many nodes < val and > val 
    def count(self, val):
        def count_smaller(node, val):
            res = 0
            while node:
                if node.val < val:
                    res += 1 + (node.left.size if node.left else 0)
                    node = node.right
                else:
                    node = node.left
            return res

        if not self.root: return 0, 0
        le = count_smaller(self.root, val)
        leq = count_smaller(self.root, val+1)
        return le, self.root.size - leq
        
def solve_treap(nums, N):  # tle
    res = 0
    treap = Treap()
    for num in nums:
        if treap.root is not None:
            small, big = treap.count(num)
            res += min(small, big)
        treap.insert(num)
    return res
 
# ====================================================
# test
# ====================================================

solve = solve_ostree

def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())
    for _ in range(T):
        N = int(stdin.readline().strip())
        nums = list(map(int, stdin.readline().strip().split()))
        out = solve(nums, N)
        print(out)

if __name__ == '__main__':
    main()
