''' B. Tenzing and Books
https://codeforces.com/contest/1842/problem/B
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

def solve(N, X, As):
    x = 0
    for A in As:
        for a in A:
            if a & X != a: break
            x |= a 
    return 'Yes' if x == X else 'No'


def main():
    T = int(input())
    for _ in range(T):
        N, X = list(map(int, input().split()))
        As = [list(map(int, input().split())) for _ in range(3)]
        res = solve(N, X, As)
        print(res)


if __name__ == '__main__':
    main()

