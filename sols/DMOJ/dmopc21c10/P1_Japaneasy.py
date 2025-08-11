''' DMOPC '21 Contest 10 P1 - Japaneasy
https://dmoj.ca/problem/dmopc21c10p1
'''

import os, sys
input = sys.stdin.readline  # strip() if str

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

cands = set([
    'a', 'ka', 'na', 'ha', 'ma', 'ra',
    'i', 'ki', 'ni', 'hi', 'mi', 'ri',
    'u', 'ku', 'nu', 'fu', 'mu', 'ru',
    'e', 'ke', 'ne', 'he', 'me', 're',
    'o', 'ko', 'no', 'ho', 'mo', 'ro',
])

def solve(S):
    i = 0
    while i < len(S):
        if S[i] in cands: i += 1
        elif i < len(S) - 1 and S[i:i+2] in cands: i += 2
        else: return 'NO'
    return 'YES'


def main():
    T = int(input())
    for _ in range(T):
        S = input().strip()
        out = solve(S)
        print(out)


if __name__ == '__main__':
    main()

