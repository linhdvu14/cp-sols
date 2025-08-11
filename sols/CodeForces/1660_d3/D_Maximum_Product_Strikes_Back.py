''' D. Maximum Product Strikes Back
https://codeforces.com/contest/1660/problem/D
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

def solve(N, A):
    if all(a == 0 for a in A): return [N, 0]
    cands = []

    # get cand intervals
    def calc(l, r):  
        if l == -1 or l > r: return
        first_neg = last_neg = -1
        neg = 0
        i = l
        while i <= r:
            if A[i] < 0:
                if first_neg < 0: first_neg = i
                last_neg = i
                neg ^= 1
            i += 1
        if neg: cands.extend([(first_neg + 1, r), (l, last_neg - 1)])
        else: cands.append((l, r))
    
    zero = -1
    for i, a in enumerate(A):
        if a == 0:
            calc(zero + 1, i - 1)
            zero = i
    calc(zero + 1, N - 1)

    # compare
    pref = [0] * (N + 1)
    c = 0
    for i, a in enumerate(A):
        if abs(a) == 2: c += 1
        pref[i+1] = c
    
    mx, mxl, mxr = 0, 0, N
    for l, r in cands:
        twos = pref[r+1] - pref[l]
        if twos > mx: mx, mxl, mxr = twos, l, N - r - 1

    return mxl, mxr


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        print(*out)


if __name__ == '__main__':
    main()
