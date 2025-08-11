''' B. Split Sort
https://codeforces.com/contest/1863/problem/B
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

def solve(N, P):
    pos = [-1] * N
    for i, p in enumerate(P): pos[p - 1] = i

    res = 0
    for i in range(N):
        if pos[i] == -1: continue
        res += 1
        prev, pos[i] = pos[i], -1
        while i + 1 < N and pos[i + 1] > prev:
            prev, pos[i + 1] = pos[i + 1], -1
            i += 1

    return res - 1


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        P = list(map(int, input().split()))
        res = solve(N, P)
        print(res)


if __name__ == '__main__':
    main()

