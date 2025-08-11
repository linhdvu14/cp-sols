''' B. Minor Reduction
https://codeforces.com/contest/1626/problem/B
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug')

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

def solve(S):
    N = len(S)

    # reduce rightmost 2 digits whose sum >= 10
    for i in range(N-2, -1, -1):
        a = int(S[i]) + int(S[i+1])
        if a >= 10:
            return S[:i] + str(a) + S[i+2:]
    
    # reduce leftmost 2 digits
    return str(int(S[0]) + int(S[1])) + S[2:]



def main():
    T = int(input())
    for _ in range(T):
        S = input().decode().strip()
        out = solve(S)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

