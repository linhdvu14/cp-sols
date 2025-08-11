''' The Delicious Cake

https://www.codechef.com/JUNE20B/problems/CONTAIN
'''

def Det(a,b,c): return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def area2(p,q,r): return -(q[0]-p[0])*(r[1]-p[1])+(q[1]-p[1])*(r[0]-p[0])	

def convex_hull(pts):
	up, dn = [], []
	for p in pts:
		while len(up)>1 and area2(up[-2],up[-1],p) >= 0: up.pop()
		while len(dn)>1 and area2(dn[-2],dn[-1],p) <= 0: dn.pop()
		up.append(p)
		dn.append(p)
	return dn + up[1:-1][::-1]

def in_convex(l, p):
	a, b = 1, len(l)-1
	if Det(l[0],l[a],l[b]) > 0: a,b = b,a
	if Det(l[0],l[a],p) >= 0 or Det(l[0],l[b],p) <= 0: return False
	while abs(a-b)>1:
		c = (a+b)//2
		if Det(l[0],l[c],p) > 0:
			b = c
		else:
			a = c
	return Det(l[a],l[b],p) < 0


def solve(points,queries):
	points = sorted(list(set(points)))
	layers = []

	while points:
		layer = convex_hull(points)
		if len(layer) <= 2: break
		layers.append(layer)
		points = [p for p in points if in_convex(layer,p)]

	res = []
	for q in queries:
		c = 0
		for layer in layers:
			if not in_convex(layer,q): break
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

