''' Problem A2: Cheeseburger Corollary 2
https://www.facebook.com/codingcompetitions/hacker-cup/2023/practice-round/problems/A2
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
# max k
# a * ca + b * cb <= C
# a + 2b >= k
# 2a + 2b >= k + 1

def solve(ca, cb, C): 
    res = 0
    for a in [0, 1, 2, C // ca]:
        b = (C - a * ca) // cb 
        k = min(2 * a + 2 * b - 1, a + 2 * b)
        res = max(res, k)

    return res


def main():
    T = int(input())
    for t in range(T):
        ca, cb, C = list(map(int, input().split()))
        res = solve(ca, cb, C)
        print(f'Case #{t + 1}: {res}')


if __name__ == '__main__':
    main()

