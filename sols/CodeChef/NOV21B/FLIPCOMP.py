''' Flip or Compress
https://www.codechef.com/NOV21B/problems/FLIPCOMP
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

# if change all to 0
# 11011      -> flip 0, compress 1s, +3 (save -1)
# 1101, 1011 -> flip 0, join 1s, +3 (save 0, but can create 11011)
# 101        -> don't flip 0, flip 1s, +2
# 1001       -> don't flip 0, flip 1s, +2
# 10011      -> don't flip 0, flip/compress 1s, +3
# -> flip 0 when cnt(0)=1 and cnt(1)>1 for at least 1 nei

def solve(S):
    def make_zero(S):
        S = '0' + S + '0'

        # alternating block sizes
        blks = []
        p, cnt = '', 0
        for c in S:
            if c != p and p != '':
                blks.append(cnt)
                cnt = 0
            p = c
            cnt += 1
        blks.append(cnt)

        # convert 1s to 0
        cost = sum(min(blks[i], 2) for i in range(1, len(blks)-1, 2))
        
        # check for 0 flips
        for i in range(2, len(blks)-2, 2):
            if blks[i] == 1 and (blks[i-1] > 1 or blks[i+1] > 1):
                if blks[i-1] > 1 and blks[i+1] > 1:
                    cost -= 1
                blks[i+1] += 1
                
        return cost

    return min(make_zero(S), make_zero(''.join('1' if c=='0' else '0' for c in S)))


def main():
    T = int(input())
    for _ in range(T):
        S = input().decode().strip()
        out = solve(S)
        print(out)


if __name__ == '__main__':
    main()

