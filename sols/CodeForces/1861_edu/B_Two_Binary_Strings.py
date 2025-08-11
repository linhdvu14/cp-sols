''' B. Two Binary Strings
https://codeforces.com/contest/1861/problem/B
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

def solve(A, B):
    if A[0] != B[0] or A[-1] != B[-1]: return 'NO'
    if A[0] == A[-1]: return 'YES'

    N = len(A)

    L = [0] * N + [1]
    for i in range(N):
        a, b = A[i], B[i]
        if a == b: L[i] = L[i - 1]
        if a == b == A[0]: L[i] = 1
    
    R = [0] * N + [1]
    for i in range(N - 1, -1, -1):
        a, b = A[i], B[i]
        if a == b: R[i] = R[i + 1]
        if a == b == A[-1]: R[i] = 1
    
    for i in range(N):
        if L[i] and R[i + 1]:
            return 'YES'
    
    return 'NO'


def main():
    T = int(input())
    for _ in range(T):
        A = input().decode().strip()
        B = input().decode().strip()
        res = solve(A, B)
        print(res)


if __name__ == '__main__':
    main()

