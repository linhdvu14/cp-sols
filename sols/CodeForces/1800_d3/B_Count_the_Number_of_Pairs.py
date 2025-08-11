''' B. Count the Number of Pairs
https://codeforces.com/contest/1800/problem/B
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

def solve(N, K, S):
    lo, up = [0] * 26, [0] * 26
    for c in S:
        if 'a' <= c <= 'z': lo[ord(c) - ord('a')] += 1
        else: up[ord(c) - ord('A')] += 1

    res = add = 0
    for a, b in zip(lo, up):
        res += min(a, b)
        add += abs(a - b) // 2
    res += min(add, K)

    return res 


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        S = input().decode().strip()
        res = solve(N, K, S)
        print(res)


if __name__ == '__main__':
    main()

