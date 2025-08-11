''' Lucky Number
https://www.codechef.com/SNCKQL21/problems/LUCKYNUM
'''


import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(A, B, C):
    return 'YES' if A==7 or B==7 or C==7 else 'NO'


def main():
	T = int(input())
	for _ in range(T):
		A, B, C = list(map(int, input().split()))
		out = solve(A, B, C)
		print(out)


if __name__ == '__main__':
	main()

