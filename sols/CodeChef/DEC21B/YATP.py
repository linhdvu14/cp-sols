''' Yet Another Tree Problem
https://www.codechef.com/DEC21B/problems/YATP
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

if DEBUG:
    from varname.core import argname
    from inspect import currentframe

def debug(var, *more_vars):
    if not DEBUG: return
    var_names = argname('var', '*more_vars', func=debug)
    values = (var, *more_vars)
    name_and_values = [f'{var_name}={value}'  for var_name, value in zip(var_names, values)]
    prefix = f'{currentframe().f_back.f_lineno:02d}: '
    print(f'{prefix}{", ".join(name_and_values)}')


INF = float('inf')

# -----------------------------------------
class RangeQuery:
    def __init__(self, data, func=max):
        self.func = func
        self._data = _data = [list(data)]
        i, n = 1, len(_data[0])
        while 2 * i <= n:
            prev = _data[-1]
            _data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, start, stop):
        """func of data[start, stop)"""
        depth = (stop - start).bit_length() - 1
        return self.func(self._data[depth][start], self._data[depth][stop - (1 << depth)])

    def __getitem__(self, idx):
        return self._data[0][idx]



def build_line_tree(N, P, W):
    # start out with each node in its own cc
    # greedily join cc of nodes with smallest edge weight
    par = list(range(N))                 # cc root
    subtree = [[i] for i in range(N)]    # line subtree under u
    weights = [[] for _ in range(N)]     # edge weights of subtree under u

    idx = sorted(list(range(N-1)), key=lambda i: W[i])
    for i in idx:
        a, b, w = i+1, P[i]-1, W[i]
        a, b = par[a], par[b]
        if len(subtree[a]) < len(subtree[b]): a, b = b, a
        for i in subtree[b]: par[i] = a
        subtree[a] += subtree[b]
        weights[a] += [w] + weights[b]
    
    # return longest subtree
    for st, w in zip(subtree, weights):
        if len(st) == N:
            return st, w


def solve(N, Q, P, W, queries):
    # conv to line tree
    # max edge of any node pair is max of their weights segment
    # edges = [(u+1, p-1, w) for u, (p, w) in enumerate(zip(P, W))]
    tree, weights = build_line_tree(N, P, W)
    weights += [0]

    # idx[u] = index of node u in tree
    idx = [-1]*N
    for i, u in enumerate(tree):
        idx[u] = i
    
    # range maximum query
    rmq = RangeQuery(weights, func=max)

    res = [0]*Q
    for qi, q in enumerate(queries):
        # calc max edge weight between consecutive wanted nodes
        wanted = [idx[q2] for q2 in q]
        wanted.sort()
        arr = [rmq.query(u, v) for u, v in zip(wanted, wanted[1:])]
        
        # sum max of all possible subarrays
        # for each ele, count how many subarrays where it is the leftmost max value
        # left[i] = idx of first ele to the left with value >= arr[i]
        # right[i] = idx of first ele to the right with value > arr[i]
        M = len(arr)
        left, right = [-1]*M, [-1]*M
        for i in range(M):
            left[i] = i-1
            while left[i] != -1 and arr[i] > arr[left[i]]: 
                left[i] = left[left[i]]

        for i in range(M-1, -1, -1):
            right[i] = i+1
            while right[i] != M and arr[i] >= arr[right[i]]: 
                right[i] = right[right[i]]
        
        res[qi] = sum(v*(i-l)*(r-i) for i, (v, l, r) in enumerate(zip(arr, left, right)))

    return res


def main():
    T = int(input())
    for _ in range(T):
        N, Q = list(map(int, input().split()))
        P = list(map(int, input().split()))
        W = list(map(int, input().split()))
        queries = [list(map(lambda x: int(x)-1, input().split()[1:])) for _ in range(Q)]
        out = solve(N, Q, P, W, queries)
        print(' '.join(map(str, out)))


if __name__ == '__main__':
    main()
