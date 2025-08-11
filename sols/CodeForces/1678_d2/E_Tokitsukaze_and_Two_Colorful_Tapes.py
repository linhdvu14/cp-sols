''' E. Tokitsukaze and Two Colorful Tapes
https://codeforces.com/contest/1678/problem/E
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

# within a cycle, num peaks == num valleys
# can always make 1 peak and 1 valley to get 2 * (peak - valley)
# any (peak - valley) > 0 so optimal to max num peaks and num valleys
# make larger ln//2 values peaks and smaller ln//2 values valleys

def solve(N, A, B):
    P = [-1] * N
    for a, b in zip(A, B):
        P[a-1] = b-1

    seen = [0] * N
    peaks = 0
    for i in range(N):
        ln = 0
        while not seen[i]:
            ln += 1
            seen[i] = 1
            i = P[i]
        peaks += ln // 2
    
    res = sum(2 * (N - i) - 2 * (i + 1) for i in range(peaks))
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        out = solve(N, A, B)
        print(out)


if __name__ == '__main__':
    main()

