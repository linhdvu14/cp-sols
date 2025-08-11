''' DMOPC '22 Contest 3 P2 - New Components
https://dmoj.ca/problem/dmopc22c3p2
'''

import os, sys
input = sys.stdin.readline  # strip() if str

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

def main():
    N, Q = list(map(int, input().split()))
    P = [0] + list(map(int, input().split()))

    # count existing cycles
    cycle = [0] * (N + 1)
    cnt = 0
    for i in range(1, N + 1):
        if cycle[i]: continue
        cnt += 1
        while not cycle[i]:
            cycle[i] = cnt
            i = P[i]

    # count num connected components w/o S
    # each full cycle within S erases 1 component
    # each partial cycle arc within S (from 2nd onwards) adds 1 component
    res = [-1] * Q
    use_node = [0] * (N + 1)
    use_cycle = [0] * (cnt + 1)
    for qi in range(Q):
        _ = input()
        S = set(map(int, input().split()))
        full = partial = 0
        for beg in S:
            if use_node[beg]: continue
            end = beg 
            while end in S and not use_node[end]:
                use_node[end] = 1
                end = P[end]
            if end == beg: 
                full += 1
            elif end not in S:
                if not use_cycle[cycle[beg]]: use_cycle[cycle[beg]] = 1
                else: partial += 1

        res[qi] = cnt - full + partial
        for u in S: use_node[u] = use_cycle[cycle[u]] = 0

    print(*res, sep='\n')



if __name__ == '__main__':
    main()

