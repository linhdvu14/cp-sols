''' E. Math Test
https://codeforces.com/contest/1622/problem/E
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

DEBUG = os.environ.get('debug') is not None

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

def bucket_sort(vals, order=None):
    '''
    given array [vals[i] for i in order]
    return new_order s.t. [vals[i] for i in new_order] is sorted
    '''
    N = len(vals)
    if order is None: order = list(range(N))

    # normalize so mn == 0
    mn = min(vals)
    vals = [v-mn for v in vals]
    mx = max(vals)

    # count[v] = number of value v in vals
    count = [0]*(mx+1)
    for v in vals: count[v] += 1

    # count[v] = number of values in vals <= v
    for i in range(len(count)-1): count[i+1] += count[i]

    # new order
    new_order = [0]*N
    for i in reversed(order):
        v = vals[i]
        c = count[v]        # c = num values in vals <= v
        new_order[c-1] = i  # so put v at idx c-1 (0-based)
        count[v] -= 1       # next time encountering v, put it at idx c-2

    return new_order


# let sign[i] = sign(r[i] - x[i])
# then total surprise = SUM_i sign[i] * (r[i] - x[i])
# expectation i contributes: - sign[i] * x[i] ---> fixed
# question q contributes:      score[q] * SUM_i signed[i] * (whether student i solves question q)
# -> can greedily assign highest scores to highest contribution questions

# if after assignment, student i has sign(r[i] - x[i]) != sign[i]
# i.e. subtract |r[i] - x[i]| from total surprise instead of add
# then flipping sign[i] will increase total surprise
# so the orig mask cannot be optimal

def solve(N, M, X, A):
    mx, mxv = -INF, []
    for mask in range(1 << N):
        x = 0

        # add[q] = num students with mask 1 who solved q - num students with mask 0 who solved q
        add = [0]*M
        for i in range(N):
            sign = 1 if (mask >> i) & 1 == 1 else -1
            x -= sign * X[i]
            for q in range(M):
                add[q] += A[i][q] * sign

        # greedily assign highest score to q with highest add
        # normal sort will TLE
        order = bucket_sort(add)
        x += sum((v+1) * add[q] for v, q in enumerate(order))
        if x > mx: mx, mxv = x, order

    res = [-1]*M
    for v, q in enumerate(mxv): res[q] = v+1
    return res


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        X = list(map(int, input().split()))
        A = [list(map(int, list(input().decode().strip()))) for _ in range(N)]
        out = solve(N, M, X, A)
        print(*out)


if __name__ == '__main__':
    main()
 