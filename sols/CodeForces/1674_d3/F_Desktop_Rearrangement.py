''' F. Desktop Rearrangement
https://codeforces.com/contest/1674/problem/F
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

    def add(self, i, x):
        '''point update data[i] += x'''
        while i < len(self.val):
            self.val[i] += x
            i |= i + 1   # 101 -> 110

def main():
    R, C, Q = list(map(int, input().split()))

    # flatten by cols
    grid = [input().decode().strip() for _ in range(R)]
    A = [0] * R * C
    cnt = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '*':
                A[c * R + r] = 1
                cnt += 1

    fw = FenwickTree(A)
    res = [-1] * Q
    for q in range(Q):
        r, c = list(map(int, input().split()))
        i = (c-1)*R + r-1
        if A[i] == 0:
            A[i] = 1
            cnt += 1
            fw.add(i, 1)
        else:
            A[i] = 0
            cnt -= 1
            fw.add(i, -1)
        res[q] = cnt - fw.query(cnt-1)

    print(*res, sep='\n')


if __name__ == '__main__':
    main()

