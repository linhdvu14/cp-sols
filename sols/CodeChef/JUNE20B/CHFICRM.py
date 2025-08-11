''' Chef and Icecream
https://www.codechef.com/JUNE20B/problems/CHFICRM
'''

def solve(nums):
	count = [0]*4
	for n in nums:
		c = (n-5)//5
		if c==1:
			if count[1]<=0: return False
			count[1] -= 1
		elif c==2:
			if count[2]>0:
				count[2] -= 1
			elif count[1]>1:
				count[1] -= 2
			else:
				return False
		count[n//5] += 1
	return True


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for _ in range(T):
		N = int(stdin.readline().strip())
		nums = list(map(int,stdin.readline().strip().split()))
		out = 'YES' if solve(nums) else 'NO'
		print(out)


if __name__ == '__main__':
	main()

