''' F. Closest Pair
https://codeforces.com/contest/1635/problem/F
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

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

class FenwickTreeMin:
    def __init__(self, data):
        '''transform list into BIT'''
        self.bit = data
        for i in range(len(data)):
            j = i | (i + 1)
            if j < len(data):
                data[j] = min(data[j], data[i])

    def query(self, end):
        '''calc min(bit[:end])'''
        x = INF
        while end:
            x = min(x, self.bit[end - 1])
            end &= end - 1  # 110 -> 100
        return x

    def update(self, idx, x):
        '''updates bit[idx] += x'''
        while idx < len(self.bit):
            self.bit[idx] = min(self.bit[idx], x)
            idx |= idx + 1   # 101 -> 110


# let L[i] = max j < i s.t. wj <= wi, R[i] = min j > i s.t. wj <= wi
# then closest pair for i..N-1 must be one of 2N intervals (L[i], i), (R[i], i)
# given q = (l, r), find min-dist interval fully covered by (l, r)

def solve(N, Q, points, queries):
    # find all cand intervals (L[i], i), (R[i], i)
    # ends[l] = right ends of all cand intervals starting at l
    ends = [[] for _ in range(N)]

    stack = []
    for i, (_, w) in enumerate(points):
        while stack and points[stack[-1]][1] > w: stack.pop()
        if stack: ends[stack[-1]].append(i)
        stack.append(i)
    
    stack = []
    for i in range(N-1, -1, -1):
        _, w = points[i]
        while stack and points[stack[-1]][1] > w: stack.pop()
        if stack: ends[i].append(stack[-1])
        stack.append(i)
    
    # query_ends[l] = [](r, i) for all queries starting at l
    query_ends = [[] for _ in range(N)]
    for i, (l, r) in enumerate(queries):
        query_ends[l-1].append((r-1, i))
    
    # move l right to left
    # add dist(l, ends[l]) and process query (l, query_ends[l])
    # all intervals added so far will have left end >= l
    # so fenwick.query(r) returns min dist inside (l, r)
    fenwick = FenwickTreeMin([INF] * N)
    res = [INF] * Q
    for l in range(N-1, -1, -1):
        for r in ends[l]:
            fenwick.update(r, (points[r][0] - points[l][0]) * (points[r][1] + points[l][1]))
        for r, i in query_ends[l]:
            res[i] = fenwick.query(r + 1)

    return res


def main():
    N, Q = list(map(int, input().split()))
    points = [list(map(int, input().split())) for _ in range(N)]
    queries = [list(map(int, input().split())) for _ in range(Q)]
    out = solve(N, Q, points, queries)
    print('\n'.join(map(str, out)))


if __name__ == '__main__':
    main()

