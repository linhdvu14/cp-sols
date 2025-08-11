''' F. Kosuke's Sloth
https://codeforces.com/contest/2033/problem/F
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

from inspect import currentframe, getframeinfo
from re import search
DEBUG = os.environ.get('debug') not in [None, '0']

def debug(*args):   
    if not DEBUG: return
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')

INF = float('inf')

# -----------------------------------------
MOD = 10**9 + 7

def solve(queries):
    first = {}
    K = set(q[1] for q in queries)
    for k in K:
        a, b, p = 0, 1, 1
        while b % k:
            p += 1
            a, b = b, (a + b) % k
        first[k] = p

    res = [N * first[K] % MOD for N, K in queries]
    return res


def main():
    T = int(input())
    queries = [list(map(int, input().split())) for _ in range(T)]
    res = solve(queries)
    print(*res, sep='\n')


if __name__ == '__main__':
    main()

