''' Problem B: Prime Subtractorization
https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-1/problems/B
'''

import os, sys
input = sys.stdin.readline
output = sys.stdout.write

from inspect import currentframe, getframeinfo
from re import search
DEBUG = os.environ.get('debug') not in [None, '0']
DEBUG_CASE = int(os.environ.get('case', 0))

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
from bisect import bisect_right

def batch_sieve(N):
    primes = []
    lpf = [0] * (N + 1)
    for i in range(2, N + 1):
        if lpf[i] == 0:
            primes.append(i)
            lpf[i] = i
        for p in primes:
            if p * i > N or p > lpf[i]: break  # lpf[p*i] <= lpf[i] < p
            lpf[p * i] = p                     # set once per composite number
    return primes


primes = batch_sieve(10_000_000)
ps = [0] * (len(primes) + 1)
for i, p in enumerate(primes):
    ps[i] = ps[i - 1]
    if i and primes[i - 1] + 2 == p: ps[i] += 1


def solve(N):
    if N < 5: return 0
    i = bisect_right(primes, N) - 1
    return ps[i] + 1


def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        if DEBUG and DEBUG_CASE and t != DEBUG_CASE: continue
        res = solve(N)
        print(f'Case #{t + 1}: {res}')


if __name__ == '__main__':
    main()

