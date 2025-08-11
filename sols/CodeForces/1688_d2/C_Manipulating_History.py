''' C. Manipulating History
https://codeforces.com/contest/1688/problem/C
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

# only src char has parity(sum occurrences in T) != parity(num occurrences in S)

def solve(N, T, S):
    res = 0
    for s in T + [S]:
        for c in s:
            res ^= ord(c) - ord('a')
    return chr(res + ord('a'))


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        T = [input().decode().strip() for _ in range(2*N)]
        S = input().decode().strip()
        out = solve(N, T, S)
        print(out)


if __name__ == '__main__':
    main()

