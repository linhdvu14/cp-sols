''' B. Fibonacci Cubes
https://codeforces.com/contest/2111/problem/B
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
FIB = [0, 1, 2]
for _ in range(10): FIB.append(FIB[-1] + FIB[-2])

def solve(N, M, boxes):
    a, b = FIB[N], FIB[N - 1]
    
    res = [0] * M 
    for i, (w, l, h) in enumerate(boxes):
        if a <= min(w, l, h) and a + b <= max(w, l, h):
            res[i] = 1

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        boxes = [list(map(int, input().split())) for _ in range(M)]
        res = solve(N, M, boxes)
        print(*res, sep='')


if __name__ == '__main__':
    main()

