''' Countdown 
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003380d2
'''

def solve(N,K,nums):
	indices = [i for i,num in enumerate(nums) if num==1]
	res = 0
	for i in indices:
		valid = True
		for k in range(K):
			if not valid: break
			if k > i: valid = False
			if nums[i-k] != 1+k: valid = False
		if valid: res += 1

	return res


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		N,K = list(map(int,stdin.readline().strip().split()))
		nums = list(map(int,stdin.readline().strip().split()))
		out = solve(N,K,nums)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()