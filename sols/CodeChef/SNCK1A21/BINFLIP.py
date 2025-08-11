''' Yet Another Flipping Problem
https://www.codechef.com/SNCK1A21/problems/BINFLIP
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write


def solve(N, K):
    if K == 0: return 'YES', []

    step, rem = 1, K
    ops = []
    prev_add = False  # is the previous op an add op
    pos = -1          # track idx of consecutive adds
    while True:
        if rem == step: return 'YES', ops + [1]
        if rem % (2*step) != step: return 'NO', []
        if (rem - step) % (4*step) == 2*step:   # rm last
            ops += [rem-step+1] if not prev_add else [ops[-1]]
            rem -= step
            prev_add = False
        elif (rem + step) % (4*step) == 2*step:  # add
            pos = rem - 2*step + 1 if not prev_add else pos - step
            ops += [pos]
            rem += step
            prev_add = True
        step *= 2



def main():
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        res, ops = solve(N, K)
        print(res)
        if res=='YES':
            print(len(ops))
            for op in ops: print(op)


if __name__ == '__main__':
    main()

