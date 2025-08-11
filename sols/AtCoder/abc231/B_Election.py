''' B - Election
https://atcoder.jp/contests/abc231/tasks/abc231_b
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

def main():
    N = int(input())
    cnt = {}
    mx = (0, '')
    for _ in range(N):
        s = input().decode().strip()
        cnt[s] = cnt.get(s, 0) + 1
        mx = max(mx, (cnt[s], s))
    print(mx[1])



if __name__ == '__main__':
    main()

