''' Wormhole in One
https://codingcompetitions.withgoogle.com/codejam/round/000000000019ffb9/00000000003386d0
'''

INF = float('inf')

class UnionFind:
	def __init__(self, points, lines):
		points = list(points)
		self.n = len(points)
		self.size = [1 for _ in range(self.n)]
		self.parent = [i for i in range(self.n)]

		# group points on same line
		p2i = {p:i for i,p in enumerate(points)}
		for x1,y1,x2,y2 in lines:
			self.union(p2i[x1,y1],p2i[x2,y2])

	def find(self, i):
		while self.parent[i] != self.parent[self.parent[i]]:
			self.parent[i] = self.parent[self.parent[i]]
		return self.parent[i]

	def union(self, i, j):
		rooti, rootj = self.find(i), self.find(j)
		if rooti == rootj: return
		if self.size[rooti] > self.size[rootj]:
			rooti, rootj = rootj, rooti
		self.parent[rooti] = rootj
		self.size[rootj] += self.size[rooti]
	
	def count(self):
		count = {}
		for i in range(self.n):
			par = self.find(i)
			if par not in count: count[par] = 0
			count[par] += 1

		res = odd = 0
		for c in count.values():  # group of points on same line
			res += c  # all even can fully connect; pair of odds can fully connect
			if c % 2 == 1: odd += 1
		return res, odd % 2


def gcd(x,y):
	if x > y: x, y = y, x
	if x == 0: return y
	return gcd(y % x, x)


def solve(N,holes):
	if N == 1: return 1

	lines = {}  # slope -> [] (start,end)
	points = {}  # slope -> set of distinct points
	for i in range(N):
		for j in range(i+1,N):
			x1,y1 = holes[i]
			x2,y2 = holes[j]
			dx,dy = x1-x2, y1-y2

			if dx == 0:
				slope = (INF,INF)
				if slope not in lines: lines[slope] = []
				lines[slope].append((x1,y1,x2,y2))
				if slope not in points: points[slope] = set()
				points[slope].add((x1,y1))
				points[slope].add((x2,y2))
			else:
				g = gcd(abs(dx),abs(dy))

				slope1 = (dx//g,dy//g)
				if slope1 not in lines: lines[slope1] = []
				lines[slope1].append((x1,y1,x2,y2))

				if slope1 not in points: points[slope1] = set()
				points[slope1].add((x1,y1))
				points[slope1].add((x2,y2))

				slope2 = (-dx//g,-dy//g)
				if slope2 not in lines: lines[slope2] = []
				lines[slope2].append((x2,y2,x1,y1))
				
				if slope2 not in points: points[slope2] = set()
				points[slope2].add((x1,y1))
				points[slope2].add((x2,y2))

	mx = 0
	for slope in lines.keys():
		uf = UnionFind(points[slope],lines[slope])
		res, odd = uf.count()
		if odd % 2 == 0 and res < N: res += 1  # exit
		if res < N: res += 1  # entry
		mx = max(mx, res)

	return mx


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		N = int(stdin.readline().strip())
		holes = []
		for _ in range(N):
			x,y = list(map(int,stdin.readline().strip().split()))
			holes.append((x,y))
		out = solve(N,holes)
		print('Case #{}: {}'.format(t+1, out))


if __name__ == '__main__':
	main()