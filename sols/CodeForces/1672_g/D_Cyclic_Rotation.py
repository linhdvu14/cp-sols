''' D. Cyclic Rotation
https://codeforces.com/contest/1672/problem/D
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

# move A[i] next to some A[j] s.t. j > i, A[j] == A[i]
# tle with defaultdict

def solve_fwd(N, A, B):
    avail = {}
    i = 0
    for j, b in enumerate(B):
        if j > 0 and b == B[j-1] and avail.get(b, 0) > 0:
            avail[b] -= 1
        else:
            while i < N and A[i] != b:
                avail[A[i]] = avail.get(A[i], 0) + 1
                i += 1
            if i < N:
                i += 1

    if any(v > 0 for v in avail.values()): return 'NO'
    return 'YES'


def solve_bwd(N, A, B):
    avail = {}
    i = j = N - 1
    while j >= 0:
        while j > 0 and B[j] == B[j-1]:
            avail[B[j]] = avail.get(B[j], 0) + 1
            j -= 1
        if A[i] == B[j]:
            j -= 1
        elif avail.get(A[i], 0) > 0:
            avail[A[i]] -= 1
        else:
            return 'NO'
        i -= 1
    return 'YES'


solve = solve_bwd

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        out = solve(N, A, B)
        print(out)


if __name__ == '__main__':
    main()

