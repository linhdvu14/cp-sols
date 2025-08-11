''' E. Node Pairs
https://codeforces.com/contest/1763/problem/E
'''

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline  # decode().strip() if str
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

# A = scc sizes in constructed graph
# want to min SUM_i A[i] s.t. SUM_i A[i] * (A[i] - 1) // 2 == N
# to max uni pairs, place sccs in line in ascending size order
def solve(P):
    if P == 0: return 0, 0

    # dp[m][p] = min nodes to make p pairs with scc sizes <= m
    M = int((P * 2) ** 0.5) + 1
    cost = [0] + [INF] * P 
    pair = [0] * (P + 1)
    for m in range(2, M + 1):
        for p in range(1, P + 1):
            np = m * (m - 1) // 2
            if p >= np and cost[p] > cost[p - np] + m:
                cost[p] = cost[p - np] + m
                pair[p] = pair[p - np] + cost[p - np] * m

    return cost[-1], pair[-1]


def main():
    P = int(input())
    res = solve(P)
    print(*res)



if __name__ == '__main__':
    main()


