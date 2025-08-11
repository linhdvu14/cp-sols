''' D. Rudolph and Christmas Tree
https://codeforces.com/contest/1846/problem/D
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

def solve(N, D, H, Y):
    sub = 0
    for i in range(1, N):
        d = max(H - (Y[i] - Y[i - 1]), 0)
        sub += d * d

    return (N - sub / H / H) * D * H / 2



def main():
    T = int(input())
    for _ in range(T):
        N, D, H = list(map(int, input().split()))
        Y = list(map(int, input().split()))
        res = solve(N, D, H, Y)
        print(res)


if __name__ == '__main__':
    main()

