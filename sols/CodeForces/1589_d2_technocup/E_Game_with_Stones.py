''' E. Game with Stones
https://codeforces.com/contest/1589/problem/E
'''

import io, os, sys
from math import e
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write


from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc


import random
random.seed(123)

class Node:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority
        self.count = 1
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f'Node(val={self.val}, count={self.count})'


class Treap:
    '''Multiset treap, all nodes hold unique values'''
    def __init__(self):
        self.root = None
        self.size = 0
    
    def _rand(self):
        return random.randint(1,2**32)
    
    def find(self, val):
        '''find node holding val'''
        node = self.root
        while node:
            if node.val == val: break
            node = node.left if node.val > val else node.right
        return node

    @bootstrap
    def split(self, root, val):
        '''split subtree rooted here into 2 treaps: one < val, one >= val'''
        if not root: yield (None, None)
        if root.val < val:
            x, y = yield self.split(root.right, val)
            root.right = x
            yield (root, y)
        else:
            x, y = yield self.split(root.left, val)
            root.left = y
            yield (x, root)

    @bootstrap
    def merge(self, x, y):
        '''merge 2 treaps into new treap, assuming x vals <= y vals'''
        if not x or not y: yield x or y
        if x.priority > y.priority:  # make x root
            x.right = yield self.merge(x.right, y)
            yield x
        else:
            y.left = yield self.merge(x, y.left)
            yield y
 
    def insert(self, val):
        '''split current tree, then merge 2 trees with new node'''
        node = self.find(val)
        if node is not None:
            node.count += 1
        else:
            y = Node(val, self._rand())
            x, z = self.split(self.root, val)
            self.root = self.merge(self.merge(x, y), z)
        self.size += 1
    
    def delete(self, val, del_all=False):
        '''delete node with val, assuming int val'''
        node = self.find(val)
        if not node: return
        if not del_all and node.count > 1:
            node.count -= 1
            self.size -= 1
        else:  # remove entire node
            x, y = self.split(self.root, val)
            y, z = self.split(y, val+1)
            self.root = self.merge(x, z)
            self.size -= node.count
    
    def get_min(self):
        '''get min value'''
        node = self.root
        while node.left:
            node = node.left
        return node.val
 
    def get_max(self):
        '''get max value'''
        node = self.root
        while node.right:
            node = node.right
        return node.val
    
    def get_count(self, val):
        '''get num nodes with val'''
        node = self.find(val)
        return 0 if not node else node.count


# let S(l, r) = a[r] - a[r-1] + a[r-2] - ... + (-1)^(r-l) * a[l]
# then a[l..r] is winning if S(l, m) >= 0 and S(l, r) == 0 for m=l..r
 
# iterate i=1..N and track set of valid prefixes / potential segment starts
# * add S(1, i) to prefix set
# * remove all prefixes S(1, l) s.t. S(l, r) < 0; note S(l, r) = S(r, 1) - (-1)^(r-l) * S(l-1, 1)
# -> if S(1, l) remains, then S(i, l) >= 0 for i=l+1..r
# * num winning segments ending at r is num l s.t. S(l, r) == 0
 
def solve_treap(N, nums):
    # set of valid prefixes with even/odd length
    pref = [Treap(), Treap()]
    pref[0].insert(0)
 
    # running prefix
    res = p = 0
    for i, num in enumerate(nums):
        p = num - p
        sign, rsign = (i+1) % 2, i % 2
 
        # remove invalid prefixes
        while pref[sign].size > 0:
            mx = pref[sign].get_max()
            if p - mx >= 0: break
            pref[sign].delete(mx, del_all=True)
        while pref[rsign].size > 0:
            mn = pref[rsign].get_min()
            if p + mn >= 0: break
            pref[rsign].delete(mn, del_all=True)
 
        # num winning segs ending at i
        res += pref[sign].get_count(p)
        res += pref[rsign].get_count(-p)
 
        # add current sum
        pref[sign].insert(p)
 
    return res


from collections import deque

def solve_deque(N, nums):
    dq1, dq2 = deque([[0, 1]]), deque()  # (pref, count)
    res = p = 0
    for num in nums:
        p = num - p

        # remove invalid prefixes
        while dq1 and p - dq1[-1][0] < 0:
            dq1.pop()
        while dq2 and p + dq2[0][0] < 0:
            dq2.popleft()

        # num winning segs ending at i
        if dq1 and p - dq1[-1][0] == 0:
            res += dq1[-1][1]
        if dq2 and p + dq2[0][0] == 0:
            res += dq2[0][1]

        # add current sum
        # note p >= all remaining vals in dq1
        # so dq1 and dq2 are both increasing deque
        if dq1 and dq1[-1][0] == p:
            dq1[-1][1] += 1
        else:
            dq1.append([p, 1])

        dq1, dq2 = dq2, dq1

    return res


solve = solve_deque

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        nums = list(map(int, input().split()))
        out = solve(N, nums)
        output(f'{out}\n')

if __name__ == '__main__':
    main()

