''' D. Vika and Bonuses
https://codeforces.com/contest/1848/problem/D
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

def solve(S, K):
    res = S * K
    if S % 2:
        S += S % 10
        K -= 1
        res = max(res, S * K)
    
    if S % 10 == 0: return res

    def f(n): return (S + 20 * n) * (K - 4 * n)

    # fix r, accumulate for first 4n + r steps
    # then score = (S + r + 20n) * (K - r - 4n)
    # ternary search for n
    for _ in range(4):
        if not K: break
        S += S % 10
        K -= 1

        lo, hi = 0, K // 4
        while lo < hi:
            mi = (lo + hi) // 2
            if f(mi) > f(mi + 1): hi = mi 
            else: lo = mi + 1
        
        res = max(res, f(lo))

    return res


def main():
    T = int(input())
    for _ in range(T):
        S, K = list(map(int, input().split()))
        res = solve(S, K)
        print(res)


if __name__ == '__main__':
    main()

