''' C1. Dual (Easy Version)
https://codeforces.com/contest/1855/problem/C1
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def debug(*args):   
    if os.environ.get('debug') in [None, '0']: return
    from inspect import currentframe, getframeinfo
    from re import search
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
    res = []

    # make same sign
    idx = 0
    for i, a in enumerate(A):
        if abs(a) > abs(A[idx]):
            idx = i 
    for i in range(N):
        if i == idx: continue
        A[i] += A[idx]
        res.append([i, idx])
    
    if A[idx] > 0:
        for i in range(N - 1):
            if A[i] > A[i + 1]:
                A[i + 1] += A[i]
                res.append([i + 1, i])
    elif A[idx] < 0:
        for i in range(N - 1, 0, -1):
            if A[i] < A[i - 1]:
                A[i - 1] += A[i]
                res.append([i - 1, i])

    assert A == sorted(A)
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(len(res))
        for a, b in res: print(a + 1, b + 1)


if __name__ == '__main__':
    main()

