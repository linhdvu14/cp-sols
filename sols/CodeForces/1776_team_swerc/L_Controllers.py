''' L. Controllers
https://codeforces.com/contest/1776/problem/L
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

def main():
    N = int(input())
    S = input().decode().strip()
    Q = int(input())

    M, N = S.count('+'), S.count('-')
    res = ['NO'] * Q 
    for i in range(Q):
        a, b = list(map(int, input().split()))
        if a == b:
            if M == N: res[i] = 'YES'
        else:
            d, r = divmod((N - M) * b, a - b)
            lo = max(0, -d)
            hi = min(M - d, N)
            if not r and lo <= hi: res[i] = 'YES'

    print(*res, sep='\n')


if __name__ == '__main__':
    main()

