''' Bike Tour 
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d82e6
'''
def solve(n,nums):
	return sum(1 for i in range(1,n-1) if nums[i]>nums[i-1] and nums[i]>nums[i+1])


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		n = int(stdin.readline().strip())
		nums = list(map(int,stdin.readline().strip().split()))
		out = solve(n,nums)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()