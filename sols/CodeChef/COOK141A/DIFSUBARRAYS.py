''' Different Subarrays Rearrange
https://www.codechef.com/COOK141A/problems/DIFSUBARRAYS
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

def solve(N, A):
    cnt = {}
    for a in A: cnt[a] = cnt.get(a, 0) + 1

    # rotate
    vals = sorted([(c, v) for v, c in cnt.items()], reverse=True)
    B = [[v]*c for c, v in vals]
    C = B[1:] + [B[0]]
    
    # flatten
    B = [v for ls in B for v in ls]
    C = [v for ls in C for v in ls]

    for i in range(N):
        cb, cc = {}, {}
        for j in range(i, N):
            b, c = B[j], C[j]
            cb[b] = cb.get(b, 0) + 1
            cc[c] = cc.get(c, 0) + 1
            if i == 0 and j == N-1: continue
            if cb == cc: print('NO'); return
    
    print('YES')
    print(*B)
    print(*C)


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        solve(N, A)


if __name__ == '__main__':
    main()

