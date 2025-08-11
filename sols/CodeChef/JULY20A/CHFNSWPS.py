''' Chefina and Swaps
https://www.codechef.com/JULY20A/problems/CHFNSWPS
'''

def solve(N,A,B):
	def count(nums):
		res = {}
		for n in nums:
			if n not in res: res[n] = 0
			res[n] += 1
		return res

	mn, countA, countBoth = 10**9, count(A), count(A+B)
	for k,v in countBoth.items():
		if v % 2 == 1: return -1
		if k not in countA: countA[k] = 0
		countA[k] -= v//2
		if countA[k] == 0: countA.pop(k)
		mn = min(mn, k)

	add, rm = [], []
	for k,v in countA.items():
		if v > 0: rm += [k]*v
		else: add += [k]*(-v)
	if len(add) != len(rm): return -1
	add, rm = sorted(add), sorted(rm, reverse=True)
	return sum(min(a,r,2*mn) for a,r in zip(add,rm))



def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for _ in range(T):
		N = int(stdin.readline().strip())
		A = list(map(int,stdin.readline().strip().split()))
		B = list(map(int,stdin.readline().strip().split()))
		out = solve(N,A,B)
		print(out)


if __name__ == '__main__':
	main()

