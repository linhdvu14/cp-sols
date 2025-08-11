''' C. Representative Edges
https://codeforces.com/contest/1616/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

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

# arithmetic sequence
# (a+b+c) / 3 = (a+c) / 2 -> 2b = a + c 
def solve(N, A):
    if N == 1 or N == 2: return 0
    res = N
    
    # keep A[i], A[j] same
    for i in range(N):
        for j in range(i+1, N):
            cnt = 0
            # (A[i] - A[k]) / (i-k) == (A[j] - A[k]) / (j-k)?
            for k in range(N):
                if k == i or k == j: continue
                if (A[i] - A[k]) * (j - k) != (A[j] - A[k]) * (i - k):
                    cnt += 1
            res = min(res, cnt)

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

