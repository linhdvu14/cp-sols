''' A. Grasshopper on a Line
https://codeforces.com/contest/1837/problem/A
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

def solve(X, K):
    if X % K: return [X]
    return [X + 1, -1]


def main():
    T = int(input())
    for _ in range(T):
        X, K = list(map(int, input().split()))
        res = solve(X, K)
        print(len(res))
        print(*res)


if __name__ == '__main__':
    main()

