''' B. It's About Drive
https://tlx.toki.id/contests/troc-25/problems/B
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

if DEBUG:
    from inspect import currentframe, getframeinfo
    from re import search

def debug(*args):
    if not DEBUG: return
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')


INF = float('inf')

# -----------------------------------------

def solve(N, F, D):
    if F > N or F*(F+1) // 2 > D: return False

    # peak
    P = F
    while True:
        if 2*P-F > N or P*(P+1) // 2 + max((P-1+F)*(P-F) // 2, 0) > D: break
        P += 1
    P -= 1

    # rem
    D -= P*(P+1) // 2 + max((P-1+F)*(P-F) // 2, 0)
    N -= 2*P - F
    return D <= P*N


def main():
    N, F, D = list(map(int, input().split()))
    out = solve(N, F, D)
    print('YES' if out else 'NO')


if __name__ == '__main__':
    main()

