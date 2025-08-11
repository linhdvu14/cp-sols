''' Image Labeler 
https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caea6/0000000000b76e11
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

def solve(N, M, A):
    A.sort(reverse=True)
    res = sum(A[:M-1])
    A = A[M-1:]
    if len(A) % 2: res += A[len(A)//2]
    else: res += (A[len(A)//2 - 1] + A[len(A) // 2]) / 2
    return res


def main():
    T = int(input())
    for t in range(T):
        N, M = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(N, M, A)
        print(f'Case #{t+1}: {out}')


if __name__ == '__main__':
    main()

