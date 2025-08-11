''' B. Minimize Permutation Subarrays
https://codeforces.com/contest/1838/problem/B
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
    p1 = p2 = p3 = -1
    for i, a in enumerate(A):
        if a == 1: p1 = i + 1
        elif a == 2: p2 = i + 1
        elif a == N: p3 = i + 1

    if p1 < p3 < p2 or p2 < p3 < p1: return 1, 1 
    if p2 < p1 < p3 or p3 < p1 < p2: return p1, p3 
    return p2, p3



def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        res = solve(N, A)
        print(*res)


if __name__ == '__main__':
    main()

