''' E. Anya's Simultaneous Exhibition
https://codeforces.com/contest/1779/problem/E
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

# add edge A -> B if A wins B
# A is CM if A can reach all nodes
# if num non-CMs is x, then a CM wins >= x and a non-CM wins <= x - 1
# so any CM wins strictly more than any non-CM

def ask(i, s):
    s = ''.join(map(str, s))
    output(f'? {i + 1} {s}')
    res = int(input())
    assert res != -1
    return res


def main():
    N = int(input())

    # group by total wins 
    cands = [[] for _ in range(N)]
    s = [1] * N
    for i in range(N):
        s[i] = 0
        w = ask(i, s)
        cands[w].append(i)
        s[i] = 1
    
    # find non-CM cutoff
    # CM if can win any known CMs
    s = [0] * N 
    found = 0
    unk = []
    for w in range(N - 1, -1, -1):
        if not cands[w]: continue
        if not found or any(ask(i, s) for i in cands[w]):
            for i in cands[w]: s[i] = 1
            while unk: s[unk.pop()] = 1
            found = 1
        else:
            unk.extend(cands[w])
    
    s = ''.join(map(str, s))
    res = output(f'! {s}')
    assert res != -1
    
 
if __name__ == '__main__':
    main()