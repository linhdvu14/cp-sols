''' C. Card Game
https://codeforces.com/contest/2104/problem/C
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

def solve(N, S):
    for i, a in enumerate(S):
        if a != 'A': continue
        win = True
        for j, b in enumerate(S):
            if b != 'B': continue
            if (i == N - 1 and j == 0) or (i < j and not (i == 0 and j == N - 1)):
                win = False
                break
        if win: return True

    return False


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().decode().strip()
        res = solve(N, S)
        print('Alice' if res else 'Bob')


if __name__ == '__main__':
    main()

