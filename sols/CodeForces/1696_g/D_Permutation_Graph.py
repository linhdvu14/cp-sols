''' D. Permutation Graph
https://codeforces.com/contest/1696/problem/D
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

class SparseTable:
    def __init__(self, data):
        self.mn = [list(data)]
        i, n = 1, len(data)
        while 2 * i <= n:
            prev = self.mn[-1]
            self.mn.append([min(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

        self.mx = [list(data)]
        i, n = 1, len(data)
        while 2 * i <= n:
            prev = self.mx[-1]
            self.mx.append([max(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query_min(self, l, r):
        '''func of data[l, r]; O(1)'''
        depth = (r - l + 1).bit_length() - 1
        return min(self.mn[depth][l], self.mn[depth][r - (1 << depth) + 1])

    def query_max(self, l, r):
        '''func of data[l, r]; O(1)'''
        depth = (r - l + 1).bit_length() - 1
        return max(self.mx[depth][l], self.mx[depth][r - (1 << depth) + 1])

# greedily move forward farthest possible
# to go from l..r, need to break at min(l..r) and max(l..r)

def solve(N, A):
    lookup = {a: i for i, a in enumerate(A)}

    # next smaller and larger ele
    next_smaller = [-1] * N
    next_larger = [-1] * N
    for i in range(N-1, -1, -1):
        next_smaller[i] = next_larger[i] = i + 1
        while next_smaller[i] != N and A[next_smaller[i]] >= A[i]: next_smaller[i] = next_smaller[next_smaller[i]]
        while next_larger[i] != N and A[next_larger[i]] <= A[i]: next_larger[i] = next_larger[next_larger[i]]

    st = SparseTable(A)
    i = res = 0
    while i < N-1:
        if A[i] < A[i+1]:  # A[i] must be min
            j = next_smaller[i]
            mx = st.query_max(i, j-1)
            i = lookup[mx]
            res += 1
        else:  # A[i] must be max
            j = next_larger[i]
            mn = st.query_min(i, j-1)
            i = lookup[mn]
            res += 1

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        print(out)


if __name__ == '__main__':
    main()

