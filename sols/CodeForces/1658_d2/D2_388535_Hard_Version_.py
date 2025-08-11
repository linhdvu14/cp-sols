''' D2. 388535 (Hard Version)
https://codeforces.com/contest/1658/problem/D2
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


INF = float('inf')

# -----------------------------------------

BITS = 18

class TrieNode:
    def __init__(self):
        self.child = [None, None]
    
    def add(self, x):
        '''add val x to trie'''
        cur = self
        for j in range(BITS-1, -1, -1):
            d = (x >> j) & 1
            if cur.child[d] is None: cur.child[d] = TrieNode()
            cur = cur.child[d]
    
    def min_xor(self, x):
        '''find min(x^a) over all a in trie'''
        cur = self
        res = 0
        for j in range(BITS-1, -1, -1):
            d = (x >> j) & 1
            if cur.child[d] is None: d ^= 1
            res |= d << j
            cur = cur.child[d]
        return res ^ x
            
    def max_xor(self, x):
        '''find max(x^a) over all a in trie'''
        cur = self
        res = 0
        for j in range(BITS-1, -1, -1):
            d = ((x >> j) & 1) ^ 1
            if cur.child[d] is None: d ^= 1
            res |= d << j
            cur = cur.child[d]
        return res ^ x


# x = a^l for some a in A
# found correct x when min(x^a) == l and max(x^a) == r
# try x = a^l for all a in A, check in O(log N) with binary trie

def solve(L, R, A):
    if (R - L + 1) % 2 == 1:
        res = 0
        for i, a in enumerate(A):
            res ^= a
            res ^= i + L
        return res

    trie = TrieNode()
    for a in A: trie.add(a)

    for a in A:
        x = L ^ a
        mn = trie.min_xor(x)
        mx = trie.max_xor(x)
        if mn == L and mx == R: return x

    return -1



def main():
    T = int(input())
    for _ in range(T):
        L, R = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(L, R, A)
        print(out)


if __name__ == '__main__':
    main()

