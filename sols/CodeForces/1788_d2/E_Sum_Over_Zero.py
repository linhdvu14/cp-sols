''' E. Sum Over Zero
https://codeforces.com/contest/1788/problem/E
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
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
from bisect import bisect_right
from itertools import accumulate


class FenwickTreeMax:
    '''basic 0-base max Fenwick tree for point update, range query'''
    def __init__(self, data):
        '''transform list into BIT'''
        self.val = data[:]
        self.tree = data[:]
        for i in range(len(self.tree)):
            j = i | (i + 1)
            if j < len(self.tree):
                self.tree[j] = max(self.tree[j], self.tree[i])

    def query(self, i):
        '''prefix max data[0..i]'''
        s = -INF
        end = i + 1
        while end:
            s = max(s, self.tree[end - 1])
            end &= end - 1
        return s

    def update(self, i, x):
        '''point update data[i] = x; require x >= desired value'''
        if self.val[i] >= x: return 
        self.val[i] = x
        while i < len(self.tree):
            self.tree[i] = max(self.tree[i], x)
            i |= i + 1


def solve(N, A):
    ps = [0] * (N + 1)
    for i, a in enumerate(A): ps[i + 1] = ps[i] + a
    ps_vals = sorted(list(set(ps)))
    mp = {a: i for i, a in enumerate(ps_vals)}

    fw = FenwickTreeMax([-INF] * len(ps_vals))
    fw.update(mp[0], 1)

    # dp[i] = max score on A[0..i]
    dp = [0] * (N + 1)
    for i in range(N):  
        # dp[i] = max_{-1 <= j < i s.t. sum(j + 1..i) >= 0} dp[j - 1] + i - j
        j = bisect_right(ps_vals, ps[i + 1]) - 1
        dp[i] = dp[i - 1]     
        if j >= 0: dp[i] = max(dp[i], fw.query(j) + i)

        # update: consider if next segment starts at i + 1
        # track ps[i] -> max_{j s.t. ps[j] == ps[i]} dp[j - 1] - j
        fw.update(mp[ps[i + 1]], dp[i - 1] - i)

    return dp[N - 1]


def main():
    N = int(input())
    A = list(map(int, input().split()))
    res = solve(N, A)
    print(res)


if __name__ == '__main__':
    main()
