''' C. Mr. Perfectly Fine
https://codeforces.com/contest/1829/problem/C
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
    a = b = c = INF
    for t, s in S:
        t = int(t)
        if s[0] == '1': a = min(a, t)
        if s[1] == '1': b = min(b, t)
        if s == '11': c = min(c, t)
    res = min(a + b, c)
    return res if res < INF else -1


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = [input().decode().strip().split() for _ in range(N)]
        res = solve(N, S)
        print(res)


if __name__ == '__main__':
    main()

