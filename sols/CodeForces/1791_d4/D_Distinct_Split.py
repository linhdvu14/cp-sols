''' D. Distinct Split
https://codeforces.com/contest/1791/problem/D
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

def solve(N, S):
    right = {}
    for c in S: right[c] = right.get(c, 0) + 1

    res = 0
    left = set()
    for i, c in enumerate(S):
        left.add(c)
        right[c] -= 1
        if not right[c]: right.pop(c)
        if i < N - 1: res = max(res, len(left) + len(right))

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().decode().strip()
        res = solve(N, S)
        print(res)


if __name__ == '__main__':
    main()

