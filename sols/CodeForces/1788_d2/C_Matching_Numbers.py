''' C. Matching Numbers
https://codeforces.com/contest/1788/problem/C
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

# N = 5
# 0:   9  = 1 + 8
# 1:   10 = 4 + 6
# 2:   11 = 2 + 9
# 3:   12 = 5 + 7
# 4:   13 = 3 + 10

def solve(N):
    if N % 2 == 0: return 'NO', []
    a = (3 * N + 1) // 2 + 1

    res = []
    for i in range(N):
        if i % 2 == 0: x = i // 2 + 1
        else: x = i // 2 + 1 + (N + 1) // 2
        res.append([x, a + i - x])

    return 'YES', res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        a, b = solve(N)
        print(a)
        for t in b: print(*t)


if __name__ == '__main__':
    main()

