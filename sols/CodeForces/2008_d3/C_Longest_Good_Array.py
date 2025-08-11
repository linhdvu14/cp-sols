''' C. Longest Good Array
https://codeforces.com/contest/2008/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']
DEBUG_CASE = int(os.environ.get('case', 0))

def debug(*args):   
    if not DEBUG: return
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
    # l + (1 + n) * n // 2 <= r
    mi = int(((R - L) * 2) ** 0.5)
    for n in range(mi + 2, mi - 2, -1):
        if L + (1 + n) * n // 2 <= R:
            return 1 + n


def main():
    T = int(input())
    for ti in range(T):
        L, R = list(map(int, input().split()))
        if DEBUG and DEBUG_CASE and ti != DEBUG_CASE: continue
        res = solve(L, R)
        print(res)


if __name__ == '__main__':
    main()

