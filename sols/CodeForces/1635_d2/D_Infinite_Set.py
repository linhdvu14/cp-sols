''' D. Infinite Set
https://codeforces.com/contest/1635/problem/D
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

MOD = 10**9 + 7

# 2y+1 = append 1; 4y = append 00
# F[n] = num ways to add n bits
# PREF[n] = num ways to add 0..n bits

FIB = [1, 1]
PREF = [1, 2]
for _ in range(2 * 10**5): 
    FIB.append((FIB[-1] + FIB[-2]) % MOD)
    PREF.append((PREF[-1] + FIB[-1]) % MOD)


def solve(N, P, A):
    # discard all numbers that can be derived from a smaller number in A
    S = []
    A = set(A)
    for a in A:    
        if a.bit_length() > P: continue    
        orig = a
        ok = True
        while a:
            if not (a % 2 == 1 or a % 4 == 0): break
            a >>= 1 if a % 2 == 1 else 2
            if a in A:
                ok = False
                break
        if ok: S.append(orig)
    
    # count num ways to append 00 or 1 s.t. <= P bits
    res = 0
    for a in S:
        n = P - a.bit_length()
        res = (res + PREF[n]) % MOD

    return res


def main():
    N, P = list(map(int, input().split()))
    A = list(map(int, input().split()))
    out = solve(N, P, A)
    output(f'{out}\n')


if __name__ == '__main__':
    main()

