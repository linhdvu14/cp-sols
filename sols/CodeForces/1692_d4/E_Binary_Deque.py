''' E. Binary Deque
https://codeforces.com/contest/1692/problem/E
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') not in [None, '0']

if DEBUG:
    from inspect import currentframe, getframeinfo
    from re import search

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

def solve(N, S, A):
    if sum(A) < S: return -1
    pref = {0: -1}
    res = cur = 0
    for i, a in enumerate(A):
        cur += a 
        if cur - S in pref: res = max(res, i - pref[cur - S])
        if cur not in pref: pref[cur] = i
    return N - res


def main():
    T = int(input())
    for _ in range(T):
        N, S = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(N, S, A)
        print(out)


if __name__ == '__main__':
    main()

