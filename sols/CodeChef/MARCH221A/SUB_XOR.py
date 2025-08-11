''' Subarray XOR
https://www.codechef.com/MARCH221A/problems/SUB_XOR
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

MOD = 998244353

def solve(N, S):
    # A[:N] = XOR of all S[i:] for i=0..N-1
    # A[:j] = XOR of all S[i:j] for i=0..j-1
    A = [0] * N
    for i, d in enumerate(S):
        if i % 2 == 0 and d == 1:
            A[i] = 1
    
    pref = [A[0]]
    for i in range(1, N):
        pref.append((pref[-1] + A[i]) % 2)

    res = 0
    for b in pref:
        res = ((res << 1) + b) % MOD

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = list(map(int, list(input().decode().strip())))
        out = solve(N, S)
        print(out)


if __name__ == '__main__':
    main()

