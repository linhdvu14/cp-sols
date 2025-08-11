''' D - LR insertion
https://atcoder.jp/contests/abc237/tasks/abc237_d
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

from collections import deque

def main():
    N = int(input())
    S = input().decode().strip()

    res = deque([N])
    for i in range(N-1, -1, -1):
        if S[i] == 'L': res.append(i)
        else: res.appendleft(i)

    print(*res)


if __name__ == '__main__':
    main()