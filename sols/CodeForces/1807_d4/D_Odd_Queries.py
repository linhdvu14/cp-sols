''' D. Odd Queries
https://codeforces.com/contest/1807/problem/D 
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

def solve(N, Q, A, queries):
    ps = [0] * (N + 1)
    for i, a in enumerate(A): ps[i] = (ps[i - 1] + a) % 2

    res = ['NO'] * Q
    for i, (l, r, k) in enumerate(queries):
        l -= 1; r -= 1
        if (ps[N - 1] - (ps[r] - ps[l - 1]) + k * (r - l + 1)) % 2: res[i] = 'YES'

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, Q = list(map(int, input().split()))
        A = list(map(int, input().split()))
        queries = [list(map(int, input().split())) for _ in range(Q)]
        res = solve(N, Q, A, queries)
        print(*res, sep='\n')


if __name__ == '__main__':
    main()

