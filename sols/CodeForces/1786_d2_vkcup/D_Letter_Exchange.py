''' D. Letter Exchange
https://codeforces.com/contest/1786/problem/D
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

WIN = 'win'

def solve(N, S):
    have = [[[] for _ in range(3)] for _ in range(3)]

    for i, s in enumerate(S):
        cnt = [0] * 3
        for c in s:
            if c == 'w': cnt[0] += 1
            elif c == 'i': cnt[1] += 1
            else: cnt[2] += 1
        
        give, take = [], []
        for j in range(3):
            if cnt[j] == 0: take.append(j)
            elif cnt[j] > 1: give += [j] * (cnt[j] - 1)
        
        for gv, tk in zip(give, take):
            have[gv][tk].append(i + 1)

    res = []
    for gv in range(3):
       for tk in range(3):
            while have[gv][tk] and have[tk][gv]:
                i = have[gv][tk].pop()
                j = have[tk][gv].pop()
                res.append([i, WIN[gv], j, WIN[tk]])
    
    # only wwi/iin/nww now
    while have[0][1]:
        i, j, k = have[0][1].pop(), have[1][2].pop(), have[2][0].pop()
        res.append([i, WIN[0], j, WIN[1]])
        res.append([j, WIN[0], k, WIN[2]])
    
    while have[0][2]:
        i, j, k = have[0][2].pop(), have[2][1].pop(), have[1][0].pop()
        res.append([i, WIN[0], j, WIN[2]])
        res.append([j, WIN[0], k, WIN[1]])

    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = [input().decode().strip() for _ in range(N)]
        res = solve(N, S)
        print(len(res))
        for t in res: print(*t)


if __name__ == '__main__':
    main()

