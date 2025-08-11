''' E - Fraction Floor Sum
https://atcoder.jp/contests/abc230/tasks/abc230_e
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write


# https://math.stackexchange.com/questions/487401/sum-of-floor-of-harmonic-progression-sum-i-1n-lfloor-frac-ni-rfloor-2-sum
def main():
    N = int(input())
    
    k = 1
    while (k+1)*(k+1) <= N:
        k += 1

    s = 0
    for i in range(k):
        s += N//(i+1)
    print(2*s - k*k)


if __name__ == '__main__':
    main()

