''' Running in Circles
https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb1b6/0000000000c4766e
'''

import os, sys
input = sys.stdin.readline
output = sys.stdout.write

def debug(*args):   
    if os.environ.get('debug') in [None, '0']: return
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

def solve(L, N, runs):
    res = cur = 0
    mem = ''
    for dist, orient in runs:
        dist = int(dist)
        if not cur: mem = orient 

        if orient == 'C':
            cur += dist 
            t, cur = divmod(cur, L)
            if t:
                res += t - (mem != orient)
                mem = orient
        else:
            if cur and cur <= dist and mem == orient: res += 1
            cur -= dist 
            if cur <= 0:
                mem = orient 
                res += abs(cur) // L
                cur %= L

    return res



def main():
    T = int(input())
    for t in range(T):
        L, N = list(map(int, input().split()))
        runs = [input().strip().split() for _ in range(N)]
        res = solve(L, N, runs)
        print(f'Case #{t+1}: {res}')


if __name__ == '__main__':
    main()
    # gen()

