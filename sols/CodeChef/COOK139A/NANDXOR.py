''' Dragonado And XOR
https://www.codechef.com/COOK139A/problems/NANDXOR
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
    # 31 adjacent pairs, at least 2 has same popcount
    if N >= 62:
        seen = {}
        for i in range(0, 31, 2):
            x = bin(A[i] ^ A[i+1]).count('1')
            if x in seen: return [seen[x][0]+1, seen[x][1]+1, i+1, i+2]
            seen[x] = (i, i+1)
    else:
        for i1 in range(N):
            for i2 in range(N):
                for i3 in range(N):
                    for i4 in range(N):
                        if len(set([i1, i2, i3, i4])) < 4: continue
                        if bin(A[i1] ^ A[i2]).count('1') == bin(A[i3] ^ A[i4]).count('1'):
                            return [i1+1, i2+1, i3+1, i4+1]
    return [-1]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        print(*out)


if __name__ == '__main__':
    main()

