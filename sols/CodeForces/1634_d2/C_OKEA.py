''' C. OKEA
https://codeforces.com/contest/1634/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']

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

# each row must be all even or all odd
# arithmetic sequence

def solve(R, C):
    N = R * C
    if N % 2 == 1:
        if C != 1: return 'NO', []
        return 'YES', [[i+1] for i in range(N)]
    else:
        if R % 2 == 1: return 'NO', []
        res = [[] for _ in range(R)]
        odd, even = 1, 2
        for r in range(R):
            if r % 2 == 0:
                res[r] = [even + 2*i for i in range(C)]
                even += 2*C
            else:
                res[r] = [odd + 2*i for i in range(C)]
                odd += 2*C
        return 'YES', res


def main():
    T = int(input())
    for _ in range(T):
        R, C = list(map(int, input().split()))
        out1, out2 = solve(R, C)
        print(out1)
        if out1 == 'YES':
            for row in out2: print(*row)

if __name__ == '__main__':
    main()

