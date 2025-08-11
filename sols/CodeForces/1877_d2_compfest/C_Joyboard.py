''' C. Joyboard
https://codeforces.com/contest/1877/problem/C
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

def solve(N, M, K):
    two = min(N, M) + max(M // N - 1, 0)
    if K == 1: return 1
    if K == 2: return two
    if K == 3: return M - two
    return 0

def main():
    T = int(input())
    for _ in range(T):
        N, M, K = list(map(int, input().split()))
        res = solve(N, M, K)
        print(res)


if __name__ == '__main__':
    main()

