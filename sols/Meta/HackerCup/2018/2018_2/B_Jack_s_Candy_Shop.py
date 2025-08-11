''' Problem B: Jack's Candy Shop
https://www.facebook.com/codingcompetitions/hacker-cup/2018/round-2/problems/B
'''

from math import ceil, log2

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

class SegmentTreeMax:
    def __init__(self, nums):
        def construct(tree, nums, ti, tlo, thi):  # tree[ti] = max(nums[tlo..thi])
            if tlo == thi:
                tree[ti] = nums[tlo]
            else:
                tmi = tlo + (thi - tlo)//2
                construct(tree, nums, 2*ti+1, tlo, tmi)
                construct(tree, nums, 2*ti+2, tmi+1, thi)
                tree[ti] = max(tree[2*ti+1], tree[2*ti+2])

        height = int(ceil(log2(len(nums))))
        size = 2**(height+1) - 1
        self.tree = [0]*size
        self.N = len(nums)
        construct(self.tree, nums, 0, 0, self.N-1)

    def query_range(self, qlo, qhi): 
        def helper(tree, ti, tlo, thi):
            if qlo > thi or qhi < tlo: return 0
            if qlo <= tlo <= thi <= qhi: return tree[ti]
            tmi = tlo + (thi - tlo)//2
            left = helper(tree, 2*ti+1, tlo, tmi)
            right = helper(tree, 2*ti+2, tmi+1, thi)
            return max(left, right)
        return helper(self.tree, 0, 0, self.N-1)

    def update(self, qi, val):
        # update tree[ti] which covers nums[tlo..thi] and
        # any descendants that includes nums[i], 
        # where nums[i] is set to val
        def helper(tree, ti, tlo, thi):
            if qi < tlo or qi > thi: return
            if tlo == thi: tree[ti] = val
            if tlo < thi:  # update descendants if internal node
                tmi = tlo + (thi - tlo)//2
                helper(tree, 2*ti+1, tlo, tmi)
                helper(tree, 2*ti+2, tmi+1, thi)
                tree[ti] = max(tree[2*ti+1], tree[2*ti+2])
        helper(self.tree, 0, 0, self.N-1)



def solve(N, M, A, B, parents):
    adj = [[] for _ in range(N)]
    for c,p in enumerate(parents):
        adj[p].append(c+1)

    # preorder
    depth = [0]*N           # depth[u] = path length from u to root (0)
    preorder = []           # preorder visit sequence
    preorder_start = [0]*N  # preorder_start[u] = start index of subtree rooted at u in preorder
    preorder_end = [0]*N    # preorder_end[u] = end index of subtree rooted at u in preorder (inclusive)
    
    @bootstrap
    def traverse(u, d):  # at node u, depth d
        preorder_start[u] = len(preorder)
        preorder.append(u)
        depth[u] = d
        sz = 1
        for v in adj[u]:
            sz += yield traverse(v, d+1)
        preorder_end[u] = preorder_start[u] + sz - 1
        yield sz

    traverse(0, 0)

    # num queries for each node, sorted child first
    queries = {}  # idx -> num queries
    for i in range(M):
        idx = (A*i + B) % N
        queries[idx] = queries.get(idx, 0) + 1
    queries = list(queries.items())
    queries.sort(key=lambda tup: depth[tup[0]], reverse=True)

    # query then reset
    res = 0
    tree = SegmentTreeMax(preorder)
    for (idx, count) in queries:
        s, e = preorder_start[idx], preorder_end[idx]
        for _ in range(count):
            mx = tree.query_range(s, e)
            res += mx
            tree.update(preorder_start[mx], 0)
    
    return res


def main():
    from sys import stdin
    
    T = int(stdin.readline().strip())
    for t in range(T):
        N, M, A, B = list(map(int, stdin.readline().strip().split()))
        parents = [int(stdin.readline().strip()) for _ in range(N-1)]
        
        out = solve(N, M, A, B, parents)
        print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
    main()
