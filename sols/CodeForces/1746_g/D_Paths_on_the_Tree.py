''' D. Paths on the Tree
https://codeforces.com/contest/1746/problem/D
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

class IntKeyDict(dict):
    from random import randrange
    rand = randrange(1 << 62)
    def __setitem__(self, k, v): super().__setitem__(k^self.rand, v)
    def __getitem__(self, k): return super().__getitem__(k^self.rand)
    def __contains__(self, k): return super().__contains__(k^self.rand)
    def __repr__(self): return str({k: v for k, v in self.items()})
    def get(self, k, default=None): return super().get(k^self.rand, default)
    def keys(self): return [k^self.rand for k in super().keys()]
    def items(self): return [(k^self.rand, v) for k, v in super().items()]

INF = float('inf')

# -----------------------------------------

# c[u] = num paths ending in u's subtree
# c[v] = c[u] / num_child(u) (+ 1) for each chid v of u
# can assign for any c[u] value
# path should only end at leaf nodes

def solve(N, K, P, S):
    adj = [[] for _ in range(N)]
    for u, v in enumerate(P):
        u += 1
        v -= 1
        adj[v].append(u)
    
    # best way to assign n paths to u's subtree
    # return best gain if assign 1 more path to u's subtree
    @bootstrap
    def dfs(u, n):
        nonlocal res 
        res += S[u] * n
        if not adj[u]: yield S[u]

        choices = []
        nc, rem = divmod(n, len(adj[u]))
        for v in adj[u]:
            gain = yield dfs(v, nc)
            choices.append(gain)
        choices.sort(reverse=True)
        res += sum(choices[:rem])

        yield S[u] + choices[rem]

    res = 0
    dfs(0, K)

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        P = list(map(int, input().split()))
        S = list(map(int, input().split()))
        res = solve(N, K, P, S)
        print(res)


if __name__ == '__main__':
    main()

