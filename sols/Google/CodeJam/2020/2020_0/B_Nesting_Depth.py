''' Nesting Depth
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f
'''

def solve(nums):
	def recurse(nums, k):  # k = count outside parentheses
		if not nums: return ''
		mn = min(nums)
		res = ''
		buff, buffmn = [], []
		for n in nums:
			if n == mn:
				if buff:
					res += recurse(buff, mn)
					buff = []
				buffmn.append(n)
			if n != mn:
				if buffmn:
					res += str(mn)*len(buffmn)
					buffmn = []
				buff.append(n)
		if buff:
			res += recurse(buff, mn)
		if buffmn:
			res += str(mn)*len(buffmn)

		return '('*(mn-k) + res + ')'*(mn-k)

	return recurse(nums,0)




def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		nums = list(map(int,list(stdin.readline().strip())))
		out = solve(nums)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()