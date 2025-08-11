''' D. Wooden Toy Festival
https://codeforces.com/contest/1840/problem/D
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

def solve(N, A):
    A.sort()

    def is_ok(d):
        end = cnt = 0
        for a in A:
            if a > end: 
                cnt += 1
                end = a + 2 * d 
        return cnt <= 3
    
    res, lo, hi = -1, 0, 10**9
    while lo <= hi:
        mi = (lo + hi) // 2
        if is_ok(mi):
            res = mi 
            hi = mi - 1
        else:
            lo = mi + 1

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(res)


if __name__ == '__main__':
    main()

