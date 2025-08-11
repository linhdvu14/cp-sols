''' C - Circular Addition 
https://atcoder.jp/contests/arc136/tasks/arc136_c
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

# usaco 2021-12 bronze B
# http://www.usaco.org/current/data/sol_prob2_bronze_dec21.html

def main():
    N = int(input())
    A = list(map(int, input().split()))
    m = d = 0
    for i in range(N):
        m = max(m, A[i])
        d += abs(A[i] - A[i-1])
    return max(m, (d+1)//2)



if __name__ == '__main__':
    out = main()
    print(out)

