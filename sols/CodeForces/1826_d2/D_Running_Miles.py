''' D. Running Miles
https://codeforces.com/contest/1826/problem/D 
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

# B[i] + B[j] + B[k] - (k - i) = (B[i] + i) + B[j] + (B[k] - k)
def solve(N, B):
    # mx1 = max B[i] + i
    # mx2 = max B[j] + (B[i] + i) for i < j
    res = mx1 = mx2 = 0

    for i, b in enumerate(B):
        res = max(res, mx2 + b - i)
        mx2 = max(mx2, mx1 + b)
        mx1 = max(mx1, b + i)

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        B = list(map(int, input().split()))
        res = solve(N, B)
        print(res)


if __name__ == '__main__':
    main()

