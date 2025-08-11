''' The Delicious Cake
https://www.codechef.com/JUNE20B/problems/CONTAIN
'''

# pypy3

def ccw(p,q,r): return -(q[0]-p[0])*(r[1]-p[1])+(q[1]-p[1])*(r[0]-p[0])	

def convex_hull(points):	
	if len(points) < 3: return [], []
	up, down = [], []
	for p in points:
		while len(up)>1 and ccw(up[-1],up[-2],p) > 0: up.pop()
		while len(down)>1 and ccw(down[-1],down[-2],p) < 0: down.pop()
		up.append(p)
		down.append(p)
	down += up[1:-1][::-1]

	sres = set(down)
	return down, [p for p in points if p not in sres]


def convex_layers(points):  # O(N^2)
	points = sorted(list(set(points)))
	layers = []
	while points:
		layer, points = convex_hull(points)
		if layer: layers.append(layer)
	return layers


# outside or on edge
def outside(points, q):
	if len(points)<2: return True

	a, b = 1, len(points)-1
	if ccw(points[0],points[a],points[b]) < 0: a,b = b,a
	c1, c2 = ccw(points[0],points[a],q), ccw(points[0],points[b],q)
	if c1<=0 or c2>=0: return True

	while abs(a-b)>1:
		c = (a+b)//2
		if ccw(points[0],points[c],q) < 0:
			b = c
		else:
			a = c

	return ccw(points[a],points[b],q) <= 0


def solve(points,queries):
	layers = convex_layers(points)
	res = []
	for q in queries:
		c = 0
		for layer in layers:
			if outside(layer,q): break
			c += 1
		res.append(c)
	return res


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())
	for _ in range(T):
		N,Q = list(map(int,stdin.readline().strip().split()))
		points = [tuple(map(int,stdin.readline().strip().split())) for _ in range(N)]
		queries = [tuple(map(int,stdin.readline().strip().split())) for _ in range(Q)]
		out = solve(points,queries)
		print('\n'.join(map(str,out)))


if __name__ == '__main__':
	main()

