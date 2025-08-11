''' C - Just K
https://atcoder.jp/contests/abc249/tasks/abc249_c
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

from string import ascii_lowercase

def main():
    N, K = list(map(int, input().split()))
    strs = [input().decode().strip() for _ in range(N)] 
    res = 0
    for mask in range(1, 1<<N):
        cnt = {}
        for i, s in enumerate(strs):
            if (mask >> i) & 1:
                for c in ascii_lowercase:
                    if c in s:
                        cnt[c] = cnt.get(c, 0) + 1
        n = sum(1 for v in cnt.values() if v == K)
        res = max(res, n)
    print(res)




if __name__ == '__main__':
    main()

