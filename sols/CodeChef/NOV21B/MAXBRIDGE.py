''' Maximise the bridges
https://www.codechef.com/NOV21B/problems/MAXBRIDGE
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, M):
    for i in range(1, N):
        print(f'{i} {i+1}')
        M -= 1
    
    i, j = N-2, N
    while M > 0:
        print(f'{i} {j}')
        M -= 1
        j += 1
        if j > N:
            i -= 1
            j = i + 2


def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        solve(N, M)


if __name__ == '__main__':
    main()

