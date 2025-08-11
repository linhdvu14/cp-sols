''' Weightlifting 
https://codingcompetitions.withgoogle.com/codejam/round/0000000000877ba5/0000000000aa9280
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

def next_permutation(P):
    '''change P inplace to next-greater permutation'''
    N = len(P)

    # l = max i s.t. P[i] < P[i+1]
    l = -1
    for i in range(N-2, -1, -1):
        if P[i] < P[i+1]: 
            l = i
            break
    
    # max P alr
    if l == -1: return False
    
    # r = max i > l s.t. P[r] > P[l]
    for r in range(N-1, l, -1):
        if P[r] > P[l]:
            break
    
    # reverse
    P[l], P[r] = P[r], P[l]
    P[l+1:] = reversed(P[l+1:])
    return True


def solve_t1(E, W, X):
    # gen all states for each exercise
    states = [[] for _ in range(E)]
    for i, x in enumerate(X):
        s = ''.join(str(j+1) * v for j, v in enumerate(x))
        states[i].append(s)
        s = list(s)
        while next_permutation(s): states[i].append(''.join(s))

    # cost between adjacent exercise states
    def cost(s1, s2):
        n = min(len(s1), len(s2))
        save = n
        for i in range(n):
            if s1[i] != s2[i]:
                save = i
                break
        return len(s1) + len(s2) - 2 * save

    # dp[i][s] = min cost to finish exercise i at state s
    dp = [{} for _ in range(E)]
    for s in states[0]: dp[0][s] = len(s)
    for i in range(1, E):
        for s in states[i]:
            dp[i][s] = INF
            for ps in states[i-1]:
                dp[i][s] = min(dp[i][s], dp[i-1][ps] + cost(s,ps))

    return min(dp[-1].values()) + len(states[-1][0])


# ? http://www.usaco.org/current/data/sol_prob2_bronze_dec21.html
# probably cannot apply as weights are ordered / not independent
def solve_t2(E, W, X):
    # common[l][r] = size of weight multiset intersection for exercises l..r
    common = [[0] * E for _ in range(E)]
    for l in range(E):
        mn = X[l][:]
        for r in range(l, E):
            for w in range(W):
                mn[w] = min(mn[w], X[r][w])
                common[l][r] += mn[w]

    # dp[l][r] = min num ops if start from empty stack, do exercises l..r, then back to empty stack
    dp = [[INF] * E for _ in range(E)]
    for i in range(E): dp[i][i] = 2 * common[i][i]

    # should always share common[l][r] for all exercises l..r
    # try each possible split point i and recursively solve l..i, i+1..r
    # when i is optimal, intersection of W[i] and W[i+1] is exactly common[l][r]
    for d in range(1, E):
        for l in range(E-d):
            r = l + d
            for i in range(l, r):  # cut between i and i+1
                dp[l][r] = min(dp[l][r], dp[l][i] + dp[i+1][r] - 2 * common[l][r])
    
    return dp[0][E-1]


solve = solve_t2

def main():
    T = int(input())
    for t in range(T):
        E, W = list(map(int, input().split()))
        X = [list(map(int, input().split())) for _ in range(E)]
        out = solve(E, W, X)
        print(f'Case #{t+1}: {out}')


if __name__ == '__main__':
    main()

