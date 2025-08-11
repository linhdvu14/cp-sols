''' DMOPC '22 Contest 2 P2 - Line Trace
https://dmoj.ca/problem/dmopc22c2p2
'''

import os, sys
input = sys.stdin.readline  # strip() if str

def debug(*args):   
    if os.environ.get('debug') in [None, '0']: return
    from inspect import currentframe, getframeinfo
    from re import search
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')

INF = float('inf')

# -----------------------------------------

class FenwickTree:
    '''basic 0-base sum Fenwick tree for point update, range query'''
    def __init__(self, data):
        '''transform list into BIT'''
        self.val = data[:]
        for i in range(len(self.val)):
            j = i | (i + 1)
            if j < len(self.val):
                self.val[j] += self.val[i]
    
    def add(self, i, x):
        '''point update data[i] += x'''
        while i < len(self.val):
            self.val[i] += x
            i |= i + 1   # 101 -> 111
    
    def query(self, i):
        '''prefix sum data[0..i]'''
        s = 0
        i += 1
        while i:
            s += self.val[i - 1]
            i &= i - 1  # 110 -> 100
        return s

    def query_range(self, l, r):
        '''range sum data[l..r]'''
        return self.query(r) - self.query(l-1)

# A[e] = s --> if start at column s, end at column e
# count inversions
def main():
    N = int(input())
    A = list(map(int, input().split()))

    if len(A) != len(set(A)): return -1

    fw = FenwickTree([0] * (N + 2))
    res = 0
    for a in A:
        res += fw.query_range(a + 1, N + 1)
        fw.add(a, 1)
    
    return res


if __name__ == '__main__':
    res = main()
    print(res)

