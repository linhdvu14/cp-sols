''' F. Forever Winter
https://codeforces.com/contest/1829/problem/F
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

def solve(N, M, edges):
    deg = [0] * N
    for u, v in edges:
        deg[u - 1] += 1
        deg[v - 1] += 1
    
    cnt = {}
    for d in deg:
        if d == 1: continue
        cnt[d] = cnt.get(d, 0) + 1
    
    x = y = 0
    for k, v in cnt.items():
        if v == 1: x = k 
        else: y = k
    
    if x == 0: return y, y - 1
    return x, y - 1


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(M)]
        res = solve(N, M, edges)
        print(*res)


if __name__ == '__main__':
    main()

