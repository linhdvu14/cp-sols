''' B. Up & Down
https://tlx.toki.id/contests/troc-26/problems/B
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

def main():
    R, C = list(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(R)]

    sums = [0, 0]
    one_pos = -1
    for r in range(R):
        for c in range(C):
            v = grid[r][c]
            p = (r + c) % 2
            if v == -1:
                one_pos = p
            else:
                sums[p] += v
    if sums[0] == sums[1]: return 'YES\n0'
    if sums[0] < sums[1]: return f'YES\n{sums[1]-sums[0]}' if one_pos == 0 else 'NO'
    return f'YES\n{sums[0]-sums[1]}' if one_pos == 1 else 'NO'



if __name__ == '__main__':
    out = main()
    print(out)

