''' Chef and Riffles
https://www.codechef.com/JAN221A/problems/RIFFLES
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

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

def solve(N, K):
    perm = [-1] + list(range(1, N+1, 2)) + list(range(2, N+1, 2))
    res = [-1]*(N+1)

    for i in range(N+1):
        if perm[i] == -1: continue
        cycle, u = [], i
        while not cycle or u != cycle[0]:
            cycle.append(u)
            u = perm[u]
        for i, u in enumerate(cycle):
            res[u] = cycle[(i+K) % len(cycle)]
            perm[u] = -1

    return res[1:]


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        out = solve(N, K)
        print(*out)


if __name__ == '__main__':
    main()

