''' Bus Routes 
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d83bf
'''

def solve(N,D,nums):
	i = D
	for n in nums[::-1]:
		i -= i % n
	return i


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		N,D = list(map(int,stdin.readline().strip().split()))
		nums = list(map(int,stdin.readline().strip().split()))
		out = solve(N,D,nums)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()