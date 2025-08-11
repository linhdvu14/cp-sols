''' A. Square of Rectangles
https://codeforces.com/contest/2120/problem/A
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

def solve(l1, b1, l2, b2, l3, b3):
    if l1 == l2 == l3 == b1 + b2 + b3: return True
    if b1 == b2 == b3 == l1 + l2 + l3: return True 
    if l2 == l3 and b2 + b3 == b1 == l1 + l2: return True 
    if b2 == b3 and l2 + l3 == l1 == b1 + b2: return True 
    return False


def main():
    T = int(input())
    for _ in range(T):
        l1, b1, l2, b2, l3, b3 = list(map(int, input().split()))
        res = solve(l1, b1, l2, b2, l3, b3)
        print('YES' if res else 'NO')


if __name__ == '__main__':
    main()

