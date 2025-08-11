''' D. Progressions Covering
https://codeforces.com/contest/1661/problem/D
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

def solve(N, K, B):
    # a = current value of A[i] before adding new sequences
    # d = current difference between consecutive ele
    # rm[i] = how many sequences start at idx i / will be removed after processing idx i
    res = a = d = 0
    rm = [0] * N

    for i in range(N-1, -1, -1):
        if a < B[i]:  # add enough sequences, as left as possible to cover difference
            j = max(0, i - K + 1)         # optimal sequence start
            v = i - j + 1                 # how much one sequence will increase A[i]
            n = (B[i] - a + v - 1) // v   # how many sequences to add
            
            a += v * n
            rm[j] += n
            d += n
            res += n

        # step down to prepare for next ele
        a -= d
        d -= rm[i]
    
    return res


def main():
    N, K = list(map(int, input().split()))
    B = list(map(int, input().split()))
    out = solve(N, K, B)
    print(out)


if __name__ == '__main__':
    main()

