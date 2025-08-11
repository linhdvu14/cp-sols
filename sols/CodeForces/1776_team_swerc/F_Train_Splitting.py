''' F. Train Splitting
https://codeforces.com/contest/1776/problem/F
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
    if N == M == 3: return 3, [1, 2, 3]

    adj = [[] for _ in range(N)]
    for i, (u, v) in enumerate(edges):
        adj[u - 1].append(i)
        adj[v - 1].append(i)
    
    res = [1] * M 
    for u in range(N):
        if len(adj[u]) < N - 1:
            for i in adj[u]: res[i] = 2
            return 2, res 
    
    # fully connected
    for i in adj[0]: res[i] = 2
    res[adj[0][-1]] = 3
    return 3, res


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(M)]
        a, b = solve(N, M, edges)
        print(a)
        print(*b)


if __name__ == '__main__':
    main()

