''' Triple Sort
https://www.codechef.com/MAY20B/problems/TRPLSRT
'''

# solvable:
# * odd-length cycle (reduce 2)
# * even number of even-length cycle (combine 2 -> 3-cycle + 1 stationery)
def solve(N, K, nums):
	nums = [-1] + nums
	ops = []
	even_cycles = []  # store idx

	# compress cycles
	seen = set()
	for i in range(1,N+1):
		if i in seen: continue
		cur = i
		cycle = []
		while cur not in seen:
			seen.add(cur)
			cycle.append(cur)
			if len(cycle) == 3:  
				ops.append(' '.join(map(str,cycle)))  # cycle[1] and cycle[2] correct
				nums[cycle[0]] = nums[cycle[2]]
				cycle = [cycle[0]]
			cur = nums[cur]
		
		if len(cycle) == 2: even_cycles.append(cycle)

	# impossible if odd num even cycles
	if len(even_cycles) % 2 == 1: return []

	# combine pair
	for i in range(len(even_cycles)//2):
		cy1, cy2 = even_cycles[i*2], even_cycles[i*2+1]
		i1, j1, i2, j2 = cy1[0], cy1[1], cy2[0], cy2[1]
		ops.append(' '.join(map(str,[i1,j1,i2]))) # j1 correct
		ops.append(' '.join(map(str,[j2,i2,i1]))) # i1,i2,j2 correct

	return ops if len(ops) <= K else []



def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for _ in range(T):
		N,K = list(map(int,stdin.readline().strip().split()))
		nums = list(map(int,stdin.readline().strip().split()))
		if nums == sorted(nums): print(0)
		else:
			ops = solve(N, K, nums)
			if not ops: print(-1)
			else: 
				print(len(ops))
				print('\n'.join(ops))


if __name__ == '__main__':
	main()

