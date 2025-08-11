''' Split AND Sum
https://www.codechef.com/COOK142A/problems/SPLITANDSUM
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

# find first bit (from lsb) with >= 2 eles
# all lower bits have 0 or 1 occurrences, so do not affect current bit and higher

def solve(N, A):
    for b in range(30):
        idx = []
        for i, a in enumerate(A):
            if (a >> b) & 1:
                idx.append(i + 1)
        if len(idx) >= 2: 
            res = [(1, idx[0])]
            for i in range(len(idx) - 2): res.append((idx[i] + 1, idx[i+1]))
            res.append((idx[-2] + 1, N))
            return res

    return []


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out = solve(N, A)
        if not out: print('NO')
        else:
            sand = (1 << 30) - 1
            for l, r in out: 
                s = sum(A[l-1:r])
                sand &= s
            assert sand != 0
            print('YES')
            print(len(out))       
            for x in out: print(*x)


if __name__ == '__main__':
    main()

