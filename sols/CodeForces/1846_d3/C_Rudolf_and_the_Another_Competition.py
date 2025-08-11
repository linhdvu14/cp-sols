''' C. Rudolf and the Another Competition
https://codeforces.com/contest/1846/problem/C
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

def solve(N, M, H, A):
    def f(A):
        A.sort()
        s = t = p = 0
        for a in A:
            if t + a > H: break 
            t += a
            p += t
            s += 1
        return s, p 
    
    B = []
    for i, a in enumerate(A):
        s, p = f(a)
        B.append((s, -p, -i))
    B.sort(reverse=True)

    for r, (_, _, i) in enumerate(B):
        if i == 0: 
            return r + 1


def main():
    T = int(input())
    for _ in range(T):
        N, M, H = list(map(int, input().split()))
        A = [list(map(int, input().split())) for _ in range(N)]
        res = solve(N, M, H, A)
        print(res)


if __name__ == '__main__':
    main()

