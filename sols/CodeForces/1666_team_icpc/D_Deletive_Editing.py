''' D. Deletive Editing
https://codeforces.com/contest/1666/problem/D
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

def solve(S, T):
    selected = [0] * len(S)
    j = len(S) - 1
    for i in range(len(T)-1, -1, -1):
        while j >= 0 and S[j] != T[i]: j -= 1
        if j < 0: return False
        for k in range(j + 1, len(S)):
            if S[k] == T[i] and not selected[k]:
                return False
        selected[j] = 1
        j -= 1
    return True


def main():
    T = int(input())
    for _ in range(T):
        S, T = input().strip().decode().split()
        out = solve(S, T)
        print('YES' if out else 'NO')


if __name__ == '__main__':
    main()

