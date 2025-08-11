''' C. Zig-Zag
https://tlx.toki.id/contests/troc-26/problems/C
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

# put small numbers in even pos (S // 2 slots) and big numbers in odd pos ((S+1) // 2 slots)
# ok if no overlapping spills

def main():
    N = int(input())
    A = list(map(int, input().split()))
    half = sum(A) // 2
    idx = 0
    for cnt in A:
        idx += cnt
        if idx < half: continue
        if idx == half: return 'YES'
        l, r = idx - half, idx - cnt
        return 'YES' if l < r else 'NO'


if __name__ == '__main__':
    out = main()
    print(out)

