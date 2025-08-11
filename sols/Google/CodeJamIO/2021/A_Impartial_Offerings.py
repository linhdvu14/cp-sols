''' Impartial Offerings 
https://codingcompetitions.withgoogle.com/codejamio/round/00000000004360f2/0000000000777098
'''

def solve(n, nums):
	count = {}
	for num in nums:
		if num not in count: count[num] = 0
		count[num] += 1
	skeys = sorted(count.keys())
	res = 0
	for i, k in enumerate(skeys):
		res += count[k]*(i+1)
	return res


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		n = int(stdin.readline().strip())
		nums = list(map(int,stdin.readline().strip().split()))
		out = solve(n, nums)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()