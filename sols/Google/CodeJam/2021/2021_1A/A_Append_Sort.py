''' Append Sort 
https://codingcompetitions.withgoogle.com/codejam/round/000000000043585d/00000000007549e5
'''

DEBUG = False

def solve(N, nums):
	res = 0
	prev = nums[0]
	nnums = [prev]
	if DEBUG: print(f'{prev}\t{prev}\t0')	
	for i in range(1,N):
		cur = nums[i]
		iprev, icur = int(prev), int(cur)
		if iprev < icur:
			prev = cur
			nnums.append(prev)
			if DEBUG: print(f'{cur}\t{prev}\t{len(prev)-len(cur)}')
		elif iprev == icur:
			prev = cur + '0'
			res += len(prev)-len(cur)
			nnums.append(prev)
			if DEBUG: print(f'{cur}\t{prev}\t{len(prev)-len(cur)}')
		else:
			j = 0
			while j < min(len(prev),len(cur)):
				if prev[j] != cur[j]: break
				j += 1

			if j==len(cur):  # prev starts with cur
				rem = prev[j:]
				if all(c=='9' for c in rem):
					prev = cur + '0'*(len(rem)+1)
				else:
					prev = str(iprev+1)
				res += len(prev)-len(cur)
				if DEBUG: print(f'{cur}\t{prev}\t{len(prev)-len(cur)}')
			elif prev[j] < cur[j]:
				prev = cur+'0'*(len(prev)-len(cur))
				res += len(prev)-len(cur)
				if DEBUG: print(f'{cur}\t{prev}\t{len(prev)-len(cur)}')
			else:
				prev = cur+'0'*(len(prev)-len(cur)+1)
				res += len(prev)-len(cur)
				if DEBUG: print(f'{cur}\t{prev}\t{len(prev)-len(cur)}')

			nnums.append(prev)

	if DEBUG: print(f'res={res}')
	return res, nnums



def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		N = int(stdin.readline().strip())
		nums = list(stdin.readline().strip().split())
		out, _ = solve(N, nums)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()