''' The Subarray XOR
https://www.codechef.com/JUNE222A/problems/XORK
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']

if DEBUG:
    from inspect import currentframe, getframeinfo
    from re import search

def debug(*args):
    if not DEBUG: return
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')

# for int dict key
from random import randrange
RAND = randrange(1 << 62)
def conv(x): return x ^ RAND

INF = float('inf')

# -----------------------------------------

BITS = 31

class Node:
    def __init__(self):
        self.children = [None, None]
        self.last = -INF

class BinaryTrie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, val, idx):
        cur = self.root
        for i in range(BITS-1, -1, -1):
            b = (val >> i) & 1
            if not cur.children[b]: cur.children[b] = Node()
            cur = cur.children[b]
            cur.last = idx
    
    def search(self, val, K):
        '''last idx s.t. (value at idx) ^ val >= K'''
        res = -INF
        cur = self.root
        for i in range(BITS-1, -1, -1):
            v = (val >> i) & 1
            k = (K >> i) & 1
            if k == 1: 
                cur = cur.children[v^1]
            else:
                if cur.children[v^1]: res = max(res, cur.children[v^1].last)
                cur = cur.children[v]
            if not cur: break 
            if i == 0: res = max(res, cur.last)
        return res


def solve(N, K, A):
    x = 0
    trie = BinaryTrie()
    trie.insert(0, -1)

    res = INF
    for i, a in enumerate(A):
        x ^= a 
        j = trie.search(x, K)
        if j > -INF: res = min(res, i - j)
        trie.insert(x, i)
    
    return res if res < INF else -1



def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(N, K, A)
        print(out)


if __name__ == '__main__':
    main()

