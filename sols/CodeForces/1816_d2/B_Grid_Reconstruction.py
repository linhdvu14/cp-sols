''' B. Grid Reconstruction
https://codeforces.com/contest/1816/problem/B
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

def solve(N):
    res = [[-1] * N for _ in range(2)]
    res[0][0] = 2 * N - 1
    res[-1][-1] = 2 * N

    l, r = 1, N + 1
    for i in range(1, N):
        if i % 2 == 1:
            res[0][i] = l 
            res[1][i - 1] = l + 1
            l += 2
        else:
            res[0][i] = r 
            res[1][i - 1] = r + 1
            r += 2

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        res = solve(N)
        for t in res: print(*t)


if __name__ == '__main__':
    main()
