''' Yet Another Contest 3 P2 - Work Experience
https://dmoj.ca/problem/yac3p2
'''

import os, sys
input = sys.stdin.readline  # strip() if str

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

from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack: return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack: break
                to = stack[-1].send(to)
        return to
    return wrappedfunc


# root tree at u; u can be mtg point if
# * >= 2 at u
# * x at u, (y, z) at different subtrees
# * (x, y, z) at different subtrees

def main():
    N = int(input())
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = list(map(int, input().split()))
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
    res, cnt = [1] * N, [1] * N 

    @bootstrap
    def dfs(u, p=-1):
        s1 = s2 = s3 = 0
        for v in adj[u]:
            if v == p: continue
            yield dfs(v, u)
            cnt[u] += cnt[v]
            s1 += cnt[v]
            s2 += cnt[v]**2
            s3 += cnt[v]**3
        s1 += (N - cnt[u])
        s2 += (N - cnt[u])**2
        s3 += (N - cnt[u])**3

        # 2 at u
        res[u] += 3 * (N - 1)

        # x at u, (y, z) at different subtrees
        # (a + b + c) ^ 2 = (a^2 + b^2 + c^2) + 2(ab + bc + ca)
        two = (s1**2 - s2) // 2  
        res[u] += 6 * two

        # (x, y, z) at different subtrees
        # (a + b + c) ^ 3 = (a^3 + b^3 + c^3) + 3(a + b + c)(ab + bc + ca) - 3abc
        res[u] += 2 * (s3 + 3*s1*two - s1**3)
        yield None

    dfs(0)
    print(*res)


if __name__ == '__main__':
    main()

