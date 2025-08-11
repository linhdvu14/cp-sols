''' D - Cylinder
https://atcoder.jp/contests/abc247/tasks/abc247_d
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

from collections import deque

def main():
    Q = int(input())
    queue = deque([])
    
    res = []
    for _ in range(Q):
        ts = list(map(int, input().split()))
        if ts[0] == 1:
            x, c = ts[1:]
            queue.append((x, c))
        else:
            rem = ts[1]
            s = 0
            while rem:
                x, c = queue.popleft()
                use = min(rem, c)
                s += x * use
                rem -= use
                c -= use
                if c: queue.appendleft((x, c))
            res.append(s)

    print('\n'.join(map(str, res)))


if __name__ == '__main__':
    main()

