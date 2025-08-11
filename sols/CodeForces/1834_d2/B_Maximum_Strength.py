''' B. Maximum Strength
https://codeforces.com/contest/1834/problem/B
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

def solve(L, R):
    N = len(R)
    L = '0' * (N - len(L)) + L 

    for i, (l, r) in enumerate(zip(L, R)):
        if l == r: continue
        return 9 * (N - i - 1) + int(r) - int(l)

    return 0


def main():
    T = int(input())
    for _ in range(T):
        L, R = input().decode().strip().split()
        res = solve(L, R)
        print(res)


if __name__ == '__main__':
    main()

