''' D. Integral Array
https://codeforces.com/contest/1649/problem/D
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

def solve(N, C, A):
    cnt = [0] * (C+1)
    for a in A: cnt[a] += 1
    if cnt[1] == 0: return False

    pref = [0]
    for a in range(1, C+1): pref.append(pref[-1] + cnt[a])

    # fix y
    # if A has x=y..2y-1 then A should have 1
    #         x=2y..3y-1                    2
    #         x=3y..4y-1                    3 
    # ... --> N log N
    for y in range(1, C+1):
        if cnt[y] == 0: continue
        for l in range(y, C+1, y):
            r = min(l+y-1, C)
            if pref[r] - pref[l-1] > 0 and pref[r // y] == pref[r // y - 1]:
                return False
    return True


def main():
    T = int(input())
    for _ in range(T):
        N, C = list(map(int, input().split()))
        A = list(map(int, input().split()))
        out = solve(N, C, A)
        print('Yes' if out else 'No')


if __name__ == '__main__':
    main()

