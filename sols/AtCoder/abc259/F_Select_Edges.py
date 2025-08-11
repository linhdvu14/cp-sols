''' F - Select Edges
https://atcoder.jp/contests/abc259/tasks/abc259_f
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


# greedy max edge bad case: (1) -9- (1) -10- (1) -9- (1)

def main():
    N = int(input())
    D = list(map(int, input().split()))

    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = list(map(int, input().split()))
        u -= 1; v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))

    # dp0[u] = max values for u's subtree, if edge (par[u], u) is not selected
    # dp1[u] = max values for u's subtree, if edge (par[u], u) is selected
    dp0, dp1 = [0] * N, [0] * N 

    @bootstrap
    def dfs(u, p=-1):
        s = 0  # score if select no subtree
        gain = []
        for v, w in adj[u]:
            if v == p: continue
            yield dfs(v, u)
            s += dp0[v]
            if D[v]: gain.append(dp1[v] + w - dp0[v])
        gain.sort(reverse=True)

        dp0[u] = s
        for i in range(D[u]):
            if i >= len(gain) or gain[i] <= 0: break
            dp0[u] += gain[i]
        
        if p != -1 and D[p]:
            dp1[u] = s
            for i in range(D[u] - 1):
                if i >= len(gain) or gain[i] <= 0: break
                dp1[u] += gain[i]
        
        yield None

    dfs(0)

    print(dp0[0])


if __name__ == '__main__':
    main()

