''' C. Serval and Toxel's Arrays
https://codeforces.com/contest/1789/problem/C
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

from collections import defaultdict

def solve():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))

    cnt = defaultdict(int)
    for a in A: cnt[a] = M + 1

    for i in range(M):
        p, v = list(map(int, input().split()))
        p -= 1
        cnt[A[p]] -= M - i 
        cnt[v] += M - i
        A[p] = v 

    res = N * M * (M + 1)
    for c in cnt.values():  # num pairs that both contain v
        res -= c * (c - 1) // 2

    print(res)


def main():
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()

