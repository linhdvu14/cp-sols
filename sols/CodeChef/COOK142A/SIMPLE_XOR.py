''' Simple XOR
https://www.codechef.com/COOK142A/problems/SIMPLE_XOR 
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

def solve(L, R):
    if L % 2 == 1: L += 1
    if L + 3 > R: return [-1]
    return [L, L+1, L+2, L+3]


def main():
    T = int(input())
    for _ in range(T):
        L, R = list(map(int, input().split()))
        out = solve(L, R)
        print(*out)


if __name__ == '__main__':
    main()

