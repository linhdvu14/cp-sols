''' F. Quadratic Set
https://codeforces.com/contest/1622/problem/F
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

def batch_xor_hash(N):
    '''
    assign a random 64-bit number to each prime
    let H(n) = xor of all prime factors of n including duplicity
    return H(n) for n=1..N
    '''
    import random
    random.seed(123)
    MAX = (1 << 64) - 1

    pmap = {}           # prime -> random large number
    hash = [0]*(N+1)    # hash[n] = xor hash of all prime factors of n
    mpf = [0]*(N+1)     # min prime factor
    for i in range(2, N+1):
        if mpf[i] == 0:
            pmap[i] = random.randint(0, MAX)
            hash[i] ^= pmap[i]
            mpf[i] = i
        for p, h in pmap.items():
            if p > mpf[i] or p*i > N: break
            mpf[p*i] = p   # set once per composite number
            hash[p*i] ^= hash[i] ^ h
    return hash, pmap


def solve(N):
    if N <= 3: return [1]

    # hash[n] = xor hash of n
    # lookup[xor hash of n!] = n 
    # xor = xor hash of 1! 2! ... N!
    hash, _ = batch_xor_hash(N)
    xor = hf = 0
    lookup = {}
    for n in range(2, N+1): 
        hf ^= hash[n]
        xor ^= hf
        lookup[hf] = n

    # 1! 2! ... N! already a square
    if xor == 0: return list(range(1, N+1))

    # can rm 1 factorial
    if xor in lookup: 
        n = lookup[xor]
        return [i for i in range(1, N+1) if i != n]
    
    # can rm 2 factorials
    for h1, n1 in lookup.items():
        h2 = xor ^ h1
        if h2 in lookup:
            n2 = lookup[h2]
            return [i for i in range(1, N+1) if i != n1 and i != n2]

    # N odd, can rm 2, N, N//2
    return [i for i in range(1, N) if i != 2 and i != N // 2]


def main():
    N = int(input())
    out = solve(N)
    print(len(out))
    print(*out)


if __name__ == '__main__':
    main()

