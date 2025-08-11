''' D. Circular Spanning Tree
https://codeforces.com/contest/1682/problem/D
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

def solve(N, S):
    odds = [i for i, c in enumerate(S) if c == '1']
    if not odds or len(odds) % 2 == 1: return 'NO', []  # sum degree is even

    # hook 0...1 to center
    center = (odds[0] + 1) % N
    edges = []
    prev = '1'
    for i in range(center+1, center+N):
        i %= N
        if prev == '1': edges.append((i+1, center+1))
        else: edges.append((i+1, (i-1) % N + 1))
        prev = S[i]

    return 'YES', edges


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().decode().strip()
        r1, r2 = solve(N, S)
        print(r1)
        for x in r2: print(*x)


if __name__ == '__main__':
    main()

