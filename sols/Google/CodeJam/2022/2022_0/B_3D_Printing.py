''' 3D Printing
https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4672b
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

def solve(P):
    N = 10**6
    mns = [min(p[i] for p in P) for i in range(4)]
    if sum(mns) < N: return 'IMPOSSIBLE'
    res = [0] * 4
    for i, mn in enumerate(mns):
        res[i] = min(N, mn)
        N -= min(N, mn)
    return ' '.join(map(str, res))


def main():
    T = int(input())
    for t in range(T):
        P = [tuple(map(int, input().split())) for _ in range(3)]
        out = solve(P)
        print(f'Case #{t+1}: {out}')


if __name__ == '__main__':
    main()

