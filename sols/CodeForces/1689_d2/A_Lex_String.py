''' A. Lex String
https://codeforces.com/contest/1689/problem/A
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

def solve(N, M, K, A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    res = ''
    ca = cb = 0
    while A and B:
        if ca == K:
            res += B.pop()
            ca = 0
            cb = 1
        elif cb == K:
            res += A.pop()
            ca = 1
            cb = 0
        elif A[-1] < B[-1]:
            res += A.pop()
            ca += 1
            cb = 0
        else:
            res += B.pop()
            ca = 0
            cb += 1

    return ''.join(res)



def main():
    T = int(input())
    for _ in range(T):
        N, M, K = list(map(int, input().split()))
        A = list(input().decode().strip())
        B = list(input().decode().strip())
        out = solve(N, M, K, A, B)
        print(out)


if __name__ == '__main__':
    main()

