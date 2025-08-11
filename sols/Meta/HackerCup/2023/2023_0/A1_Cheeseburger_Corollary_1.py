''' Problem A1: Cheeseburger Corollary 1
https://www.facebook.com/codingcompetitions/hacker-cup/2023/practice-round/problems/A1
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

def solve(S, D, K):
    bun = (S + D) * 2
    cheese = S + D * 2
    if bun >= K + 1 and cheese >= K: return 'YES'
    return 'NO'


def main():
    T = int(input())
    for t in range(T):
        S, D, K = list(map(int, input().split()))
        res = solve(S, D, K)
        print(f'Case #{t + 1}: {res}')


if __name__ == '__main__':
    main()

