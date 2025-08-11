''' Overexcited Fan
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef4/0000000000317409
'''

def solve(X,Y,M):
	x, y = X, Y
	if x == 0 and y == 0: return 0
	for i, m in enumerate(M):
		if m == 'N':
			x, y = x, y+1
		elif m == 'S':
			x, y = x, y-1
		elif m == 'E':
			x, y = x+1, y
		elif m == 'W':
			x, y, = x-1, y
		if i+1 >= abs(x)+abs(y):
			return i+1
	return -1


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		X,Y,M = stdin.readline().strip().split()
		X,Y = int(X), int(Y)
		out = solve(X,Y,M)
		if out < 0:
			print('Case #{}: {}'.format(t+1, 'IMPOSSIBLE'))
		else:
			print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()