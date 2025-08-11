''' B - Pasta
https://atcoder.jp/contests/abc241/tasks/abc241_b
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
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cntA, cntB = {}, {}
    for a in A: cntA[a] = cntA.get(a, 0) + 1
    for b in B: cntB[b] = cntB.get(b, 0) + 1

    if all(cntA.get(b, 0) >= cnt for b, cnt in cntB.items()):
        print('Yes')
    else:
        print('No')



if __name__ == '__main__':
    main()

