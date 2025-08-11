''' Manhattan Crepe Cart 
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/000000000012295c
'''
def count_x(x0,points):
	return sum(1 for x,y,d in points if (d=='E' and x0>x) or (d=='W' and x0<x))


def count_y(y0,points):
	return sum(1 for x,y,d in points if (d=='N' and y0>y) or (d=='S' and y0<y))


def solve(p,q,points):
	px, py, mx, my = 0, 0, count_x(0,points), count_y(0,points)

	for x,y,_ in points:
		for d in range(-1,2,1):
			if 0 <= x+d <= q:
				cnt = count_x(x+d,points)
				if mx < cnt or (mx == cnt and px > x+d):
					px, mx = x+d, cnt
			if 0 <= y+d <= q:
				cnt = count_y(y+d,points)
				if my < cnt or (my == cnt and py > y+d):
					py, my = y+d, cnt
	return px, py


def main():
	from sys import stdin
	
	T = int(stdin.readline().strip())

	for t in range(T):
		p, q = list(map(int, stdin.readline().strip().split()))
		points = []
		for _ in range(p):
			x,y,d = stdin.readline().strip().split()
			x, y = int(x), int(y)
			points.append((x,y,d))
		x, y = solve(p,q,points)
		print('Case #{}: {} {}'.format(t+1, x, y))
 
 
if __name__ == '__main__':
	main()