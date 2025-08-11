''' Axiom
https://www.codechef.com/ENCO2022/problems/ENCOD03
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

def batch_sieve(N):
    '''return all primes in [2..N] in O(N)'''
    primes = []
    lpf = [0]*(N+1)  # least prime factor
    for i in range(2, N+1):
        if lpf[i] == 0:
            primes.append(i)
            lpf[i] = i
        for p in primes:
            if p*i > N or p > lpf[i]: break  # lpf[p*i] <= lpf[i] < p
            lpf[p*i] = p                     # set once per composite number
    return primes


from heapq import heappush, heappop, heapify

def solve(N):
    h = batch_sieve(N)
    heapify(h)
    res = 0
    while len(h) > 1:
        a = heappop(h)
        b = heappop(h)
        res += a + b
        heappush(h, a+b)
    return res


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        out = solve(N)
        print(out)


if __name__ == '__main__':
    main()

