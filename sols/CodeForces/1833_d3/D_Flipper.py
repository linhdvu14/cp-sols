''' D. Flipper
https://codeforces.com/contest/1833/problem/D
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
    if N == 1: return A

    j = 1
    for i in range(2, N):
        if A[i] > A[j]:
            j = i 
    
    res = max(A[::-1], [A[-1]] + A[:-1])
    tail = A[j:]
    for i in range(j):
        head = A[:i]
        mid = A[i:j]
        cand = tail + mid[::-1] + head
        res = max(res, cand)

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(*res)


if __name__ == '__main__':
    main()

