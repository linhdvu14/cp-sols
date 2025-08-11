''' D - Strange Balls
https://atcoder.jp/contests/abc240/tasks/abc240_d
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

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    res, stack = [], []
    cnt = 0
    for a in A:
        if stack and stack[-1][0] == a:
            stack[-1][1] += 1
            if stack[-1][1] == a:
                stack.pop()
                cnt -= a
        else:
            stack.append([a, 1])
        cnt += 1
        res.append(cnt)
    return res




if __name__ == '__main__':
    out = main()
    print('\n'.join(map(str, out)))

