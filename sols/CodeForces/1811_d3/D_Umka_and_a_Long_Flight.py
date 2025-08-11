''' D. Umka and a Long Flight
https://codeforces.com/contest/1811/problem/D
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

FIB = [1, 1]
for _ in range(50): FIB.append(FIB[-1] + FIB[-2])

def f(n, x, y):
    if n == 1: return x == 1
    if y > FIB[n]: return f(n - 1, FIB[n - 1] - (y - FIB[n]) + 1, x)
    if y <= FIB[n - 1]: return f(n - 1, y, FIB[n] - x + 1)
    return False


def main():
    T = int(input())
    for _ in range(T):
        N, X, Y = list(map(int, input().split()))
        res = f(N, X, Y)
        print('YES' if res else 'NO')


if __name__ == '__main__':
    main()

