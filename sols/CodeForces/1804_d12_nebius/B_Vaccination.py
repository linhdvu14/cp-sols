''' B. Vaccination
https://codeforces.com/contest/1804/problem/B
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

def solve(N, K, D, W, A):
    res = rem = end = 0 
    for a in A:
        if not rem or a > end:
            res += 1
            end = a + W + D 
            rem = K
        rem -= 1

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, K, D, W = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, K, D, W, A)
        print(res)


if __name__ == '__main__':
    main()

