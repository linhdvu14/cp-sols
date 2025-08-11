''' B. Restore the Weather
https://codeforces.com/contest/1833/problem/B
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

def solve(N, K, A, B):
    idxa = sorted(list(range(N)), key=lambda i: A[i])
    idxb = sorted(list(range(N)), key=lambda i: B[i])
    res = [-1] * N 
    for ia, ib in zip(idxa, idxb): res[ia] = B[ib]
    return res


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        res = solve(N, K, A, B)
        print(*res)


if __name__ == '__main__':
    main()
