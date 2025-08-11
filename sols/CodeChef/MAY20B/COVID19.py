''' Coronavirus Spread

https://www.codechef.com/MAY20B/problems/COVID19

'''


def solve(n, nums):
	mn, mx = float('inf'), -float('inf')
	size = prev = 0
	for num in nums:
		if size and num-prev > 2:  # new group
			mn = min(mn, size)
			mx = max(mx, size)
			size = prev = 0

		if not size or num-prev <= 2:
			size += 1
			prev = num

	mn = min(mn, size)
	mx = max(mx, size)	
	return mn, mx



def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for _ in range(T):
		n = int(stdin.readline().strip())
		nums = list(map(int,stdin.readline().strip().split()))
		mn, mx = solve(n, nums)
		print('{} {}'.format(mn,mx))


if __name__ == '__main__':
	main()