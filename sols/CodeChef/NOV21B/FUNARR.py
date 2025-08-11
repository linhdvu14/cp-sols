''' Functional Array
https://www.codechef.com/NOV21B/problems/FUNARR
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write


# compute fB: fB[i] = B[i+1] - B[i]
# then fA is formed by appending to ends of fB (useless) or decomposing fB[i] = a1 + a2 + ... 
# then fA is subsequence of Z iff Z can split into len(fB) partitions s.t. partitions[i] has subset sum fB[i]
# https://www.geeksforgeeks.org/subset-sum-queries-using-bitset/

def solve(NB, NZ, B, Z):
    fB = [B[i] - B[i-1] for i in range(1, NB)]
    if len(fB) == 0: return True
    if any(b < 0 for b in fB): return False

    # mask[1 << x] = 1 if possible to make subset sum x
    mask = i = 0
    for b in fB:
        bound = (1 << (b+2)) - 1

        # scan Z till can make subset sum b
        while i < NZ and (mask >> b) & 1 == 0:
            mask |= mask << Z[i]
            mask |= 1 << Z[i]
            mask &= bound
            i += 1
        
        # found subset set, start new partition
        if (mask >> b) & 1 == 1:
            mask = 0
        elif i == NZ: 
            return False

    return True


def main():
    T = int(input())
    for _ in range(T):
        NB, NZ = list(map(int, input().split()))
        B = list(map(int, input().split()))
        Z = list(map(int, input().split()))
        out = solve(NB, NZ, B, Z)
        print('YES' if out else 'NO')


if __name__ == '__main__':
    main()

