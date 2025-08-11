''' Problem A2: Perfectly Balanced - Chapter 2
https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-2/problems/A2
'''

import os, sys
input = sys.stdin.readline
output = sys.stdout.write

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

import random
random.seed(123)

HASH = [random.randrange(1 << 62) for _ in range(10**6 + 1)]
HASH_SET = set(HASH)

class FenwickTree:
    '''basic 0-base sum Fenwick tree for point update, range query'''
    def __init__(self, data):
        '''transform list into BIT'''
        self.val = data[:]
        for i in range(len(self.val)):
            j = i | (i + 1)
            if j < len(self.val):
                self.val[j] += self.val[i]

    def query(self, i):
        '''prefix sum data[0..i]'''
        s = 0
        end = i + 1
        while end:
            s += self.val[end - 1]
            end &= end - 1  # 110 -> 100
        return s
    
    def query_range(self, l, r):
        '''range sum data[l..r]'''
        return self.query(r) - self.query(l-1)

    def add(self, i, x):
        '''point update data[i] += x'''
        while i < len(self.val):
            self.val[i] += x
            i |= i + 1   # 101 -> 110


# WA: 1 32-bit hash
# AC:
# - 2 32-bit hashes
# - 1 32-bit hash + check that missing value appears in range
# - 1 64-bit hash

def solve(N, A, Q, queries):
    fw = FenwickTree([HASH[a] for a in A])
    
    def is_ok(l, r):
        if (r - l + 1) % 2 == 0: return False
        l -= 1; r -= 1
        m = (l + r) // 2

        if fw.query_range(l, m) - fw.query_range(m + 1, r) in HASH_SET: return True
        if fw.query_range(m, r) - fw.query_range(l, m - 1) in HASH_SET: return True
        return False

    res = 0
    for t, x, y in queries:
        if t == 1:
            x -= 1
            fw.add(x, HASH[y] - HASH[A[x]])
            A[x] = y
        elif is_ok(x, y):
            res += 1

    return res


def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        Q = int(input())
        queries = [list(map(int, input().split())) for _ in range(Q)]
        res = solve(N, A, Q, queries)
        print(f'Case #{t+1}: {res}')


if __name__ == '__main__':
    main()

