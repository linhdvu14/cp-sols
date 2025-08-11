''' D - Index Trio
https://atcoder.jp/contests/abc249/tasks/abc249_d
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
    cnt = {}
    for a in A: cnt[a] = cnt.get(a, 0) + 1

    res = 0
    for i, ci in cnt.items():
        j = 1
        while j * j < i:
            k, r = divmod(i, j)
            if r == 0 and j in cnt and k in cnt:
                res += 2 * ci * cnt[j] * cnt[k]
            j += 1
        if j * j == i and j in cnt: res += ci * cnt[j] * cnt[j]
    
    print(res)
                



if __name__ == '__main__':
    main()

