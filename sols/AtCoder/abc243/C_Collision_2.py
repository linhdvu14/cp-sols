''' C - Collision 2
https://atcoder.jp/contests/abc243/tasks/abc243_c
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
    N = int(input())
    rows = {}
    for i in range(N):
        x, y = list(map(int, input().split()))
        if y not in rows: rows[y] = []
        rows[y].append((x, i))

    S = input().strip().decode()
    for pos in rows.values():
        pos.sort()
        for i in range(1, len(pos)):
            _, i1 = pos[i-1]
            _, i2 = pos[i]
            if S[i1] == 'R' and S[i2] == 'L': return 'Yes'
    return 'No'


if __name__ == '__main__':
    out = main()
    print(out)
