''' C. To Become Max
https://codeforces.com/contest/1856/problem/C
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

def solve(N, K, A):
    def ok(idx, x):
        rem = K
        for i in range(idx, N - 1):
            need = max(x - (i - idx) - A[i], 0)
            if not need: return True
            if rem < need: return False 
            rem -= need
        return A[-1] >= x - (N - 1 - idx)

    res = max(A)
    for idx in range(N):
        lo, hi = A[idx], 10**9
        while lo <= hi:
            mi = (lo + hi) // 2
            if ok(idx, mi):
                res = max(res, mi)
                lo = mi + 1
            else:
                hi = mi - 1
    
    return res


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, K, A)
        print(res)


if __name__ == '__main__':
    main()

