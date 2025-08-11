''' A. Recent Actions
https://codeforces.com/contest/1799/problem/A
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

def solve(N, M, P):
    res = [-1] * N 
    seen = [0] * M
    cur = N - 1
    for i, p in enumerate(P):
        if seen[p - N - 1]: continue
        seen[p - N - 1] = 1
        res[cur] = i + 1
        cur -= 1
        if cur < 0: break 

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        P = list(map(int, input().split()))
        res = solve(N, M, P)
        print(*res)


if __name__ == '__main__':
    main()
