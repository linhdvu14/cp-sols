''' Problem A1: Perfectly Balanced - Chapter 1
https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-2/problems/A1
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

def solve(S, Q, queries):
    pref = [[0] * 26]
    for c in S:
        cnt = pref[-1][:]
        cnt[ord(c) - ord('a')] += 1
        pref.append(cnt)
    
    def is_ok(l, r):
        if (r - l + 1) % 2 == 0: return False
        l -= 1; r -= 1
        m = (l + r) // 2
        cl = cr = 0
        for c in range(26): 
            if pref[m + 1][c] - pref[l][c] != pref[r + 1][c] - pref[m + 1][c]: cl += 1
            if pref[m][c] - pref[l][c] != pref[r + 1][c] - pref[m][c]: cr += 1
        return cl == 1 or cr == 1
        
    res = 0
    for l, r in queries:
        if is_ok(l, r):
            res += 1

    return res


def main():
    T = int(input())
    for t in range(T):
        S = input().strip()
        Q = int(input())
        queries = [list(map(int, input().split())) for _ in range(Q)]
        res = solve(S, Q, queries)
        print(f'Case #{t+1}: {res}')


if __name__ == '__main__':
    main()

