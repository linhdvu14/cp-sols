''' Challenge Nine
https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e7997
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

def solve(N):
    S = str(N)
    if N % 9 == 0: return S[:1] + '0' + S[1:]
    d = str(9 - N % 9)
    for i, c in enumerate(S):
        if d < c:
            return S[:i] + d + S[i:]
    return S + d



def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        out = solve(N)
        print(f'Case #{i+1}: {out}')


if __name__ == '__main__':
    main()

