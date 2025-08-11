''' D. Peculiar Movie Preferences
https://codeforces.com/contest/1629/problem/D
'''

import io, os, sys
from tkinter.messagebox import RETRY
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

def solve(N, strs):
    if any(len(set(s)) == 1 for s in strs): return True
    if any(s[0] == s[-1] for s in strs): return True
    
    seen, seen2 = set(), set()
    for s in strs: 
        if s[::-1] in seen: return True  # same length pair
        if len(s) == 3 and s[1:][::-1] in seen: return True
        if len(s) == 2 and s[::-1] in seen2: return True
        if len(s) == 3: seen2.add(s[:2])
        seen.add(s)

    return False


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        strs = [input().decode().strip() for _ in range(N)]
        out = solve(N, strs)
        print('YES' if out else 'NO')


if __name__ == '__main__':
    main()

