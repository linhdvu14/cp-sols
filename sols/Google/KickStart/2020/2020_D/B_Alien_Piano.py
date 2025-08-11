''' Alien Piano 
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000387174
'''
def solve(nums):
	cur = [0]*4  # min breaks if nums[i]==k
	for i in range(1,len(nums)):
		nxt = [float('inf')]*4
		diff = nums[i]-nums[i-1]
		for k in range(4):
			for kk in range(4):
				add = 0 if (diff==0 and k==kk) or (diff>0 and k>kk) or (diff<0 and k<kk) else 1
				nxt[k] = min(nxt[k], add+cur[kk])
		cur = nxt
	return min(cur)


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		N = int(stdin.readline().strip())
		nums = list(map(int,stdin.readline().strip().split()))
		out = solve(nums)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()