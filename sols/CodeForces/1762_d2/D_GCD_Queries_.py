''' D. GCD Queries
https://codeforces.com/contest/1762/problem/D
'''

import functools
import os, sys
input = sys.stdin.readline  # strip() if str; io.BytesIO(os.read(0,os.fstat(0).st_size)).readline doesn't work
output = functools.partial(print, flush=True)

DEBUG = os.environ.get('debug') not in [None, '0']

def debug(*args):   
    if not DEBUG: return
    from inspect import currentframe, getframeinfo
    from re import search
    frame = currentframe().f_back
    s = getframeinfo(frame).code_context[0]
    r = search(r"\((.*)\)", s).group(1)
    vnames = r.split(', ')
    var_and_vals = [f'{var}={val}' for var, val in zip(vnames, args)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(var_and_vals)}')

INF = float('inf')

# -----------------------------------------

def ask(x, y, final=False):
    if final: output(f'! {x + 1} {y + 1}')
    else: output(f'? {x + 1} {y + 1}')
    res = int(input())
    assert res != -1
    return res


# consider triplet (a, b, c)
# - gcd(a, b) == gcd(a, c) -> a != 0
# - gcd(a, b) < gcd(a, c) -> gcd(a, b) < a, b != 0
def solve(N):
    cands = set(range(N))
    while len(cands) > 2:
        a, b, c = cands.pop(), cands.pop(), cands.pop()
        ab = ask(a, b)
        ac = ask(a, c)
        if ab == ac: cands.update([b, c])
        elif ab < ac: cands.update([c, a])
        else: cands.update([a, b])
    
    a, b = cands.pop(), cands.pop()
    ask(a, b, final=True)



def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        solve(N)
    
 
if __name__ == '__main__':
    main()
