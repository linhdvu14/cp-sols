''' F. Fibonacci Additions
https://codeforces.com/contest/1634/problem/F
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

# let C[i] = A[i] - B[i]
#     D[i] = C[i] - C[i-1] - C[i-2]; D[0] = C[0], D[1] = C[1] - C[0]
# then A[i] == B[i] for all i <-> C[i] == 0 for all [i] <-> D[i] == 0 for all i

# operation l..r on A will update:
#  D[l] += F[0]
#  D[l+1] += F[1] - F[0]       --> += 0
#  ...D[l+i] += 0...
#  D[r+1] -= F[r-l] + F[r-l-1] --> -= F[r-l+1]
#  D[r+2] -= F[r-l]

def main():
    N, Q, MOD = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    FIB = [1, 1]
    for _ in range(N-1): FIB.append((FIB[-1] + FIB[-2]) % MOD)

    C = [(a - b) % MOD for a, b in zip(A, B)]
    D = [C[0]]
    if N > 1: D.append((C[1] - C[0]) % MOD)
    for i in range(2, N): D.append((C[i] - C[i-1] - C[i-2]) % MOD)

    # note D[i] >= 0 so D[i] == 0 iff S == 0
    S = sum(D)

    out = []
    for _ in range(Q):
        c, l, r = input().decode().strip().split()
        l, r = int(l)-1, int(r)-1
        sign = 1 if c == 'A' else -1

        S -= D[l]
        D[l] = (D[l] + sign) % MOD
        S += D[l]

        if r+1 < N:
            S -= D[r+1]
            D[r+1] = (D[r+1] - sign * FIB[r-l+1]) % MOD
            S += D[r+1]
        
        if r+2 < N:
            S -= D[r+2]
            D[r+2] = (D[r+2] - sign * FIB[r-l]) % MOD
            S += D[r+2]

        out.append('YES' if S == 0 else 'NO')
    
    print('\n'.join(out))


if __name__ == '__main__':
    main()