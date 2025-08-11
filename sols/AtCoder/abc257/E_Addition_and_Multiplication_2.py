''' E - Addition and Multiplication 2 
https://atcoder.jp/contests/abc257/tasks/abc257_e
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
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

def main():
    N = int(input())
    C = [0] + list(map(int, input().split()))

    # find cheapest digit to max num ops
    mn = 1
    for i in range(2, 10):
        if C[i] <= C[mn]: 
            mn = i

    # greedily change for 9, 8, 7, ...
    cnt = [0] * 10
    cnt[mn], rem = divmod(N, C[mn])

    for i in range(9, mn, -1):
        if not rem: break
        use, rem = divmod(rem, C[i] - C[mn])
        cnt[mn] -= use
        cnt[i] += use

    # final answers have form (9..9)(8..8)..(1..1), 1 digit for each op
    res = ''
    for i in range(9, 0, -1):
        res += str(i) * cnt[i]
    print(res)


if __name__ == '__main__':
    main()

