''' B - Unique Nicknames
https://atcoder.jp/contests/abc247/tasks/abc247_b
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

    A = []
    cnt = {}
    for _ in range(N):
        s, t = input().strip().decode().split()
        ls = [s, t] if s != t else [s]
        A.append(ls)
        for s in ls: cnt[s] = cnt.get(s, 0) + 1
    
    for ls in A:
        if all(cnt[s] > 1 for s in ls):
            return 'No'

    return 'Yes'


if __name__ == '__main__':
    out = main()
    print(out)

