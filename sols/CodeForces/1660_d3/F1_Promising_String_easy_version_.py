''' F1. Promising String (easy version)
https://codeforces.com/contest/1660/problem/F1
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

# let bal = (num -) minus (num +)
# each non-overlapping '--' can increase balance by 3
# interval i..j is promising if bal % 3 == 0 and num '--' >= bal // 3

def solve_1(N, S):
    res = 0
    for i in range(N):
        bal = add = ln = 0
        for j in range(i, N):
            if S[j] == '-': ln += 1
            if ln == 2: 
                add += 1
                ln = 0
            if S[j] == '-': 
                bal += 1
            else:
                bal -= 1
                ln = 0
            if bal >= 0 and bal % 3 == 0 and bal // 3 <= add: 
                res += 1

    return res


# if cnt(neg) - cnt(pos) >= 3, then there must be '--'
# changing '--' to '+' increases balance by 3
# interval i..j is promising if cnt(neg) >= cnt(pos) and (cnt(neg) - cnt(pos)) % 3 == 0

def solve_2(N, S):
    res = 0
    for i in range(N):
        pos = neg = 0
        for j in range(i, N):
            if S[j] == '+': pos += 1
            else: neg += 1
            if neg >= pos and (neg - pos) % 3 == 0: res += 1
    return res

solve = solve_2

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().decode().strip()
        out = solve(N, S)
        print(out)


if __name__ == '__main__':
    main()

