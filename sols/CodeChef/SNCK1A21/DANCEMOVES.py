''' Dance Moves
https://www.codechef.com/SNCK1A21/problems/DANCEMOVES
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(X, Y):
    if Y <= X: return X-Y
    return (Y-X+1)//2 + (Y-X)%2


def main():
	T = int(input())
	for _ in range(T):
		X, Y = list(map(int, input().split()))
		out = solve(X, Y)
		output(str(out) + '\n')


if __name__ == '__main__':
	main()

