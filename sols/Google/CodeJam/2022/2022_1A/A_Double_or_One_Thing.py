''' Double or One Thing 
https://codingcompetitions.withgoogle.com/codejam/round/0000000000877ba5/0000000000aa8e9c
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

def solve(S):
    res = ''
    N = len(S)
    for i, c in enumerate(S):
        j = i
        while j < N and S[j] == c: j += 1
        if j < N and S[j] > c: res += 2*c
        else: res += c
    return res


def main():
    T = int(input())
    for t in range(T):
        S = input().decode().strip()
        out = solve(S)
        print(f'Case #{t+1}: {out}')


if __name__ == '__main__':
    main()

