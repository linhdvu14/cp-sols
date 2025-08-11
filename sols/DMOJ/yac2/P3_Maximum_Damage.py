''' Yet Another Contest 2 P3 - Maximum Damage
https://dmoj.ca/problem/yac2p3
'''

import sys
input = sys.stdin.readline  # strip() if str

INF = float('inf')

# -----------------------------------------

def batch_sieve(N):
    primes = []
    lpf = [0]*(N+1)  # least prime factor
    for i in range(2, N+1):
        if lpf[i] == 0:
            primes.append(i)
            lpf[i] = i
        for p in primes:
            if p*i > N or p > lpf[i]: break  # lpf[p*i] <= lpf[i] < p
            lpf[p*i] = p                     # set once per composite number
    return lpf


def is_ok(cnt, n, sz): 
    need = n * sz 
    for c in cnt:
        need -= min(c, n, need)  
        if need == 0: return True 
    return False 


def find_max_groups(cnt, sz): 
    res, lo, hi = 0, 0, sum(cnt) // sz + 1
    while lo <= hi:
        mi = (lo + hi) // 2
        if is_ok(cnt, mi, sz): 
            res = mi
            lo = mi + 1 
        else: 
            hi = mi - 1 
    return res 


# solve separately for each prime p
# let C = cnt factors of p over array H
# need to group C into max num size-K groups of distinct eles
# O(N (log N)^2)

def main():
    N, K = list(map(int, input().split()))
    
    H = list(map(int, input().split()))
    mx, H_cnt = 0, {}
    for h in H:
        mx = max(mx, h)
        H_cnt[h] = H_cnt.get(h, 0) + 1

    lpf = batch_sieve(mx)
    prime_cnt = {}
    for h, dup in H_cnt.items():
        while lpf[h] > 1:
            p = lpf[h]
            c = 0
            while h % p == 0:
                c += 1
                h //= p
            if p not in prime_cnt: prime_cnt[p] = []
            prime_cnt[p].extend([c] * dup)
    
    res = 0
    for p, cnt in prime_cnt.items():
        if len(cnt) < K: continue
        res += find_max_groups(cnt, K)

    print(res)


if __name__ == '__main__':
    main()

