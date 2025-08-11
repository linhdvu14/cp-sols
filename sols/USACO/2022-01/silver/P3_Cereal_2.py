''' Problem 3. Cereal 2 '''

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

def solve(N, M, edges):
    adj = [[] for _ in range(M)]
    for u, v in edges:
        adj[u-1].append(v-1)
    
    # find longest non-cyclic path


def main():
    N, M = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for _ in range(N)]
    out = solve(N, M, edges)
    output(f'{out}\n')


if __name__ == '__main__':
    main()

