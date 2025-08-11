''' D. Hemose in ICPC ?
https://codeforces.com/contest/1592/problem/D
'''

import functools
import sys
input = sys.stdin.readline  # io.BytesIO(os.read(0,os.fstat(0).st_size)).readline doesn't work
output = functools.partial(print, flush=True)

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

def euler(adj):
    res = []
    @bootstrap
    def tour(root, par=-1):
        res.append(root)
        for nei in adj[root]:
            if nei==par: continue
            yield tour(nei, root)
            res.append(root)
        yield None
    tour(1)
    return res


def solve(N, edges):
    # target = max edge weight between any node pairs
    nodes = map(str, list(range(1, N+1)))
    output(f'? {N} {" ".join(nodes)}')
    target = int(input())

    # after euler tour, any subarray is a component whose nodes are connected by edges within subarray
    adj = [[] for _ in range(N+1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    tour = euler(adj)

    # bin search to find component containing target edge
    def query(lo, hi):
        nodes = list(set(str(u) for u in tour[lo:hi+1]))
        output(f'? {len(nodes)} {" ".join(nodes)}')
        res = int(input())
        return res

    lo, hi = 0, len(tour)-1
    while True:
        mi = (lo + hi) // 2
        res = query(lo, mi)
        if res == target:  # target pair in lo..mi
            hi = mi
        else:  # target pair in mi..hi
            lo = mi
        if lo+1 == hi:
            output(f'! {tour[lo]} {tour[hi]}')
            return


def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    solve(N, edges)
    
 
if __name__ == '__main__':
    main()