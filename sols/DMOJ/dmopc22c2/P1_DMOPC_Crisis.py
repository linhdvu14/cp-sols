''' DMOPC '22 Contest 2 P1 - DMOPC Crisis
https://dmoj.ca/problem/dmopc22c2p1
'''

import os, sys
input = sys.stdin.readline  # strip() if str

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

def main():
    N = int(input())
    res = '__MM' * (N // 4)
    if N % 4 == 1: res += '_'
    elif N % 4 == 2: res += '__'
    elif N % 4 == 3: res += '__M'

    print(res.count('M'))
    print(res)



if __name__ == '__main__':
    main()

