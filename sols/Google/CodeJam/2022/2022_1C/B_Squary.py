''' Squary
https://codingcompetitions.withgoogle.com/codejam/round/0000000000877b42/0000000000afdf76
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

# let S(A) = sum(A), P(A) = sum A[i] * A[j]
# then P(A + [b]) = P(A) + S(A) * b
# want to add B s.t. P(A + B) = 0

def solve(N, K, A):
    s = p = 0
    for i in range(N):
        s += A[i]
        for j in range(i):
            p += A[i] * A[j]
    
    # p + bs = 0 -> b = -p/s
    if K == 1:
        if s == p == 0: return [0]
        if s != 0 and p % s == 0: return [-p//s]
        return ['IMPOSSIBLE']

    # P(A + [b, c]) = P(A + [b]) + S(A + [b]) * c
    # b = 1 - S(A); c = -P(A + [b])
    b = 1 - s
    c = -p - s*b
    assert p + s*(b+c) + b*c == 0
    return [b, c]



def main():
    T = int(input())
    for t in range(T):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(N, K, A)
        print(f'Case #{t+1}: ', end='')
        print(*out)


if __name__ == '__main__':
    main()

