''' D. Robot Cleaner Revisit
https://codeforces.com/contest/1623/problem/D
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

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

def mod_inv(a, p):
    '''return 1/a mod p i.e. b s.t. ab = 1 (mod p)
    Fermat's little theorem: x = x^p mod p -> x^(-1) = x^(p-2) mod p
    '''
    return pow(a, p-2, p)


def mod_div(a, b, p):
    '''return a/b mod p'''
    return a * mod_inv(b, p) % p


# robot walks in cycle and passes through k good points
# consider (s, x1, x2, ..., xk) where
# s = distance from start point to good point 1
# xi = distance from good point i to good point i+1
# xk = distance from good point k back to start
# let C = expected cost from start point
# then C = s + (1-p) * (x1 + (1-p) * (x2 + (1-p) * ( ... + (1-p) * (xk + C) )))
# C = s + x1*(1-p) + x2*(1-p)^2 + ... + xk*(1-p)^k + C*(1-p)^k
def solve_1(R, C, r1, c1, r2, c2, p):
    p = mod_div(p, 100, MOD)

    # find dists = (s, x1, x2, ..., xk)
    dists = []
    d, dr, dc = 0, 1, 1
    seen = set()
    while True:
        if not 1 <= r1+dr <= R: dr = -dr
        if not 1 <= c1+dc <= C: dc = -dc
        
        if (r1, c1, dr, dc) in seen: 
            dists.append(d)
            break
        if r1 == r2 or c1 == c2: 
            dists.append(d)
            d = 0
        seen.add((r1, c1, dr, dc))
        r1 += dr
        c1 += dc
        d += 1
    
    # S = s + x1*(1-p) + x2*(1-p)^2 + ... + xk*(1-p)^k
    S, m = 0, 1
    for d in dists:
        S += d * m
        m = m * (1 - p) % MOD
    m = mod_div(m, 1-p, MOD)
    return mod_div(S, 1 - m, MOD)


# consider all good points encountered during cycle: x0, x1, ..., xk
# where xi = distance from point i to start point, S = cycle len
# then C = p * x0 + p(1-p) * x1 + p(1-p)^2 * x2 + ...  + p(1-p)^k * xk + (1-p)^(k+1) * (cycle len + C)
def solve_2(R, C, r1, c1, r2, c2, p):
    p = mod_div(p, 100, MOD)

    # find dists = (x0, x1, ..., xk)   
    d, dr, dc = 0, 1, 1
    start = None
    dists = []
    while True:
        if not 1 <= r1+dr <= R: dr = -dr
        if not 1 <= c1+dc <= C: dc = -dc
        if start is None: 
            start = (r1, c1, dr, dc)
        elif start == (r1, c1, dr, dc):
            break
        if r1 == r2 or c1 == c2: dists.append(d)
        r1 += dr
        c1 += dc
        d += 1

    # S = p * x0 + p(1-p) * x1 + p(1-p)^2 * x2 + ...  + p(1-p)^k * xk
    S, m = 0, p
    for x in dists:
        S += m * x
        m = m * (1 - p) % MOD
    
    m = mod_div(m, p, MOD)
    res = mod_div(S + m*d, 1 - m, MOD)
    return res


# why cycle back to start point?
# https://codeforces.com/blog/entry/98463?#comment-872602

solve = solve_2


def main():
    T = int(input())
    for _ in range(T):
        R, C, r1, c1, r2, c2, p = list(map(int, input().split()))
        out = solve(R, C, r1, c1, r2, c2, p)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

