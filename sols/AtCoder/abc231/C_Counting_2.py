''' C - Counting 2
https://atcoder.jp/contests/abc231/tasks/abc231_c
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

from bisect import bisect_left

def main():
    N, Q = list(map(int, input().split()))
    A = sorted(list(map(int, input().split())))

    res = []
    for _ in range(Q):
        x = int(input())
        res.append(len(A) - bisect_left(A, x))
    
    print(*res, sep='\n')



if __name__ == '__main__':
    main()

