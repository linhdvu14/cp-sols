''' C. Vika and Price Tags
https://codeforces.com/contest/1848/problem/C
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

def solve(N, A, B):
    def f(a, b):
        res = 0
        while b:
            if a < b: 
                res += 1 
                a, b = b, b - a 
            else:
                n, r = divmod(a, b)
                if n & 1:
                    res += 1
                    a, b = b, r 
                else:
                    a, b = r, b
        return res % 3

    par = -1
    for a, b in zip(A, B):
        if a == b == 0: continue
        p = f(a, b)
        if par == -1: par = p 
        elif par != p: return 'NO'

    return 'YES'


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        res = solve(N, A, B)
        print(res)


if __name__ == '__main__':
    main()

