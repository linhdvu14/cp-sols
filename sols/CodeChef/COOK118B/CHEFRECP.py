''' Chef and Recipe

https://www.codechef.com/COOK118B/problems/CHEFRECP

'''

def solve(nums):
	blocks = []
	n = cnt = 0
	for num in nums:
		if num != n and n > 0:
			blocks.append((n,cnt))
			n = cnt = 0
		n = num
		cnt += 1
	blocks.append((n,cnt))

	seen1, seen2 = set(), set()
	for k,v in blocks:
		if k in seen1 or v in seen2: return False
		seen1.add(k)
		seen2.add(v)

	return True



def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for _ in range(T):
		N = int(stdin.readline().strip())
		nums = list(map(int,stdin.readline().strip().split()))
		out = solve(nums)
		print('YES' if out else 'NO')


if __name__ == '__main__':
	main()

