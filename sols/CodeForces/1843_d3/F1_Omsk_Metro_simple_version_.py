''' F1. Omsk Metro (simple version)
https://codeforces.com/contest/1843/problem/F1
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

def solve(M, events):
    # nodes[u] = 
    # - min suff on path u..0
    # - max suff on path u..0
    # - min subseg on path u..0
    # - max subset on path u..0
    nodes = [[0, 1, 0, 1]]
    res = []
    for e in events:
        if e[0] == '+':
            p, w = int(e[1]) - 1, int(e[2])
            smn, smx, mn, mx = nodes[p]
            smn = min(smn, 0) + w 
            smx = max(smx, 0) + w 
            mn = min(mn, smn)
            mx = max(mx, smx)
            nodes.append([smn, smx, mn, mx])
        else:
            v, k = int(e[2]) - 1, int(e[3])
            _, _, mn, mx = nodes[v]
            if mn <= k <= mx: res.append('YES')
            else: res.append('NO')

    return res


def main():
    T = int(input())
    for _ in range(T):
        M = int(input())
        events = [input().decode().strip().split() for _ in range(M)]
        res = solve(M, events)
        print(*res, sep='\n')


if __name__ == '__main__':
    main()

