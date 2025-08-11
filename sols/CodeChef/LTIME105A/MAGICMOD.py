''' Magical Modulo
https://www.codechef.com/LTIME105A/problems/MAGICMOD
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

def solve(N, A):
    if len(set(A)) < N: return 'NO'
    if len(set(a for a in A if 1 <= a <= N)) == N: return f'YES {N+1}'

    S = sum(A) - N * (N+1) // 2
    d = 1
    while d * d <= S:
        sd, r = divmod(S, d)
        if r == 0:
            if len(set(a % d for a in A if 1 <= a % d <= N)) == N: return f'YES {d}'
            if len(set(a % sd for a in A if 1 <= a % sd <= N)) == N: return f'YES {sd}'
        d += 1
    return 'NO'


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        output(f'{out}\n')


if __name__ == '__main__':
    main()

