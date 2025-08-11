''' C. Bakry and Partitioning
https://codeforces.com/contest/1592/problem/C
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode() if str
output = sys.stdout.write

# RE without
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

# if XOR of all nodes is 0, then can partition into any 2 trees
# if XOR of all nodes is S != 0, then check if can partition into 3 trees with XOR S
def solve(N, K, vals, edges):
    S = 0
    for v in vals: S ^= v
    if S == 0: return 'YES'
    if K == 2: return 'NO'

    adj = [set() for _ in range(N)]
    for u,v in edges:
        adj[u-1].add(v-1)
        adj[v-1].add(u-1)

    # returns (xor, (lv, par, child)) where
    # xor = XOR of subtree rooted at par
    # (par, child) is edge under subtree rooted at par s.t.
    #   * subtree rooted at child has XOR = S
    #   * child is at lv
    #   * lv is as large as possible
    @bootstrap
    def dfs(root, lv, par=-1):  
        xor = vals[root]
        mx_lv = mx_u = mx_v = -1
        for nei in adj[root]:
            if nei == par: continue
            xor_nei, (lv_nei, u_nei, v_nei) = yield dfs(nei, lv+1, root)
            xor ^= xor_nei
            if lv_nei > mx_lv: mx_lv, mx_u, mx_v = lv_nei, u_nei, v_nei
        
        # try disconnecting (par, root)
        if mx_lv == -1 and par != -1 and xor == S:
            mx_lv, mx_u, mx_v = lv, par, root
        
        yield (xor, (mx_lv, mx_u, mx_v))

    # find lowest subtree with xor = S
    _, (lv, u, v) = dfs(0, 0)
    if lv == -1: return 'NO'

    # disconnect first subtree, and find 2nd subtree with xor = S
    adj[u].remove(v)
    adj[v].remove(u)
    _, (lv, _, _) = dfs(0, 0)
    if lv == -1: return 'NO'

    return 'YES'


def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        vals = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for _ in range(N-1)]
        out = solve(N, K, vals, edges)
        output(out + '\n')

if __name__ == '__main__':
    main()