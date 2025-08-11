''' D. Max GEQ Sum
https://codeforces.com/contest/1691/problem/D
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

class SparseTableMin:
    def __init__(self, data, func=min):
        self.func = func
        self.data = data = [list(data)]
        i, n = 1, len(data[0])
        while 2 * i <= n:
            prev = data[-1]
            data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, l, r):
        '''func of data[l, r]; O(1)'''
        depth = (r - l + 1).bit_length() - 1
        return self.func(self.data[depth][l], self.data[depth][r - (1 << depth) + 1])


# let L[i] = max j < i s.t. A[j] > A[i], R[i] = min j > i s.t. A[j] > A[i]
# then A[i] is max ele of (l, r) where l in (L[i] + 1, i) and r in (i, R[i] - 1)
# (l, r) is bad if (l, i) is bad or (i, r) is bad
# (l, i) is bad if exist l < j < i s.t. sum(A[j..i]) > A[i]
# iff max_j sum(A[j..i]) > A[i]

# alternatively: (l, i) is bad if exist l < j < i s.t. sum(A[j..i]) > A[i]
# iff pref[j-1] < pref[i-1]
# iff L[i-1] on pref lies between l-1 and i-1

def is_bad(N, A):
    pref = [0] * (N + 1)
    left = [-1] * N
    for i, a in enumerate(A):
        pref[i + 1] = pref[i] + a
        left[i] = i - 1
        while left[i] != -1 and A[left[i]] <= a: left[i] = left[left[i]]

    rmq = SparseTableMin(pref, func=min)
    for i in range(1, N):
        if left[i] == i - 1: continue
        b = pref[i + 1] - rmq.query(left[i] + 1, i)
        if b > A[i]: return True
    
    return False


def solve(N, A):
    if is_bad(N, A): return 'NO'
    A.reverse()
    if is_bad(N, A): return 'NO'
    return 'YES'


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        print(out)


if __name__ == '__main__':
    main()

