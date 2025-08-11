''' G1. Teleporters (Easy Version)
https://codeforces.com/contest/1791/problem/G1
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

def solve(N, C, A):
    cost = [i + a + 1 for i, a in enumerate(A)]
    cost.sort(reverse=True)

    res = 0
    while cost and C >= cost[-1]:
        res += 1
        C -= cost.pop()

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, C = list(map(int, input().split()))
        A = list(map(int, input().split()))
        res = solve(N, C, A)
        print(res)


if __name__ == '__main__':
    main()

