''' Oversized Pancake Choppers
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef4/00000000003172d1
'''

# pypy2

def gcd(x,y):
	if x > y: x, y = y, x
	if x == 0: return y
	return gcd(y % x, x)


def solveBig(n,d,arr):  # O(D*N)
	arr.sort()

	# possible cut sizes
	sizes = {}
	for x in arr:
		for y in range(1,d+1):
			g = gcd(x,y)
			sizes[x,y] = (x//g,y//g)

	# find max size that gives at least d pieces
	cuts = sorted(list(set(sizes.values())),key=lambda x: 1.*x[0]/x[1])
	idx,lo,hi = 0,0,len(cuts)-1
	while lo <= hi:
		mi = lo + (hi-lo)//2
		x,y = cuts[mi]
		if sum(a*y//x for a in arr) >=d:
			idx = mi
			lo = mi+1
		else:
			hi = mi-1
	tx,ty = cuts[idx]

	# count num fully usable slices for each cut size
	count = {}  # cut size -> (num fully used slices, num pieces created so far)
	for x in arr:
		for y in range(1,d+1):
			if x*ty > tx*y: continue
			xx,yy = sizes[x,y]
			if (xx,yy) not in count: count[xx,yy] = (0,0)
			c1,c2 = count[xx,yy]
			found = c2+y
			count[xx,yy] = (c1+1,found) if found <= d else (c1,found)

	return d - max(c1 for c1,_ in count.values())


def solveSmall(n,d,arr):  # O(D*N^2)
	arr.sort()

	def cut(x,y,d):  # min cuts to make d slices of size x/y
		rem, res = d, 0
		for a in arr:  # slice small -> big (easier to fully use)
			if a*y % x == 0:
				new = a*y // x
				if new > rem: return res + rem
				if new == rem: return res + rem - 1
				rem -= new
				res += new-1

		for a in arr[::-1]:
			if a*y < x: break  # not big enough
			if a*y % x == 0: continue  # already used
			new = a*y // x
			if new >= rem: return res + rem
			rem -= new
			res += new

		return d if rem else res

	seen = set()
	res = d
	for x in arr:  # some slice must be fully used
		for y in range(1,d+1):   # by cutting into 1..d equal pieces
			g = gcd(x, y)
			xx, yy = x//g, y//g
			if (xx,yy) in seen: continue
			seen.add((xx,yy))
			res = min(res, cut(xx,yy,d))
	return res


solve = solveBig



def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		n,d = list(map(int,stdin.readline().strip().split()))
		arr = list(map(int,stdin.readline().strip().split()))
		out = solve(n,d,arr)
		print 'Case #{}: {}'.format(t+1, out)


if __name__ == '__main__':
	# mine()
	main()
