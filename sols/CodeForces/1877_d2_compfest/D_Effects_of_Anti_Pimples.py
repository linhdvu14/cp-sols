''' D. Effects of Anti Pimples
https://codeforces.com/contest/1877/problem/D
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
MOD = 998244353

def solve(N, A):
    A = [-1] + A
    for i in range(1, N + 1):
        for j in range(i, N + 1, i):
            A[i] = max(A[i], A[j])
    A.sort()
    
    res = 0
    two = 1
    for i in range(1, N + 1):
        res = (res + two * A[i]) % MOD
        two = two * 2 % MOD

    return res


def main():
    N = int(input())
    A = list(map(int, input().split()))
    res = solve(N, A)
    print(res)


if __name__ == '__main__':
    main()

