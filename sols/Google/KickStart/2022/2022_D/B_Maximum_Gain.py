''' Maximum Gain
https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caea6/0000000000b76fae
'''

import io, os, sys
from operator import ilshift
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

def solve(N, A, M, B, K):
    if K == M + N: return sum(A) + sum(B)

    mna = [0] + [INF] * N
    for i in range(N):
        s = 0
        for j in range(i, N):
            s += A[j]
            mna[j - i + 1] = min(mna[j - i + 1], s)
    
    mnb = [0] + [INF] * M
    for i in range(M):
        s = 0
        for j in range(i, M):
            s += B[j]
            mnb[j - i + 1] = min(mnb[j - i + 1], s)
    
    mns = INF
    for i in range(N + 1):
        j = M + N - K - i
        if not 0 <= j <= M: continue
        mns = min(mns, mna[i] + mnb[j])

    return sum(A) + sum(B) - mns


def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        M = int(input())
        B = list(map(int, input().split()))
        K = int(input())
        out = solve(N, A, M, B, K)
        print(f'Case #{t+1}: {out}')


if __name__ == '__main__':
    main()

