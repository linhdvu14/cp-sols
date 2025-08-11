''' D - ABC Transform
https://atcoder.jp/contests/abc242/tasks/abc242_d
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

# length of S at time t is N << i

# char c at idx i will spawn into
# * char (c+1) % 3 at idx 2*i
# * char (c+2) % 3 at idx 2*i + 1
# at the next time step


def main():
    S = input().decode().strip()
    S = [ord(c) - ord('A') for c in S]
    Q = int(input())

    res = []
    for _ in range(Q): 
        t, k = map(int, input().split())
        k -= 1
        shift = 0
        while t > 0 and k > 0: 
            if k % 2 == 0: shift = (shift + 1) % 3
            else: shift = (shift + 2) % 3
            k >>= 1
            t -= 1
        res.append((S[k] + t + shift) % 3)

    res = [chr(i + ord('A')) for i in res]
    print('\n'.join(res))



if __name__ == '__main__':
    main()

