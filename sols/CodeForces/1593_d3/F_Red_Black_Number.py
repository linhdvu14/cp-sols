''' F. Red-Black Number
https://codeforces.com/contest/1593/problem/F
'''

import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write

def solve(N, A, B, X):
	# dp[i][ra][rb][na] = trace
	# * after processing i digits
	# * currently built numA % A == ra
	# * currently built numB % B == rb
	# * currently built numA has na digits 
	dp = [[[[-1]*(N+1) for _ in range(B)] for _ in range(A)] for _ in range(N+1)]
	dp[0][0][0][0] = True

	for i in range(N):
		d = int(X[i])
		for ra in range(A):
			for rb in range(B):
				for na in range(N+1):
					if dp[i][ra][rb][na] == -1: continue
					dp[i+1][(ra*10+d)%A][rb][na+1] = 2*ra
					dp[i+1][ra][(rb*10+d)%B][na] = 2*rb + 1
	
	mn, mna = N+1, -1
	for na in range(1, N):
		if dp[N][0][0][na] == -1: continue
		if abs(N-2*na) < mn: mn, mna = abs(N-2*na), na
	if mna < 0: return -1
	
	res = ''
	ra, rb, na = 0, 0, mna
	for i in range(N, 0, -1):
		prev = dp[i][ra][rb][na]
		if prev % 2 == 0:
			res += 'R'
			ra = prev >> 1
			na -= 1
		else:
			res += 'B'
			rb = prev >> 1
	return res[::-1]



def main():
	T = int(input())
	for _ in range(T):
		N, A, B = list(map(int, input().split()))
		X = list(input().decode())
		out = solve(N, A, B, X)
		output(str(out) + '\n')


if __name__ == '__main__':
	main()

