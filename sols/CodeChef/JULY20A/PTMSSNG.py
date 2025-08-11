''' Missing a Point
https://www.codechef.com/JULY20A/problems/PTMSSNG
'''

def solve(N,vertices):
	x, y = 0, 0
	for xx, yy in vertices:
		x ^= xx
		y ^= yy
	return x, y


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for _ in range(T):
		N = int(stdin.readline().strip())
		vertices = [tuple(map(int,stdin.readline().strip().split())) for _ in range(4*N-1)]
		x, y = solve(N,vertices)
		print(x, y)


if __name__ == '__main__':
	main()

