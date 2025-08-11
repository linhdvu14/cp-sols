''' B. Helmets in Night Light
https://codeforces.com/contest/1877/problem/B
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

def solve(N, P, A, B):
    C = sorted((b, a) for a, b in zip(A, B))

    rem = N - 1
    res = P
    for b, a in C:
        if b >= P: break 
        use = min(rem, a)
        rem -= use
        res += use * b
    
    res += P * rem
    return res


def main():
    T = int(input())
    for _ in range(T):
        N, P = list(map(int, input().split()))
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        res = solve(N, P, A, B)
        print(res)


if __name__ == '__main__':
    main()

