''' Problem B: Xs and Os
https://www.facebook.com/codingcompetitions/hacker-cup/2021/qualification-round/problems/B
'''


def solve(grid, N):
	c_o, r_o = set(), set()
	c_dot, r_dot = {}, {}

	for r,row in enumerate(grid):
		for c,val in enumerate(row):
			if val == 'O':
				c_o.add(c)
				r_o.add(r)
			elif val == '.':
				if c not in c_dot: c_dot[c] = set()
				if r not in r_dot: r_dot[r] = set()
				c_dot[c].add(r)
				r_dot[r].add(c)
	
	mn, mn_cnt = float('inf'), 0
	for i in range(N):
		if i not in c_o:
			cand = len(c_dot[i]) if i in c_dot else N 
			if cand < mn: mn, mn_cnt = cand, 0
			if cand == mn: mn_cnt += 1
			if cand == 1:
				for r in c_dot[i]: break
				if r in r_dot and len(r_dot[r]) == 1 and r not in r_o: 
					mn_cnt -= 1
		if i not in r_o:
			cand = len(r_dot[i]) if i in r_dot else N 
			if cand < mn: mn, mn_cnt = cand, 0
			if cand == mn: mn_cnt += 1            
	if mn == 0: mn_cnt = 0

	return f'{mn} {mn_cnt}' if mn < float('inf') else 'Impossible'


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for t in range(T):
		# if t != 813: continue
		N = int(stdin.readline().strip())
		grid = [stdin.readline().strip() for _ in range(N)]
		out = solve(grid, N)
		print('Case #{}: {}'.format(t+1, out))
		# print(N)
		# for row in grid: print(row)


def gen():
	import random
	random.seed(12)

	T = 1000
	print(T)
	for _ in range(T):
		N = random.randint(2,50)
		print(N)

		fill = random.randint(0,(N*N)//5)
		x_pos, o_pos = set(), set()
		while len(x_pos) < fill:
			r = random.randint(0,N-1)
			c = random.randint(0,N-1)
			x_pos.add((r,c))
		while len(o_pos) < fill:
			r = random.randint(0,N-1)
			c = random.randint(0,N-1)
			if (r,c) not in x_pos: o_pos.add((r,c))

		grid = [['.']*N for _ in range(N)]
		for r,c in x_pos: grid[r][c] = 'X'
		for r,c in o_pos: grid[r][c] = 'O'
		for row in grid: print(''.join(row))


if __name__ == '__main__':
	main()
