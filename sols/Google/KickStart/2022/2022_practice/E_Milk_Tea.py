''' Milk Tea
https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4332/0000000000943934
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

def solve(NA, NB, P, A, B):
    B = set(B)

    ones = [0] * P
    for a in A:
        for i in range(P):
            if (a >> i) & 1:
                ones[i] += 1
    
    def get_cost(mask):
        res = 0
        for i, one in enumerate(ones):
            bit = (mask >> i) & 1
            if bit == 1: res += NA - one
            else: res += one
        return res
    
    best = best_cost = 0
    for i, one in enumerate(ones):
        if one * 2 > NA:
            best |= 1 << i
            best_cost += NA - one
        else:
            best_cost += one
    
    if best not in B: return best_cost

    # flip one bit of each bad
    best_cost = INF
    for b in B:
        for i in range(P):
            b ^= 1 << i
            if b not in B: best_cost = min(best_cost, get_cost(b))
            b ^= 1 << i

    return best_cost


def main():
    T = int(input())
    for t in range(T):
        NA, NB, P = list(map(int, input().split()))
        A = [int(input().decode().strip(), 2) for _ in range(NA)]
        B = [int(input().decode().strip(), 2) for _ in range(NB)]
        out = solve(NA, NB, P, A, B)
        print(f'Case #{t+1}: {out}')


if __name__ == '__main__':
    main()

