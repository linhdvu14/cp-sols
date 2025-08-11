''' E - Takahashi's Anguish
https://atcoder.jp/contests/abc256/tasks/abc256_e
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

def main():
    N = int(input())
    X = list(map(int, input().split()))
    C = list(map(int, input().split()))

    adj = [-1] * N
    for u, v in enumerate(X):
        adj[u] = v - 1
    
    # if found cycles, add min-cost edge
    res = 0
    seen = [0] * N
    for u in range(N):
        if seen[u]: continue
        stack = set()
        while not seen[u]:
            seen[u] = 1
            stack.add(u)
            u = adj[u]
        
        if u in stack:
            mn = INF
            v = u
            while True:
                mn = min(mn, C[v])
                v = adj[v]
                if v == u: break
            res += mn

    print(res)


if __name__ == '__main__':
    main()

