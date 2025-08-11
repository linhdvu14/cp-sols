''' Punched Cards 
https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4621b
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

def solve(R, C, t):
    a = '+-' * C + '+'
    b = '|.' * C + '|'

    print(f'Case #{t+1}:')
    print('..' + a[2:])
    print('..' + b[2:])
    for _ in range(R-1): print(a + '\n' + b)
    print(a)


def main():
    T = int(input())
    for t in range(T):
        R, C = list(map(int, input().split()))
        solve(R, C, t)


if __name__ == '__main__':
    main()

