''' Weird Palindrome Making
https://www.codechef.com/NOV21B/problems/MAKEPAL
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, counts):
    odd = sum(1 for c in counts if c % 2 == 1)
    return 0 if odd <= 1 else odd // 2


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        counts = list(map(int, input().split()))
        out = solve(N, counts)
        print(out)


if __name__ == '__main__':
    main()

