''' Problem B1: Sum 41 (Chapter 1)
https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/B1
'''

import os, sys
input = sys.stdin.readline  # strip() if str
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

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

def solve(P):
    res = []
    s = 0
    for d in PRIMES:
        while P % d == 0 and (s + d) <= 41:
            P //= d
            res.append(d)
            s += d
    
    if P != 1: return -1
    return res + [1] * (41 - s)


def main():
    T = int(input())
    for t in range(T):
        P = int(input())
        res = solve(P)
        if res == -1: print(f'Case #{t + 1}: {res}')
        else: print(f'Case #{t + 1}: {len(res)}', *res)


if __name__ == '__main__':
    main()

