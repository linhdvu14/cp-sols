''' Record Breaker 
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000387171
'''
def solve(N, nums):
	res = 0
	mx = -1
	for i,num in enumerate(nums):
		if num > mx and (i==N-1 or num>nums[i+1]):
			res += 1
		mx = max(mx, num)
	return res


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		N = int(stdin.readline().strip())
		nums = list(map(int,stdin.readline().strip().split()))
		out = solve(N, nums)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()