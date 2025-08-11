''' D. Optimal Partition
https://codeforces.com/contest/1668/problem/D
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

class FenwickTreeMax:
    '''basic 0-base max Fenwick tree for point update, range query'''
    def __init__(self, data):
        '''transform list into BIT'''
        self.val = data[:]
        for i in range(len(self.val)):
            j = i | (i + 1)
            if j < len(self.val):
                self.val[j] = max(self.val[j], self.val[i])

    def query(self, i):
        '''prefix max data[0..i]'''
        s = -INF
        end = i + 1
        while end:
            s = max(s, self.val[end - 1])
            end &= end - 1  # 110 -> 100
        return s

    def update(self, i, x):
        '''point update data[i] = x; require x >= desired value'''
        while i < len(self.val):
            self.val[i] = max(self.val[i], x)
            i |= i + 1   # 101 -> 110


# optimal to only have 0-sum and neg-sum subarray with length 1
# dp[r] = optimal sum for A[0..r]
#       = max( dp[r-1] + sign(A[r]), 
#              max (dp[l] - l + 1) + r  over all l s.t. pref[l] < pref[r]
#         )
def solve(N, A):
    # fw.query(p) = dp[l] - l + 1 over all pref[l] < p
    idx = [0]
    for a in A: idx.append(idx[-1] + a)
    idx = sorted(list(set(idx)))
    idx = {p: i+1 for i, p in enumerate(idx)}
    idx[-INF] = 0
    fw = FenwickTreeMax([-INF] * len(idx))

    # find max partition of 0..i
    dp = [-INF] * (N + 1)
    dp[0] = 0
    p = 0
    fw.update(idx[p], 1)
    for r, a in enumerate(A):
        p += a
        dp[r+1] = max(
            dp[r] + (1 if a > 0 else 0 if a == 0 else -1),
            fw.query(idx[p] - 1) + r,
        )
        fw.update(idx[p], dp[r+1] - r)

    return dp[-1]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        print(out)


if __name__ == '__main__':
    main()

