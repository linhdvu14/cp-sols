''' Problem A: Runway
https://www.facebook.com/codingcompetitions/hacker-cup/2021/round-2/problems/A
'''


# orig
def solve_1(N, M, grid):
	from collections import deque
	
	cur = {}  # s -> avail model idx + unavail model idx
	for i, s in enumerate(grid[0]):
		if s not in cur: cur[s] = deque([])
		cur[s].append(i) 

	avail = set(list(range(M)))  # model indices who have not changed
	res = 0
	for gi in range(1, N+1):
		nxt = {}
		unfilled = []
		for s in grid[gi]:
			if s not in nxt: nxt[s] = deque([])
			if s in cur:  # if common, assign unavail first
				idx = cur[s].pop()
				if idx in avail:
					nxt[s].appendleft(idx)
				else:
					nxt[s].append(idx)
				if len(cur[s]) == 0: del cur[s]
			else:
				unfilled.append(s)

		ui = 0
		for idx in cur.values():
			for i in idx:
				s = unfilled[ui]
				ui += 1
				if i in avail:
					avail.remove(i)
				else:
					res += 1
				nxt[s].append(i)

		cur = nxt

	return res	


# official
def solve_2(N, M, grid):
	# style -> (num models wearing style who haven't changed, num models wearing style who have changed)
	cur = {}
	for s in grid[0]:
		if s not in cur: cur[s] = [0, 0]
		cur[s][0] += 1
	
	res = 0
	for gi in range(1, N+1):
		nxt = {}
		for s in grid[gi]:
			if s not in nxt: nxt[s] = [0, 0]
			if s in cur:
				if cur[s][1] > 0:  # take models who have changed first
					cur[s][1] -= 1
					nxt[s][1] += 1
				else:
					cur[s][0] -= 1
					nxt[s][0] += 1
				if cur[s][0] == cur[s][1] == 0: del cur[s]
			else:
				nxt[s][1] += 1
		
		# remaining models must change
		for (_, unavail) in cur.values():
			res += unavail
		
		cur = nxt

	return res


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for t in range(T):
		N, M = list(map(int, stdin.readline().strip().split()))
		grid = [list(map(int, stdin.readline().strip().split())) for _ in range(N+1)]
		out = solve_2(N, M, grid)
		print(f'Case #{t+1}: {out}')



if __name__ == '__main__':
	main()
