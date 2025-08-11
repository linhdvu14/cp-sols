''' E. Breaking the Wall
https://codeforces.com/contest/1674/problem/E
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
    res = INF
    mns = [INF, INF]

    for i in range(N):
        # [a] b [c]
        if 0 < i < N-1: res = min(res, (A[i-1] + A[i+1] + 1) // 2)
    
        # [a] [b]
        if i < N-1: 
            a, b = min(A[i], A[i+1]), max(A[i], A[i+1])
            if a <= (b+1)//2: res = min(res, (b+1)//2)
            else: res = min(res, (a + b + 2) // 3)

        # [a] ... [b]
        mns = sorted(mns + [A[i]])[:2]
        res = min(res, (mns[0] + 1) // 2 + (mns[1] + 1) // 2)

    return res


def main():
    N = int(input())
    A = list(map(int, input().split()))
    out = solve(N, A)
    print(out)


if __name__ == '__main__':
    main()

