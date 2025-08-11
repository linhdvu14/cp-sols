'''G. Trader Problem
https://codeforces.com/contest/1618/problem/G
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

if DEBUG:
    from varname.core import argname
    from inspect import currentframe

def debug(var, *more_vars):
    if not DEBUG: return
    var_names = argname('var', '*more_vars', func=debug)
    values = (var, *more_vars)
    name_and_values = [f'{var_name}={value}'  for var_name, value in zip(var_names, values)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(name_and_values)}')


INF = float('inf')

# -----------------------------------------

# each cc is a merged interval; par points to interval right endpoint
# track how many A nodes in each cc
class UnionFind:
    def __init__(self, N):
        self.N = N
        self.parent = [i for i in range(N)]
        self.cnt = [0]*N
    
    def find(self, i):
        r = i
        while self.parent[r] != r:
            r = self.parent[r]		
        while self.parent[i] != r:
            p = self.parent[i]
            self.parent[i] = r
            i = p
        return r

    def union(self, i, j):
        ri, rj = self.find(i), self.find(j)
        if ri == rj: return
        if ri > rj: ri, rj = rj, ri
        self.parent[ri] = rj
        self.cnt[rj] += self.cnt[ri]
        self.cnt[ri] = 0


def solve(N, M, Q, A, B, queries):
    items = [(a, 1) for a in A] + [(b, 0) for b in B]
    items.sort()
    N = len(items)

    # init each item in its own cc/interval
    uf = UnionFind(N)
    s = 0
    for i, (a, d) in enumerate(items):
        if d == 1:
            uf.cnt[i] = 1
            s += a

    # precompute prefix sum
    pref = [0]
    for a, _ in items: pref.append(pref[-1] + a)

    # given items idx, find max attainable val from its cc
    def get_val(i):
        r = uf.find(i)
        c = uf.cnt[r]
        return pref[r+1] - pref[r-c+1]

    # merge adjacent intervals whose distance <= k
    # at most N-1 merges over all queries
    dist = [(items[i+1][0]-items[i][0], i) for i in range(N-1)]
    dist.sort()
    di = 0

    res = [0]*Q
    queries = [(q, i) for i, q in enumerate(queries)]
    queries.sort()
    for k, qi in queries:
        while di < N-1 and dist[di][0] <= k:
            i = dist[di][1]
            s -= get_val(i) + get_val(i+1)
            uf.union(i, i+1)
            s += get_val(i+1)
            di += 1
        res[qi] = s

    for s in res: print(s)

def main():
    N, M, Q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    queries = list(map(int, input().split()))
    solve(N, M, Q, A, B, queries)


if __name__ == '__main__':
    main()

