''' C. Strongly Composite
https://codeforces.com/contest/1823/problem/C
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
from collections import defaultdict

def solve(N, A):
    cnt = defaultdict(int)
    for a in A: 
        d = 2
        while d * d <= a:
            while a % d == 0:
                cnt[d] += 1
                a //= d 
            d += 1
        if a > 1: cnt[a] += 1

    res = rem = 0
    for c in cnt.values():
        res += c // 2 
        rem += c % 2
    res += rem // 3 
    
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

