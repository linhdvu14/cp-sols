''' D. New Year Concert
https://codeforces.com/contest/1632/problem/D
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

def gcd(a, b):
    '''assume a, b >= 0'''
    if a < b: a, b = b, a
    while b > 0: a, b = b, a % b
    return a


class SparseTable:
    def __init__(self, data, func=gcd):
        self.func = func
        self.data = data = [list(data)]
        i, n = 1, len(data[0])
        while 2 * i <= n:
            prev = data[-1]
            data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, left, right):
        '''func of data[left, right)'''
        depth = (right - left).bit_length() - 1
        return self.func(self.data[depth][left], self.data[depth][right - (1 << depth)])

    def __getitem__(self, idx):
        return self.data[0][idx]


# iterate over prefixes
# if adding index j makes some (i, j) bad, set j to big prime
# then all intervals containing j are good
# then only need to consider intervals starting from j+1

def solve(N, A):
    res = []
    cur = i = 0
    lookup = SparseTable(A)
    for j in range(N):
        # find k s.t. i <= k <= j, gcd(k..j) == j - k + 1
        k, lo, hi = -1, i, j
        while lo <= hi:
            mi = (lo + hi) // 2
            g = lookup.query(mi, j+1)
            if g == j - mi + 1:
                k = mi
                break
            elif g > j - mi + 1:
                hi = mi - 1
            else:
                lo = mi + 1
        if k > -1:
            cur += 1
            i = j + 1
        res.append(cur)

    return res


def main():
    N = int(input())
    A = list(map(int, input().split()))
    out = solve(N, A)
    print(*out)


if __name__ == '__main__':
    main()

