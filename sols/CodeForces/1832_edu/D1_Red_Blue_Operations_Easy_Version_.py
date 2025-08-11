''' D1. Red-Blue Operations (Easy Version)
https://codeforces.com/contest/1832/problem/D1
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
    N, Q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    def f(k):
        if k <= N: return min(a + k - i if i < k else a for i, a in enumerate(A))
        add = min(k, N) - (k % 2 != N % 2)
        sub = (k - add) // 2

        tot, base = 0, INF 
        for i, a in enumerate(A):
            if i < add: a += k - i 
            tot += a 
            base = min(base, a)
        
        rem = max(0, sub - (tot - base * N))
        res = base - rem // N - (1 if rem % N else 0)
        return res

    A.sort()
    res = [f(k) for k in queries]
    print(*res)


if __name__ == '__main__':
    main()

