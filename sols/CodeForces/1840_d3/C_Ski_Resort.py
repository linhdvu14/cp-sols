''' C. Ski Resort
https://codeforces.com/contest/1840/problem/C
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

def solve(N, K, Q, A):
    res = cnt = 0
    for a in A:
        if a > Q:
            cnt = 0
        else:
            cnt += 1
            res += max(cnt - K + 1, 0)
    return res


def main():
    T = int(input())
    for _ in range(T):
        N, K, Q = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, K, Q, A)
        print(res)


if __name__ == '__main__':
    main()

