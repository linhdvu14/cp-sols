''' Divisible by i
https://www.codechef.com/JUNE221A/problems/DIVBYI
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

# 1 2 3 4 5 6 7 8 9
# 5 4 6 3 7 2 8 1 9

def solve(N):
    used = [0] * (N + 1)
    res = [0] * N + [N]
    for i in range(N-1, 0, -1):
        v = res[i+1] - i
        if v <= 0 or used[v]: v = res[i+1] + i
        used[v] = 1
        res[i] = v
    
    res = res[1:]
    assert all(1 <= a <= N for a in res) and len(set(res)) == N
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        out = solve(N)
        print(*out)


if __name__ == '__main__':
    main()
