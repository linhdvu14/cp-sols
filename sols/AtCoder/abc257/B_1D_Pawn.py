''' B - 1D Pawn
https://atcoder.jp/contests/abc257/tasks/abc257_b
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
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
    N, K, Q = list(map(int, input().split()))
    A = list(map(int, input().split()))

    L = list(map(int, input().split()))
    for i in L:
        i -= 1
        if A[i] == N or (i < K-1 and A[i] + 1 == A[i+1]): continue
        A[i] += 1

    print(*A)



if __name__ == '__main__':
    main()

