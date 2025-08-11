''' Reversort
https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
'''

def solve(N, nums):
	res = 0
	for i in range(N-1):
		for j in range(i,N):
			if nums[j]==i+1:
				res += j-i+1
				nums[i:j+1] = reversed(nums[i:j+1])
				break
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