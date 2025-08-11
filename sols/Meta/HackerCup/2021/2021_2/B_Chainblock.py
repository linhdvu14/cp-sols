''' Problem B: Chainblock
https://www.facebook.com/codingcompetitions/hacker-cup/2021/round-2/problems/B
'''

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


def solve(N, edges, freqs):
    adj = [[] for _ in range(N)]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # count of each unique val
    count = {}
    for f in freqs:
        count[f] = count.get(f, 0) + 1

    # try rm each edge
    res = 0
    
    # returns (num unique vals under this subtree, how many of those vals only exist under this subtree)
    @bootstrap
    def dfs(u, parent=-1):
        nonlocal res
        subtree_cnt, subtree_full = {}, 0
        for v in adj[u]:
            if v==parent: continue
            child_cnt, child_full = yield dfs(v, u)
            subtree_full += child_full
            if len(child_cnt) > len(subtree_cnt): subtree_cnt, child_cnt = child_cnt, subtree_cnt
            for f, cnt in child_cnt.items():
                subtree_cnt[f] = subtree_cnt.get(f, 0) + cnt
                if cnt < count[f] and subtree_cnt[f] == count[f]: subtree_full += 1
        f = freqs[u]
        subtree_cnt[f] = subtree_cnt.get(f, 0) + 1
        if subtree_cnt[f] == count[f]: subtree_full += 1
        if parent != -1 and subtree_full == len(subtree_cnt): res += 1  # edge (u,parent) can be rm
        yield subtree_cnt, subtree_full

    dfs(0)
    return res            



def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())
    for t in range(T):
        N = int(stdin.readline().strip())
        edges = []
        for _ in range(N-1):
            a, b = list(map(int, stdin.readline().strip().split()))
            edges.append((a-1,b-1))
        freqs = list(map(int, stdin.readline().strip().split()))
        out = solve(N, edges, freqs)
        print(f'Case #{t+1}: {out}')



if __name__ == '__main__':
    main()
