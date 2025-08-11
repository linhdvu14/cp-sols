''' B. Fear of the Dark
https://codeforces.com/contest/1886/problem/B
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

def solve(P, A, B):
    def dist(A, B): return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5
    O = [0, 0]

    res = min(
        max(dist(A, O), dist(A, P)),
        max(dist(B, O), dist(B, P)),
        max(dist(A, B) / 2, min(dist(A, O), dist(B, O)), min(dist(A, P), dist(B, P))),
    )
    
    return res


def main():
    T = int(input())
    for _ in range(T):
        P = list(map(int, input().split()))
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        res = solve(P, A, B)
        print(res)


if __name__ == '__main__':
    main()

