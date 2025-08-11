''' C. awoo's Favorite Problem
https://codeforces.com/contest/1697/problem/C
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

# consider parallel blocks of (a, b) and (b, c)
# for (a, b), can sort if index of i-th b in S <= index of i-th b in T
# for (b, c), can sort if index of i-th c in S <= index of i-th c in T
def solve_1(N, S, T):
    S = [0 if c == 'a' else 1 if c == 'b' else 2 for c in S]
    T = [0 if c == 'a' else 1 if c == 'b' else 2 for c in T]

    i = 0
    while i < N:
        v = S[i]
        if v == T[i]:
            i += 1
        elif v == 2:
            return 'NO'
        else:
            idx_S, idx_T = [], []
            j = i
            while j < N and S[j] != (v + 2) % 3 and T[j] != (v + 2) % 3:
                if S[j] == v + 1: idx_S.append(j)
                if T[j] == v + 1: idx_T.append(j)
                j += 1
            if not idx_S or len(idx_S) != len(idx_T): return 'NO'
            if any(si < ti for si, ti in zip(idx_S, idx_T)): return 'NO'
            i = j
        
    return 'YES'


# check if can sort by moving a down through b's or c up through b's
def solve_2(N, S, T):
    if any(S.count(c) != T.count(c) for c in 'abc'): return 'NO'

    S_rem = T_rem = ''
    S_idx, T_idx = [], []
    for i, c in enumerate(S):
        if c != 'b': 
            S_rem += c
            S_idx.append(i)
    for i, c in enumerate(T):
        if c != 'b': 
            T_rem += c
            T_idx.append(i)
    
    if S_rem != T_rem: return 'NO'  # a cannot pass through c and vice versa
    for i, (si, ti) in enumerate(zip(S_idx, T_idx)):
        if S_rem[i] == 'a' and si > ti: return 'NO'  # a can only move down
        if S_rem[i] == 'c' and si < ti: return 'NO'  # c can only move up
    
    return 'YES'



solve = solve_2

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = list(input().decode().strip())
        T = list(input().decode().strip())
        out = solve(N, S, T)
        print(out)


if __name__ == '__main__':
    main()
 