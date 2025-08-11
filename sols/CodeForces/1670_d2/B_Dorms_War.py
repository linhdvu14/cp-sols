''' B. Dorms War
https://codeforces.com/contest/1670/problem/B
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

def solve(N, S, specials):
    specials = set(specials)

    # max dist from any char to the next special char
    mx = i = 0
    while i < N:
        j = i + 1
        while j < N:
            if S[j] in specials:
                mx = max(mx, j-i)
                break
            j += 1
        i = j

    return mx


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().decode().strip()
        specials = input().decode().strip().split()[1:]
        out = solve(N, S, specials)
        print(out)


if __name__ == '__main__':
    main()

