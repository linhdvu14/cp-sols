''' D. Climbing the Tree
https://codeforces.com/contest/1810/problem/D
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

def solve(Q, queries):
    l, r = 1, INF 
    res = [0] * Q
    for i, ts in enumerate(queries):
        if ts[0] == 1:
            a, b, n = ts[1:]
            l2 = max(l, (a - b) * (n - 2) + a + 1 if n >= 2 else l)
            r2 = min(r, (a - b) * (n - 1) + a)
            if l2 <= r2: 
                res[i] = 1
                l, r = l2, r2
        else:
            a, b = ts[1:]
            nl = max((l - b - 1) // (a - b) + 1, 1)
            nr = max((r - b - 1) // (a - b) + 1, 1)
            res[i] = nl if nl == nr else -1

    return res


def main():
    T = int(input())
    for _ in range(T):
        Q = int(input())
        queries = [list(map(int, input().split())) for _ in range(Q)]
        res = solve(Q, queries)
        print(*res)


if __name__ == '__main__':
    main()

